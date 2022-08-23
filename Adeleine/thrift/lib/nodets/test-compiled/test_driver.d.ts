import ThriftTest = require("./gen-nodejs/ThriftTest");
export declare function ThriftTestDriver(client: ThriftTest.Client, callback: (status: string) => void): void;
export declare function ThriftTestDriverPromise(client: ThriftTest.Client, callback: (status: string) => void): void;
