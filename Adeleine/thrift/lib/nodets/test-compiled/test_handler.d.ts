/// <reference types="node" />
import ttypes = require("./gen-nodejs/ThriftTest_types");
import Q = require("q");
import Int64 = require("node-int64");
export declare class SyncThriftTestHandler {
    testVoid(): Q.IPromise<void>;
    testMapMap(hello: number): Q.Promise<{
        [key: number]: {
            [key: number]: number;
        };
    }>;
    testInsanity(argument: ttypes.Insanity): Q.IPromise<{
        [k: number]: any;
    }>;
    testMulti(arg0: any, arg1: number, arg2: Int64, arg3: {
        [k: number]: string;
    }, arg4: ttypes.Numberz, arg5: number): Q.Promise<ttypes.Xtruct>;
    testException(arg: string): Q.IPromise<void>;
    testMultiException(arg0: string, arg1: string): Q.Promise<ttypes.Xtruct>;
    testOneway(sleepFor: number): void;
    testString(thing: string): Q.Promise<string>;
    testBool(thing: boolean): Q.Promise<boolean>;
    testByte(thing: number): Q.Promise<number>;
    testI32(thing: number): Q.Promise<number>;
    testI64(thing: number): Q.Promise<number>;
    testDouble(thing: number): Q.Promise<number>;
    testBinary(thing: Buffer): Q.Promise<Buffer>;
    testStruct(thing: ttypes.Xtruct): Q.Promise<ttypes.Xtruct>;
    testNest(thing: ttypes.Xtruct2): Q.Promise<ttypes.Xtruct2>;
    testMap(thing: {
        [k: number]: number;
    }): Q.Promise<{
        [k: number]: number;
    }>;
    testStringMap(thing: {
        [k: string]: string;
    }): Q.Promise<{
        [k: string]: string;
    }>;
    testSet(thing: number[]): Q.Promise<number[]>;
    testList(thing: number[]): Q.Promise<number[]>;
    testEnum(thing: ttypes.Numberz): Q.Promise<ttypes.Numberz>;
    testTypedef(thing: number): Q.Promise<number>;
}
export declare class AsyncThriftTestHandler {
    private syncHandler;
    constructor();
    testVoid(callback: (result: void) => void): Q.IPromise<void>;
    testMapMap(hello: number, callback: (err: any, result: {
        [k: number]: {
            [k: number]: number;
        };
    }) => void): Q.IPromise<{
        [k: number]: {
            [k: number]: number;
        };
    }>;
    testInsanity(argument: ttypes.Insanity, callback?: (err: any, result: {
        [k: number]: any;
    }) => void): Q.IPromise<{
        [k: number]: any;
    }>;
    testMulti(arg0: any, arg1: number, arg2: Int64, arg3: {
        [k: number]: string;
    }, arg4: ttypes.Numberz, arg5: number, result: Function): Q.IPromise<ttypes.Xtruct>;
    testException(arg: string, result: (err: any) => void): Q.IPromise<void>;
    testMultiException(arg0: string, arg1: string, result: (err: any, res?: ttypes.Xtruct) => void): Q.IPromise<ttypes.Xtruct>;
    testOneway(sleepFor: number, result: Function): void;
    testString(thing: string, callback: (err: any, result: string) => void): Q.IPromise<string>;
    testByte(thing: number, callback: (err: any, result: number) => void): Q.IPromise<number>;
    testBool(thing: boolean, callback: (err: any, result: boolean) => void): Q.IPromise<boolean>;
    testI32(thing: number, callback: (err: any, result: number) => void): Q.IPromise<number>;
    testI64(thing: number, callback: (err: any, result: number) => void): Q.IPromise<number>;
    testDouble(thing: number, callback: (err: any, result: number) => void): Q.IPromise<number>;
    testBinary(thing: Buffer, callback: (err: any, result: Buffer) => void): Q.IPromise<Buffer>;
    testStruct(thing: ttypes.Xtruct, callback: (err: any, result: ttypes.Xtruct) => void): Q.IPromise<ttypes.Xtruct>;
    testNest(thing: ttypes.Xtruct2, callback: (err: any, result: ttypes.Xtruct2) => void): Q.IPromise<ttypes.Xtruct2>;
    testMap(thing: {
        [k: number]: number;
    }, callback: (err: any, result: {
        [k: number]: number;
    }) => void): Q.IPromise<{
        [k: number]: number;
    }>;
    testStringMap(thing: {
        [k: string]: string;
    }, callback: (err: any, result: {
        [k: string]: string;
    }) => void): Q.IPromise<{
        [k: string]: string;
    }>;
    testSet(thing: number[], callback: (err: any, result: number[]) => void): Q.IPromise<number[]>;
    testList(thing: number[], callback: (err: any, result: number[]) => void): Q.IPromise<number[]>;
    testEnum(thing: ttypes.Numberz, callback: (err: any, result: ttypes.Numberz) => void): Q.IPromise<ttypes.Numberz>;
    testTypedef(thing: number, callback: (err: any, result: number) => void): Q.IPromise<number>;
}
