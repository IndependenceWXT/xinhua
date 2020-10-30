// ==UserScript==
// @name         泛采专业版主题
// @namespace    http://tampermonkey.net/
// @include        http://spider.vpc.shangjian.tech/*
// @icon           https://www.valuesimplex.com/favicon.ico
// @require        https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.js
// @grant           GM_xmlhttpRequest
// @version      0.2
// @description  try to take over the world!
// @author       房天生
// @match        http://*/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    // Your code here...
    function enlarge_log() {
        // 拉伸弹出框
        var popups = $(".popup_hover .popup_container");
        for (var i = 0, len = popups.length; i < len; i++) {
            popups[i].style = "height: 90%;width: 90%;max-height: 1217px;";
            // 文本区扩大
            var log = $('.flex_column_bottom > div.planDetail_testBox_log[data-v-ce0dab22]');
            if (log.length > 0) {
                log[0].style.height = '90%';
            }
            var yaml = $('.CodeMirror');
            if (yaml.length > 0) {
                yaml[0].style = 'height: 800px;';
            }
        };
    };
    window.setInterval(enlarge_log, 500);

})();