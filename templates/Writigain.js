

var t;
var seconds = 25*60;

var timer_is_on= false;




function LeadingZero(Time) {

    return (Time < 10) ? "0" + Time : + Time;

}





function timedCount() {
    var minutes = Math.floor(seconds/60);
    seconds -= minutes*60;
    document.getElementById('txt').innerHTML=LeadingZero(minutes) + ":" + LeadingZero(seconds);
    seconds--;
    seconds+=minutes*60;
    if (timer_is_on) {
        setTimeout(timedCount,1000);
    }
}


function doTimer() {
    if (!timer_is_on) {
        timer_is_on = true;
        document.getElementById("toggleTimer").value = "Stop count!";
        timedCount();
    } else {
        timer_is_on = false;
        document.getElementById("toggleTimer").value = "Start count!";

    }
}
/**
 * jQuery.textareaCounter
 * Version 1.0
 * Copyright (c) 2011 c.bavota - http://bavotasan.com
 * Dual licensed under MIT and GPL.
 * Date: 10/20/2011
 **/
(function($){
    $.fn.textareaCounter = function () {
        // setting the defaults
        // $("textarea").textareaCounter({ limit: 100 });
        var defaults = {
            limit: 100
        };

        //noinspection JSDuplicatedDeclaration
        var options = $.extend(defaults, options);

        // and the plugin begins
        return this.each(function() {
            var obj, text, wordcount, limited;

            obj = $(this);
            obj.after('<span style="font-size: 11px; clear: both; margin-top: 3px; display: block;" id="counter-text">Max. '+options.limit+' words</span>');

            obj.keyup(function() {
                text = obj.val();
                if(text === "") {
                    wordcount = 0;
                } else {
                    wordcount = $.trim(text).split(" ").length;
                }
                if(wordcount > options.limit) {
                    $("#counter-text").html('<span style="color: #DD0000;">0 words left</span>');
                    limited = $.trim(text).split(" ", options.limit);
                    limited = limited.join(" ");
                    $(this).val(limited);
                } else {
                    $("#counter-text").html((options.limit - wordcount)+' words left');
                }
            });
        });
    };

    $('textarea').textareaCounter();
})(jQuery);
