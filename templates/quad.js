
var quad = {
    /*
     For testing only


     wl: [
     {'q':'recrimination',
     'a':[
     'To turn into ridicule by addressing in ironical or bantering language',
     'To turn into ridicule by addressing in ironical or bantering language',
     'To turn into ridicule by addressing in ironical or bantering language',
     'To turn into ridicule by addressing in ironical or bantering language',
     ],
     's':1,
     },

     {'q':'advantageous',
     'a':[
     'To turn into ridicule by addressing in ironical or bantering language',
     'To turn into ridicule by addressing in ironical or bantering language',
     'To turn into ridicule by addressing in ironical or bantering language',
     'To turn into ridicule by addressing in ironical or bantering language',
     ],
     's':0,
     },
     ],



     constants */
    ROUNDS:10,
    ANSWERS:5,
    TURNTIME:1500,

    startQuad:function () {

        this.s = null;  //setInterval (for the countdown timer)
        this.turn = 1; // turn count
        this.sec_left = null; // number of seconds left for the countdown timer
        this.submitted = true;
        this.initialized = false;
        this.id = null;
        // setup click handlers for answers
        $('.ab').each(function () {
            $(this).click(quad.answer_click1);
        });
        $('#complete').click(quad.completed);

        // grab the word list
        console.log("before initialize_quad");
        $.ajax({
            url:'{% url initialize_quad %}',
            cache:'false',
            dataType:'json',
            async:'false',
            success:function (quad_tasks) {

                quad.wl = quad_tasks;
                // preload images
                jQuery.each(quad.wl, function (index, value) {

                    if (index == quad.wl.length - 1) {
                        // last image has loaded
                        quad.new_turn();
                    }
                });
            },
            error:function () {
                console.log("ERROR: initialize_quad");
            }
        });


    },
    answer_click1:function () {

        // check to see if the word is correct

        quad.id = $(this).attr('id');
        quad.sec_left = quad.TURNTIME;
        var t;

        for (var i = 0; i < quad.wl.length; i++) {
            if (quad.id == 'a' + i) {
                $('#game').hide();
                $('#taskscreen').fadeIn('500');
                $('#task_info').html('<div class="span-24" style="text-align: center; font-size: 24pt; line-height: 24pt"><p> ' + quad.wl[i]['content'] + '<br/><p id="txt"></p></p></div>');
                $('#complete').html('<div class="span-9">&nbsp;</div> <a href="javascript:void(0)"> <div class="span-6 center button orange" style=" height: 100px; display: table; ">' +
                    '<div style="display: table-cell; vertical-align: middle; font: bold; font-size: 16pt; line-height: 16pt">Click here when complete!</div></div></a>');

                t=setTimeout(function(){startTime()},500);
                function startTime()
                {
                     var minutes = Math.floor(quad.sec_left/60);
                     quad.sec_left -= minutes*60;
                     document.getElementById('txt').innerHTML=LeadingZero(minutes) + ":" + LeadingZero(quad.sec_left);
                    quad.sec_left--;
                    quad.sec_left+=minutes*60;
                    if (quad.sec_left >=0) {
                    t=setTimeout(function(){startTime()},1000);
                    }
                    else {
                        clearTimeout(t);
                        quad.sec_left = 0;
                        quad.time_up();
                    }
                 }
/*
                t = setTimeout(start(),1000);
                   function start() {
                        var minutes = Math.floor(seconds/60);
                        seconds -= minutes*60;
                        document.getElementById('txt').innerHTML=LeadingZero(minutes) + ":" + LeadingZero(seconds);
                        seconds--;
                        seconds+=minutes*60;
                        if (seconds > 0) {
                        t = setTimeout(start(),1000);
                        }
                        else {
                            clearTimeout(t);
                        }
                    }
*/





            }
        }
    },

    completed:function () {
        window.clearInterval()
        if (quad.submitted) {
            return false;
        } else {
            quad.submitted = true;
        }
        // check to see if the word is correct

        for (var i = 0; i < quad.wl.length; i++) {
            if (quad.id == 'a' + i) {
                var time_spent = quad.TURNTIME - quad.sec_left;
                $.ajax({
                    url:'/listigain/'+quad.wl[i]['id']+'/'+time_spent+'/completed',
                    cache:'false',
                    dataType:'json',
                    async:'false',
                    success:function (quad_tasks) {

                        quad.wl = quad_tasks;
                        // preload images
                        jQuery.each(quad.wl, function (index, value) {

                            if (index == quad.wl.length - 1) {
                                // last image has loaded
                                quad.new_turn();
                            }
                        });
                    },
                    error:function () {
                        console.log("ERROR: initialize_quad");
                    }
                });

            }
        }
    },
    time_up:function () {
        window.clearInterval()
        if (quad.submitted) {
            return false;
        } else {
            quad.submitted = true;
        }
        // check to see if the word is correct

        for (var i = 0; i < quad.wl.length; i++) {
            if (quad.id == 'a' + i) {
                var time_spent = quad.TURNTIME - quad.sec_left;
                $.ajax({
                    url:'/listigain/'+quad.wl[i]['id']+'/'+time_spent+'/time_up',
                    cache:'false',
                    dataType:'json',
                    async:'false',
                    success:function (quad_tasks) {

                        quad.wl = quad_tasks;
                        // preload images
                        jQuery.each(quad.wl, function (index, value) {

                            if (index == quad.wl.length - 1) {
                                // last image has loaded
                                quad.new_turn();
                            }
                        });
                    },
                    error:function () {
                        console.log("ERROR: initialize_quad");
                    }
                });

            }
        }
    },
/*
    show_answer:function () {
        clearInterval(game.s); // stop the countdown timer
        // reset opacity
        $('.ab').each(function () {
            $(this).removeAttr("style");
        });
        var wrong_answers = [];
        for (var cnt = 0; cnt < game.wl.length; cnt++) {
            if (cnt != game.wd['s']) {
                wrong_answers.push(cnt);
            }
        }
        jQuery.each(wrong_answers, function (index, value) {
            $('#a' + value).hide("puff", {}, '1000', function () {
                if (index == wrong_answers.length - 1) {
                    //last wrong answer has faded out,
                    //now move the correct one
                    var pos0 = $('#a' + game.wd['s']).position();
                    // change the style

                    $('#a' + game.wd['s']).css({
                        position:'absolute',
                        top:pos0.top

                    }).animate(
                        {
                            top:160,
                            left:145
                        },
                        500, function () {
                            setTimeout(game.new_turn, 900);
                        }
                    );
                }
            });
        });
    },
*/
    new_turn:function () {
        $('.nt').hide();
        clearInterval(quad.s);
        if (quad.turn > quad.ROUNDS) {
            console.log('game over');
            $('#a0').unbind();
            $('#a1').unbind();
            $('#a2').unbind();
            $('#a3').unbind();
            $('#a4').unbind();
            game_over.showscreen();

        } else {
            $('.game-questions').fadeOut('slow', function () {
                //$('.game-info').html('Turn ' + game.turn + ' / 10');
                time = quad.unix_time();
                for (var j = 0; j < quad.wl.length; j++) {
                    $('div#a' + j + ' .answer').html('');
                }
                //$('.ct').html(game.sec_left);
              //  game.s = setInterval(function () {
               //     if (game.sec_left <= 1) {
                  //      if (game.submitted) {
                //            return false;
                 //       } else {
                 //           game.submitted = true;
                   //     }
                       // clearInterval(game.s); // stop the countdown timer
                      //  $('.nt').css({
                     //       'backgroundImage':'url("{{STATIC_PREFIX}}img/outoftime.png")'
                      //  });
                       // $('.nt').fadeIn('slow', function () {
                       //     game.show_answer();
                       // });

                //    } else {
               //         game.sec_left = game.TURNTIME - (game.unix_time() - time);
                 //       if (game.sec_left >= 1) {
                            // just to be paranoid..
                          //  $('.ct').html(game.sec_left);
              //          }
              //      }
              //  }, 1000);

                // reset the answer board
                $('.ab').each(function () {
                    $(this).removeAttr("style");
                });

                for (var j = 0; j < quad.wl.length; j++) {
                    if (j == quad.wl.length - 1) {
                        if (quad.wl[j]['id'] == -1) {
                            if (quad.initialized == false) {
                                window.location.replace('no_tasks');
                            } else {
                                window.location.replace('finished_quad');
                            }

                        }
                    }
                    if (quad.wl[j]['id'] != -1) {
                        $('#qb').html('The Quad');
                        quad.initialized = true;
                        break;
                    }
                }

                for (var j = 0; j < quad.wl.length; j++) {

                    if (quad.wl[j]['id'] == -1) {
                        continue;
                    }
                    else if (j == 0){
                        $('div#alt_title').html('');
                        $('div#a' + j + ' .answer').html('<div class="span-24 center"> <h3>Pick your main task:</h3></div> ' +
                            '<div class="span-4">&nbsp;</div><a href="javascript:void(0)" ><div class="span-16 center button red" style="  height: 200px; display: table; ">' +
                            '<div style="display: table-cell; vertical-align: middle; font: bold; font-size: 16pt; line-height: 16pt"><p class="span-16 no_margin">' + quad.wl[j]['content'] + '</p></div></div></a><div class="span-4">&nbsp;</div>' +
                            '');
                        continue;

                    }
                    else if(j==1) {
                        $('div#alt_title').html('<div class="span-24 center"><h3>Or choose one of the following:</h3></div>');
                        $('div#a' + j + ' .answer').html('' +
                            '<a href="javascript:void(0)" ><div class="span-8 center button orange" style=" height: 150px; display: table; ">' +
                            '<div style="display: table-cell; vertical-align: middle; font: bold; font-size: 14pt;line-height: 14pt"><p class="span-8 no_margin">' + quad.wl[j]['content'] + '</p></div></div></a>');
                    }
                    else {
                    $('div#a' + j + ' .answer').html('<a href="javascript:void(0)" ><div class="span-8 center button orange" style=" height: 150px; display: table; ">' +
                        '<div style="display: table-cell; vertical-align: middle; font: bold; font-size: 14pt;line-height: 14pt"><p class="span-8 no_margin">' + quad.wl[j]['content'] + '</p></div></div></a>');
                    }
                }
                $('.game-questions').fadeIn('slow', function () {
                    $('#taskscreen').hide();
                    $('#game').fadeIn('500'); // for the first time
                    quad.submitted = false; // finally we allow clicks
                });
                quad.turn++;

            });
        }
    },

    unix_time:function () {
        return Math.floor(new Date().getTime() / 1000);
    }

};






    $(document).ready(function () {


        if (typeof console == "undefined") {
            console = { log:function (s) {
            } };
        }
        $('.new').click(function () {
            $('.splash').fadeOut('1000', function () {
                quad.startQuad();
            });

        });
        // on the main page load we show the splash screen
        // and register start and highscores for clicks




        $('.splash').fadeIn('500');
    });

