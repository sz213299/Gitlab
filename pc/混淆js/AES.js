//标准算法包   AES、SHA256、MD5 等

const CryptoJS = require('crypto-js')

function _0x66f3q(_0x581773, _0x3b658c) {
    var _0x144afe = '';
    for (i = 2; i < 18; i++) {
        _0x144afe += (_0x581773 % (i + 1) % 9).toString();
    }
    ;
    var _0x5e23cc = CryptoJS.MD5(_0x581773 + "Bxk80i9Rt").toString();
    var _0x4ed4cb = CryptoJS.MD5(_0x144afe + _0x5e23cc).toString().substr(8, 16);
    var _0x205b9c = _0x3b658c.split(_0x5e23cc)[1];
    var _0x52c50a = CryptoJS.enc.Hex.parse(_0x205b9c);
    var _0x5db2de = CryptoJS.enc.Base64.stringify(_0x52c50a);
    var _0x4ed4cb = CryptoJS.enc.Utf8.parse(_0x4ed4cb);
    var _0x3d2ab5 = CryptoJS.AES.decrypt(_0x5db2de, _0x4ed4cb, {
        "iv": CryptoJS.enc.Utf8.parse(_0x144afe),
        "mode": CryptoJS.mode.CBC,
        "padding": CryptoJS.pad.Pkcs7
    });
    return JSON.parse(_0x3d2ab5.toString(CryptoJS.enc.Utf8));

}

data = "1b82afc1172574a8df31fd3913bccbf44f48ad9054fcbe3bed1fe11d86536daf0d731dee4baf0bc5f954cb267f5ca2a1267614c397658d9460ce732899e3b71d73b8d4e867d79704865070fdaa9ef66d13293e20b46f4dc1c9ce7d35a70629e772f2ef44dbb76297dca16d4324b040ca4e1b96857b08a543895a09bf337711522db8e5efc60529e9330e5cda562ef5c72964afc6de9cd9c92e54fb9d46a507fc0d7bc184f75190b27d185e1967da9b64d06f9e595316397ad0596dad9cc65e906f16eba44bcd95668b71a3627308eb6dceb5aaadd65a58cf773ca43cde6998cd4870b0d3a36d85f410b462c5be46e3fa6e654e963781f92e6cea06f53b01ef5041f87559c1f87f4dbd7009ccfe5232e5c121a38c829980e64712a39906e62fc305317c0eda1b0bf478da15f98ea9faa1"


console.log(_0x66f3q("39108", data))