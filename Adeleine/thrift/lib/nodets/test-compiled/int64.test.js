"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Int64 = require("node-int64");
const JSONInt64 = require("json-int64");
const i64types = require("./gen-nodejs/Int64Test_types");
const test = require("tape");
const cases = {
    "should correctly generate Int64 constants": function (assert) {
        const EXPECTED_SMALL_INT64_AS_NUMBER = 42;
        const EXPECTED_SMALL_INT64 = new Int64(42);
        const EXPECTED_MAX_JS_SAFE_INT64 = new Int64(Number.MAX_SAFE_INTEGER);
        const EXPECTED_MIN_JS_SAFE_INT64 = new Int64(Number.MIN_SAFE_INTEGER);
        const EXPECTED_MAX_JS_SAFE_PLUS_ONE_INT64 = new Int64("0020000000000000");
        const EXPECTED_MIN_JS_SAFE_MINUS_ONE_INT64 = new Int64("ffe0000000000000");
        const EXPECTED_MAX_SIGNED_INT64 = new Int64("7fffffffffffffff");
        const EXPECTED_MIN_SIGNED_INT64 = new Int64("8000000000000000");
        const EXPECTED_INT64_LIST = [
            EXPECTED_SMALL_INT64,
            EXPECTED_MAX_JS_SAFE_INT64,
            EXPECTED_MIN_JS_SAFE_INT64,
            EXPECTED_MAX_JS_SAFE_PLUS_ONE_INT64,
            EXPECTED_MIN_JS_SAFE_MINUS_ONE_INT64,
            EXPECTED_MAX_SIGNED_INT64,
            EXPECTED_MIN_SIGNED_INT64
        ];
        assert.ok(EXPECTED_SMALL_INT64.equals(i64types.SMALL_INT64));
        assert.ok(EXPECTED_MAX_JS_SAFE_INT64.equals(i64types.MAX_JS_SAFE_INT64));
        assert.ok(EXPECTED_MIN_JS_SAFE_INT64.equals(i64types.MIN_JS_SAFE_INT64));
        assert.ok(EXPECTED_MAX_JS_SAFE_PLUS_ONE_INT64.equals(i64types.MAX_JS_SAFE_PLUS_ONE_INT64));
        assert.ok(EXPECTED_MIN_JS_SAFE_MINUS_ONE_INT64.equals(i64types.MIN_JS_SAFE_MINUS_ONE_INT64));
        assert.ok(EXPECTED_MAX_SIGNED_INT64.equals(i64types.MAX_SIGNED_INT64));
        assert.ok(EXPECTED_MIN_SIGNED_INT64.equals(i64types.MIN_SIGNED_INT64));
        assert.equal(EXPECTED_SMALL_INT64_AS_NUMBER, i64types.SMALL_INT64.toNumber());
        assert.equal(Number.MAX_SAFE_INTEGER, i64types.MAX_JS_SAFE_INT64.toNumber());
        assert.equal(Number.MIN_SAFE_INTEGER, i64types.MIN_JS_SAFE_INT64.toNumber());
        for (let i = 0; i < EXPECTED_INT64_LIST.length; ++i) {
            assert.ok(EXPECTED_INT64_LIST[i].equals(i64types.INT64_LIST[i]));
        }
        for (let i = 0; i < EXPECTED_INT64_LIST.length; ++i) {
            let int64Object = EXPECTED_INT64_LIST[i];
            assert.ok(i64types.INT64_2_INT64_MAP[JSONInt64.toDecimalString(int64Object)].equals(int64Object));
        }
        assert.end();
    }
};
Object.keys(cases).forEach(function (caseName) {
    test(caseName, cases[caseName]);
});
