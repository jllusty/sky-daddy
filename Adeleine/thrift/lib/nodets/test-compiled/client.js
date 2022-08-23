"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const assert = require("assert");
const thrift = require("thrift");
var Thrift = thrift.Thrift;
const ThriftTest = require("./gen-nodejs/ThriftTest");
const test_driver = require("./test_driver");
var ThriftTestDriver = test_driver.ThriftTestDriver;
var ThriftTestDriverPromise = test_driver.ThriftTestDriverPromise;
const program = require("commander");
program
    .option("--port <port>", "Set thrift server port number to connect", 9090)
    .option("--promise", "test with promise style functions")
    .option("--protocol", "Set thrift protocol (binary) [protocol]")
    .parse(process.argv);
var port = program.port;
var promise = program.promise;
var options = {
    transport: Thrift.TBufferedTransport,
    protocol: Thrift.TBinaryProtocol
};
var testDriver = promise ? ThriftTestDriverPromise : ThriftTestDriver;
var connection = thrift.createConnection("localhost", port, options);
connection.on("error", function (err) {
    assert(false, err);
});
var client = thrift.createClient(ThriftTest.Client, connection);
runTests();
function runTests() {
    testDriver(client, function (status) {
        console.log(status);
        process.exit(0);
    });
}
exports.expressoTest = function () { };
