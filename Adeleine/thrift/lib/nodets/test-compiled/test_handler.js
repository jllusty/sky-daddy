"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AsyncThriftTestHandler = exports.SyncThriftTestHandler = void 0;
const ttypes = require("./gen-nodejs/ThriftTest_types");
const thrift = require("thrift");
var Thrift = thrift.Thrift;
const Q = require("q");
class SyncThriftTestHandler {
    testVoid() {
        return Q.resolve(undefined);
    }
    testMapMap(hello) {
        var mapmap = [];
        var pos = [];
        var neg = [];
        for (var i = 1; i < 5; i++) {
            pos[i] = i;
            neg[-i] = -i;
        }
        mapmap[4] = pos;
        mapmap[-4] = neg;
        return Q.resolve(mapmap);
    }
    testInsanity(argument) {
        const first_map = [];
        const second_map = [];
        first_map[ttypes.Numberz.TWO] = argument;
        first_map[ttypes.Numberz.THREE] = argument;
        const looney = new ttypes.Insanity();
        second_map[ttypes.Numberz.SIX] = looney;
        const insane = [];
        insane[1] = first_map;
        insane[2] = second_map;
        return Q.resolve(insane);
    }
    testMulti(arg0, arg1, arg2, arg3, arg4, arg5) {
        var hello = new ttypes.Xtruct();
        hello.string_thing = 'Hello2';
        hello.byte_thing = arg0;
        hello.i32_thing = arg1;
        hello.i64_thing = arg2;
        return Q.resolve(hello);
    }
    testException(arg) {
        if (arg === 'Xception') {
            var x = new ttypes.Xception();
            x.errorCode = 1001;
            x.message = arg;
            throw x;
        }
        else if (arg === 'TException') {
            throw new Thrift.TException(arg);
        }
        else {
            return Q.resolve();
        }
    }
    testMultiException(arg0, arg1) {
        if (arg0 === ('Xception')) {
            var x = new ttypes.Xception();
            x.errorCode = 1001;
            x.message = 'This is an Xception';
            throw x;
        }
        else if (arg0 === ('Xception2')) {
            var x2 = new ttypes.Xception2();
            x2.errorCode = 2002;
            x2.struct_thing = new ttypes.Xtruct();
            x2.struct_thing.string_thing = 'This is an Xception2';
            throw x2;
        }
        var res = new ttypes.Xtruct();
        res.string_thing = arg1;
        return Q.resolve(res);
    }
    testOneway(sleepFor) {
    }
    testString(thing) {
        return Q.resolve(thing);
    }
    testBool(thing) {
        return Q.resolve(thing);
    }
    testByte(thing) {
        return Q.resolve(thing);
    }
    testI32(thing) {
        return Q.resolve(thing);
    }
    testI64(thing) {
        return Q.resolve(thing);
    }
    testDouble(thing) {
        return Q.resolve(thing);
    }
    testBinary(thing) {
        return Q.resolve(thing);
    }
    testStruct(thing) {
        return Q.resolve(thing);
    }
    testNest(thing) {
        return Q.resolve(thing);
    }
    testMap(thing) {
        return Q.resolve(thing);
    }
    testStringMap(thing) {
        return Q.resolve(thing);
    }
    testSet(thing) {
        return Q.resolve(thing);
    }
    testList(thing) {
        return Q.resolve(thing);
    }
    testEnum(thing) {
        return Q.resolve(thing);
    }
    testTypedef(thing) {
        return Q.resolve(thing);
    }
}
exports.SyncThriftTestHandler = SyncThriftTestHandler;
class AsyncThriftTestHandler {
    constructor() {
        this.syncHandler = new SyncThriftTestHandler();
    }
    testVoid(callback) {
        callback(undefined);
        return Q.resolve();
    }
    testMapMap(hello, callback) {
        var mapmap = [];
        var pos = [];
        var neg = [];
        for (var i = 1; i < 5; i++) {
            pos[i] = i;
            neg[-i] = -i;
        }
        mapmap[4] = pos;
        mapmap[-4] = neg;
        callback(null, mapmap);
        return Q.resolve();
    }
    testInsanity(argument, callback) {
        const first_map = [];
        const second_map = [];
        first_map[ttypes.Numberz.TWO] = argument;
        first_map[ttypes.Numberz.THREE] = argument;
        const looney = new ttypes.Insanity();
        second_map[ttypes.Numberz.SIX] = looney;
        const insane = [];
        insane[1] = first_map;
        insane[2] = second_map;
        if (callback !== undefined) {
            callback(null, insane);
        }
        return Q.resolve();
    }
    testMulti(arg0, arg1, arg2, arg3, arg4, arg5, result) {
        var hello = this.syncHandler.testMulti(arg0, arg1, arg2, arg3, arg4, arg5);
        hello.then(hello => result(null, hello));
        return Q.resolve();
    }
    testException(arg, result) {
        if (arg === 'Xception') {
            var x = new ttypes.Xception();
            x.errorCode = 1001;
            x.message = arg;
            result(x);
        }
        else if (arg === 'TException') {
            result(new Thrift.TException(arg));
        }
        else {
            result(null);
        }
        return Q.resolve();
    }
    testMultiException(arg0, arg1, result) {
        if (arg0 === ('Xception')) {
            var x = new ttypes.Xception();
            x.errorCode = 1001;
            x.message = 'This is an Xception';
            result(x);
        }
        else if (arg0 === ('Xception2')) {
            var x2 = new ttypes.Xception2();
            x2.errorCode = 2002;
            x2.struct_thing = new ttypes.Xtruct();
            x2.struct_thing.string_thing = 'This is an Xception2';
            result(x2);
        }
        else {
            var res = new ttypes.Xtruct();
            res.string_thing = arg1;
            result(null, res);
        }
        return Q.resolve();
    }
    testOneway(sleepFor, result) {
        this.syncHandler.testOneway(sleepFor);
    }
    testString(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testByte(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testBool(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testI32(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testI64(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testDouble(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testBinary(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testStruct(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testNest(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testMap(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testStringMap(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testSet(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testList(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testEnum(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
    testTypedef(thing, callback) {
        callback(null, thing);
        return Q.resolve();
    }
}
exports.AsyncThriftTestHandler = AsyncThriftTestHandler;
