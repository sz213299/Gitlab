// 对称加密算法AES  DES做数据解密
//内置方法  en
const zlib = require('pako') //注意替换

const eR = require('crypto-js')
// console.log(zlib)
var eN = function (t) {

    //对象复杂

    //ZP 压缩

    var e, n = zlib.inflate(new Uint8Array(t.match(/[\da-f]{2}/gi).map(function (t) {
        return parseInt(t, 16)
    }))), r = "", i = 16384;
    for (e = 0; e < n.length / i; e++)
        r += String.fromCharCode.apply(null, n.slice(e * i, (e + 1) * i));
    return decodeURIComponent(escape(r += String.fromCharCode.apply(null, n.slice(e * i))))
}
t = 'NaYHai6PCTwyS1vWrJYZY15NK3HXffLJeIiGLEbvxGdumsQsv4ltJ/GShEtXYwwMtrOeiV/PfI8vQuSZZpMt00D6RcnxrFuv9ikdU0iTcO21lKTbZ/m0LpPnTCw2ABnCaVJ4DAyMR8G/HUShMG+BwiYG2rHU4m0JIjLbyREHlMyAsgI3U0kdwKM8p4JAbqXTpyVGtZSjcrI6qYZYQ0ybrEdDnm7z6o4qBzFyGDDbbWo='

// 假设 eN 和 eR 已经被正确定义和引入
function decryptData(t) {
    var decrypted = eN(eR.AES.decrypt(t, eR.enc.Utf8.parse('442a4e88849340e7'), {
        mode: eR.mode.ECB,
        padding: eR.pad.Pkcs7
    }).toString(eR.enc.Hex));

    return decrypted; // 返回解密后的结果
}

// 测试输出
console.log(decryptData(t)); // 用你的加密数据替换

