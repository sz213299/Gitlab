const CryptoJS = require('crypto-js')


window = global;


var o = CryptoJS.MD5("getUtilsFromFile")
    , a = CryptoJS.enc.Utf8.parse(o);

//   找a
var u = CryptoJS.enc.Utf8.parse("getClassFromFile");
window.d = function (t) {
    return CryptoJS.AES.decrypt(t, a, {
        iv: u,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8).toString()
}

function main123(t) {
    scriptData = window.d(t)
    scriptData = eval(scriptData)
    return scriptData
}

function r(t) {
    if ("105" == t.substring(0, 3) || "106" == t.substring(0, 3) || "107" == t.substring(0, 3))
        return t;
    if ("NASDAQ" == t.substring(0, 6) || "nasdaq" == t.substring(0, 6))
        return "105." + t.substring(7, 999);
    if ("NYSE" == t.substring(0, 4) || "nyse" == t.substring(0, 4))
        return "106." + t.substring(5, 999);
    if ("AMEX" == t.substring(0, 4) || "amex" == t.substring(0, 4))
        return "107." + t.substring(5, 999);
    if ("HK" == t.substring(0, 2) || "hk" == t.substring(0, 2))
        return "116." + t.substring(3, 999);
    var e = t.substring(0, 1)
        , n = t.substring(0, 2)
        , r = t.substring(0, 3);
    return "920" == r ? "0." + t : "5" == e || "6" == e || "9" == e ? "1." + t : 0 == t.toLowerCase().indexOf("sh") ? "1." + t.substring(2, t.length) : 0 == t.toLowerCase().indexOf("sz") ? "0." + t.substring(2, t.length) : "bk" == n.toLowerCase() ? "90." + t : "000003" == t || "000300" == t ? "1." + t : "009" == r || "126" == r || "110" == r ? "1." + t : "0." + t
}

getHQSecIdByMutiCode = function (t) {
    for (var e = [], n = 0, i = t.split(","); n < i.length; n++) {
        var o = r(i[n]);
        e.push(o)
    }
    return e.join(",")
}