"use strict";
process.env.HYBRIS_EGLPLATFORM = "wayland";
if (typeof global.pageWindow !== "undefined" && global.pageWindow.loadEngine) {
    global.pageWindow.loadEngine("domless");
    global.pageWindow.animation.start.enable = false;
    global.pageWindow.animation.show.enable = false;
    global.pageWindow.animation.hide.enable = false;
    global.pageWindow.animation.stop.enable = false;
} else {
    require("agil");
}

var lang = require("caf/core/lang");
var Page = require("caf/app/Page");
var TextView = require("caf/ui/TextView");

var HelloPage = lang.extend(Page, {
    constructor: function() {
        HelloPage.superclass.constructor.apply(this);
    },

    destructor: function() {
        HelloPage.superclass.destructor.apply(this);
    },

    onStart: function() {
        var textView = new TextView();
        textView.text = "Hello World, Domless";
        textView.x = 0;
        textView.y = 0;
        textView.width = this.window.width;
        textView.height = this.window.height;
        textView.fontPixelSize = 70;
        textView.textColor = "#FFFFFF";
        textView.background = "#FF6600";
        textView.vAlign = TextView.VAlign.AlignVCenter;
        textView.hAlign = TextView.HAlign.AlignHCenter;
        this.window.addChildView(textView);
    }
});

module.exports = new HelloPage();
