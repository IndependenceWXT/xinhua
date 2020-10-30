// ==UserScript==
// @name         New TamperMonkey Script
// @namespace    http://tampermonkey.net/
// @include        http://spider.vpc.shangjian.tech/*
// @version      0.1
// @description  shows how to use coffeescript compiler
// @author       房天生
// @match        <$URL$>
// @icon           https://www.valuesimplex.com/favicon.ico
// @match          <$URL$>
// @grant          none
// @run-at         document-start
// @require        https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.js

// ==/UserScript==

(function () {
    'use strict';

    // Your code here...
    function xxx() {
        $('xxx')[0];
    };
    window.setInterval(xxx, 500);

})();