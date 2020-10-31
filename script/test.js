function jsonToUrl(json) {
    var str = "";
    var nullPara = false;
    try {
        json = eval("(" + json + ")");
    } catch (e) {
        console.log("JSON格式有误");
    }
    for (var key in json) {
        if (nullPara) {
            console.log(nullPara)
            if (json[key] === "") {
                continue;
            }
        }
        if (typeof json[key] === "object") {
            str += key + "=" + JSON.stringify(json[key]) + "&";
        } else {
            str += key + "=" + json[key] + "&";
        }
    }
    str = "?" + str;

    str = encodeURI(str);

    return str.substr(0, str.length - 1);
}
function isNumber(val) {
    var regPos = /^\d+(\.\d+)?$/;
    var regNeg = /^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$/;
    return regPos.test(val) || regNeg.test(val);
}
function sortJson(jsonObj) {
    var keys = [];
    for (var key in jsonObj) {
        keys.push(key);
    }
    keys.sort();
    var sortedJson = {};
    for (var i in keys) {
        sortedJson[keys[i]] = jsonObj[keys[i]];
    }
    return sortedJson;
}
function urlFormat(url) {
    var tickDecode = true;
    var tickFormat = true;
    var toJson = true;
    var str = url;
    if (str.split("?").length === 2 && str.charAt(0) === "?") {
        str = str.substr(1);
    }
    var json = {};
    if (tickDecode) {
        str = decodeURIComponent(str);
    }
    if (tickFormat) {
        if (str.indexOf("?") < str.indexOf("&")) {
            str = str.replace(/\?/, "?\r\n");
        }
        str = str.replace(/&/g, "\r\n").replace(/\+/g, " ");
        var lines = str.split("\n");
        var temp = "";
        for (var k in lines) {
            temp += lines[k].replace(/=/, ": ") + "\n";
        }
        str = temp.trim();
    }
    if (toJson) {
        tickDecode ? (str = decodeURIComponent(url)) : (str = url);
        str = str.replace(/\+/g, " ");
        var paramList = [];
        var params = [];
        var paramValue = "";
        if (str.indexOf("?") < 0) {
            if (str.indexOf("&") < 0) {
                if (str.indexOf("=") < 0) {
                    return str;
                    return;
                } else {
                    paramList = str.split("=");
                    paramValue = paramList[1];
                    if (isNumber(paramValue) && paramValue.length < 17) {
                        paramValue = parseFloat(paramValue);
                    }
                    json[paramList[0]] = paramValue;
                }
            } else {
                params = str.split("&");
                for (var i = 0; i < params.length; i++) {
                    paramList = params[i].split("=");
                    paramValue = paramList[1];
                    if (isNumber(paramValue) && paramValue.length < 17) {
                        paramValue = parseFloat(paramValue);
                    }
                    json[paramList[0]] = paramValue;
                }
            }
        } else {
            if (str.indexOf("?") < str.indexOf("&")) {
                params = str.substr(str.indexOf("?") + 1).split("&");
                for (var j = 0; j < params.length; j++) {
                    var key = params[j].substr(0, params[j].indexOf("="));
                    var value = params[j].substr(params[j].indexOf("=") + 1);
                    paramList = [key, value];
                    paramValue = paramList[1];
                    if (isNumber(paramValue) && paramValue.length < 17) {
                        paramValue = parseFloat(paramValue);
                    }
                    json[paramList[0]] = paramValue;
                }
            } else {
                params = str.split("&");
                for (var h = 0; h < params.length; h++) {
                    paramList = params[h].split("=");
                    paramValue = paramList[1];
                    if (isNumber(paramValue) && paramValue.length < 17) {
                        paramValue = parseFloat(paramValue);
                    }
                    json[paramList[0]] = paramValue;
                }
            }
        }
        return JSON.stringify(json, null, 5);
    } else {
        return str;
    }
}
function dedupURIParam(url) {
    params = url.split("?");
    if (params.length < 2) {
        return url;
    }
    var baseurl = params[0];
    var query = params[1];

    var json = urlFormat(query);
    if (json == query) {
        return query;
    } else {
        var new_url = baseurl + jsonToUrl(json);
        return new_url;
    }
}
var url = "https://juejin.im/?1=1&2=";

var new_url = dedupURIParam(url);
if (new_url == url) {
    console.log(url);
} else {
    console.log(new_url);
}
