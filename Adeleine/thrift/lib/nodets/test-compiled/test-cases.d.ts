import ttypes = require('./gen-nodejs/ThriftTest_types');
export declare var stringTest: string;
export declare var specialCharacters: string;
export declare var mapTestInput: {
    a: string;
    "a b": string;
    same: string;
    0: string;
    longValue: string;
    stringTest: string;
};
export declare var simple: ((string | number)[] | (string | undefined)[])[];
export declare var simpleLoose: (string | number)[][];
export declare var deep: ((string | {
    [key: number]: number;
})[] | (string | {
    a: string;
    "a b": string;
    same: string;
    0: string;
    longValue: string;
    stringTest: string;
})[])[];
export declare var out: ttypes.Xtruct;
export declare var out2: ttypes.Xtruct2;
export declare var crazy: ttypes.Insanity;
export declare var insanity: any;
