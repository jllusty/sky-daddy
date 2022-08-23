"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ThriftTestDriverPromise = exports.ThriftTestDriver = void 0;
const test = require("tape");
const ttypes = require("./gen-nodejs/ThriftTest_types");
const thrift = require("thrift");
var Q = thrift.Q;
var TException = thrift.Thrift.TException;
var Int64 = require("node-int64");
const testCases = require("./test-cases");
function ThriftTestDriver(client, callback) {
    test("NodeJS Style Callback Client Tests", function (assert) {
        var checkRecursively = makeRecursiveCheck(assert);
        function makeAsserter(assertionFn) {
            return function (c) {
                var fnName = c[0];
                var expected = c[1];
                client[fnName](expected, function (err, actual) {
                    assert.error(err, fnName + ": no callback error");
                    assertionFn(actual, expected, fnName);
                });
            };
        }
        testCases.simple.forEach(makeAsserter(assert.equal));
        testCases.simpleLoose.forEach(makeAsserter(function (a, e, m) {
            assert.ok(a == e, m);
        }));
        testCases.deep.forEach(makeAsserter(assert.deepEqual));
        client.testMapMap(42, function (err, response) {
            var expected = {
                "4": { "1": 1, "2": 2, "3": 3, "4": 4 },
                "-4": { "-4": -4, "-3": -3, "-2": -2, "-1": -1 }
            };
            assert.error(err, 'testMapMap: no callback error');
            assert.deepEqual(expected, response, "testMapMap");
        });
        client.testStruct(testCases.out, function (err, response) {
            assert.error(err, "testStruct: no callback error");
            checkRecursively(testCases.out, response, "testStruct");
        });
        client.testNest(testCases.out2, function (err, response) {
            assert.error(err, "testNest: no callback error");
            checkRecursively(testCases.out2, response, "testNest");
        });
        client.testInsanity(testCases.crazy, function (err, response) {
            assert.error(err, "testInsanity: no callback error");
            checkRecursively(testCases.insanity, response, "testInsanity");
        });
        client.testException("TException", function (err, response) {
            assert.ok(err instanceof TException, 'testException: correct error type');
            assert.ok(!Boolean(response), 'testException: no response');
        });
        client.testException("Xception", function (err, response) {
            assert.ok(err instanceof ttypes.Xception, 'testException: correct error type');
            assert.ok(!Boolean(response), 'testException: no response');
            assert.equal(err.errorCode, 1001, 'testException: correct error code');
            assert.equal('Xception', err.message, 'testException: correct error message');
        });
        client.testException("no Exception", function (err, response) {
            assert.error(err, 'testException: no callback error');
            assert.ok(!Boolean(response), 'testException: no response');
        });
        client.testOneway(0, function (err, response) {
            assert.error(err, 'testOneway: no callback error');
            assert.strictEqual(response, undefined, 'testOneway: void response');
        });
        checkOffByOne(function (done) {
            client.testI32(-1, function (err, response) {
                assert.error(err, "checkOffByOne: no callback error");
                assert.equal(-1, response);
                assert.end();
                done();
            });
        }, callback);
    });
}
exports.ThriftTestDriver = ThriftTestDriver;
;
function ThriftTestDriverPromise(client, callback) {
    test("Q Promise Client Tests", function (assert) {
        var checkRecursively = makeRecursiveCheck(assert);
        function fail(msg) {
            return function (error, response) {
                if (error !== null) {
                    assert.fail(msg);
                }
            };
        }
        function makeAsserter(assertionFn) {
            return function (c) {
                var fnName = c[0];
                var expected = c[1];
                client[fnName](expected)
                    .then(function (actual) {
                    assertionFn(actual, expected, fnName);
                })
                    .fail(fail("fnName"));
            };
        }
        testCases.simple.forEach(makeAsserter(assert.equal));
        testCases.simpleLoose.forEach(makeAsserter(function (a, e, m) {
            assert.ok(a == e, m);
        }));
        testCases.deep.forEach(makeAsserter(assert.deepEqual));
        Q.resolve(client.testStruct(testCases.out))
            .then(function (response) {
            checkRecursively(testCases.out, response, "testStruct");
        })
            .fail(fail("testStruct"));
        Q.resolve(client.testNest(testCases.out2))
            .then(function (response) {
            checkRecursively(testCases.out2, response, "testNest");
        })
            .fail(fail("testNest"));
        Q.resolve(client.testInsanity(testCases.crazy))
            .then(function (response) {
            checkRecursively(testCases.insanity, response, "testInsanity");
        })
            .fail(fail("testInsanity"));
        Q.resolve(client.testException("TException"))
            .then(function (response) {
            fail("testException: TException");
        })
            .fail(function (err) {
            assert.ok(err instanceof TException);
        });
        Q.resolve(client.testException("Xception"))
            .then(function (response) {
            fail("testException: Xception");
        })
            .fail(function (err) {
            assert.ok(err instanceof ttypes.Xception);
            assert.equal(err.errorCode, 1001);
            assert.equal("Xception", err.message);
        });
        Q.resolve(client.testException("no Exception"))
            .then(function (response) {
            assert.equal(undefined, response);
        })
            .fail(fail("testException"));
        client.testOneway(0, fail("testOneway: should not answer"));
        checkOffByOne(function (done) {
            Q.resolve(client.testI32(-1))
                .then(function (response) {
                assert.equal(-1, response);
                assert.end();
                done();
            })
                .fail(fail("checkOffByOne"));
        }, callback);
    });
}
exports.ThriftTestDriverPromise = ThriftTestDriverPromise;
;
function makeRecursiveCheck(assert) {
    return function (map1, map2, msg) {
        var equal = true;
        var equal = checkRecursively(map1, map2);
        assert.ok(equal, msg);
        function checkRecursively(map1, map2) {
            if (!(typeof map1 !== "function" && typeof map2 !== "function")) {
                return false;
            }
            if (!map1 || typeof map1 !== "object") {
                if ((typeof map1 === "number") && (typeof map2 === "object") &&
                    (map2.buffer) && (map2.buffer instanceof Buffer) && (map2.buffer.length === 8)) {
                    var n = new Int64(map2.buffer);
                    return map1 === n.toNumber();
                }
                else {
                    return map1 == map2;
                }
            }
            else {
                return Object.keys(map1).every(function (key) {
                    return checkRecursively(map1[key], map2[key]);
                });
            }
        }
    };
}
function checkOffByOne(done, callback) {
    var retry_limit = 30;
    var retry_interval = 100;
    var test_complete = false;
    var retrys = 0;
    done(function () {
        test_complete = true;
    });
    function TestForCompletion() {
        if (test_complete && callback) {
            callback("Server successfully tested!");
        }
        else {
            if (++retrys < retry_limit) {
                setTimeout(TestForCompletion, retry_interval);
            }
            else if (callback) {
                callback("Server test failed to complete after " +
                    (retry_limit * retry_interval / 1000) + " seconds");
            }
        }
    }
    setTimeout(TestForCompletion, retry_interval);
}
