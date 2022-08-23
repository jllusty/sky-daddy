'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
exports.insanity = exports.crazy = exports.out2 = exports.out = exports.deep = exports.simpleLoose = exports.simple = exports.mapTestInput = exports.specialCharacters = exports.stringTest = void 0;
const ttypes = require("./gen-nodejs/ThriftTest_types");
const Int64 = require("node-int64");
exports.stringTest = "Afrikaans, Alemannisch, Aragonés, العربية, مصرى, " +
    "Asturianu, Aymar aru, Azərbaycan, Башҡорт, Boarisch, Žemaitėška, " +
    "Беларуская, Беларуская (тарашкевіца), Български, Bamanankan, " +
    "বাংলা, Brezhoneg, Bosanski, Català, Mìng-dĕ̤ng-ngṳ̄, Нохчийн, " +
    "Cebuano, ᏣᎳᎩ, Česky, Словѣ́ньскъ / ⰔⰎⰑⰂⰡⰐⰠⰔⰍⰟ, Чӑвашла, Cymraeg, " +
    "Dansk, Zazaki, ދިވެހިބަސް, Ελληνικά, Emiliàn e rumagnòl, English, " +
    "Esperanto, Español, Eesti, Euskara, فارسی, Suomi, Võro, Føroyskt, " +
    "Français, Arpetan, Furlan, Frysk, Gaeilge, 贛語, Gàidhlig, Galego, " +
    "Avañe'ẽ, ગુજરાતી, Gaelg, עברית, हिन्दी, Fiji Hindi, Hrvatski, " +
    "Kreyòl ayisyen, Magyar, Հայերեն, Interlingua, Bahasa Indonesia, " +
    "Ilokano, Ido, Íslenska, Italiano, 日本語, Lojban, Basa Jawa, " +
    "ქართული, Kongo, Kalaallisut, ಕನ್ನಡ, 한국어, Къарачай-Малкъар, " +
    "Ripoarisch, Kurdî, Коми, Kernewek, Кыргызча, Latina, Ladino, " +
    "Lëtzebuergesch, Limburgs, Lingála, ລາວ, Lietuvių, Latviešu, Basa " +
    "Banyumasan, Malagasy, Македонски, മലയാളം, मराठी, مازِرونی, Bahasa " +
    "Melayu, Nnapulitano, Nedersaksisch, नेपाल भाषा, Nederlands, ‪" +
    "Norsk (nynorsk)‬, ‪Norsk (bokmål)‬, Nouormand, Diné bizaad, " +
    "Occitan, Иронау, Papiamentu, Deitsch, Polski, پنجابی, پښتو, " +
    "Norfuk / Pitkern, Português, Runa Simi, Rumantsch, Romani, Română, " +
    "Русский, Саха тыла, Sardu, Sicilianu, Scots, Sámegiella, Simple " +
    "English, Slovenčina, Slovenščina, Српски / Srpski, Seeltersk, " +
    "Svenska, Kiswahili, தமிழ், తెలుగు, Тоҷикӣ, ไทย, Türkmençe, Tagalog, " +
    "Türkçe, Татарча/Tatarça, Українська, اردو, Tiếng Việt, Volapük, " +
    "Walon, Winaray, 吴语, isiXhosa, ייִדיש, Yorùbá, Zeêuws, 中文, " +
    "Bân-lâm-gú, 粵語";
exports.specialCharacters = 'quote: \" backslash:' +
    ' forwardslash-escaped: \/ ' +
    ' backspace: \b formfeed: \f newline: \n return: \r tab: ' +
    ' now-all-of-them-together: "\\\/\b\n\r\t' +
    ' now-a-bunch-of-junk: !@#$%&()(&%$#{}{}<><><' +
    ' char-to-test-json-parsing: ]] \"]] \\" }}}{ [[[ ';
exports.mapTestInput = {
    "a": "123", "a b": "with spaces ", "same": "same", "0": "numeric key",
    "longValue": exports.stringTest, stringTest: "long key"
};
exports.simple = [
    ['testVoid', undefined],
    ['testString', 'Test'],
    ['testString', ''],
    ['testString', exports.stringTest],
    ['testString', exports.specialCharacters],
    ['testByte', 1],
    ['testByte', 0],
    ['testByte', -1],
    ['testByte', -127],
    ['testI32', -1],
    ['testDouble', -5.2098523],
    ['testDouble', 7.012052175215044],
    ['testEnum', ttypes.Numberz.ONE]
];
exports.simpleLoose = [
    ['testI64', 5],
    ['testI64', -5],
    ['testI64', 734359738368],
    ['testI64', -34359738368],
    ['testI64', -734359738368],
    ['testTypedef', 69]
];
var mapout = {};
for (var i = 0; i < 5; ++i) {
    mapout[i] = i - 10;
}
exports.deep = [
    ['testMap', mapout],
    ['testSet', [1, 2, 3]],
    ['testList', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
    ['testStringMap', exports.mapTestInput]
];
exports.out = new ttypes.Xtruct({
    string_thing: 'Zero',
    byte_thing: 1,
    i32_thing: -3,
    i64_thing: new Int64(1000000)
});
exports.out2 = new ttypes.Xtruct2();
exports.out2.byte_thing = 1;
exports.out2.struct_thing = exports.out;
exports.out2.i32_thing = 5;
exports.crazy = new ttypes.Insanity({
    "userMap": { "5": new Int64(5), "8": new Int64(8) },
    "xtructs": [new ttypes.Xtruct({
            "string_thing": "Goodbye4",
            "byte_thing": 4,
            "i32_thing": 4,
            "i64_thing": new Int64(4)
        }), new ttypes.Xtruct({
            "string_thing": "Hello2",
            "byte_thing": 2,
            "i32_thing": 2,
            "i64_thing": new Int64(2)
        })]
});
exports.insanity = {
    "1": { "2": exports.crazy, "3": exports.crazy },
    "2": { "6": { "userMap": {}, "xtructs": [] } }
};
