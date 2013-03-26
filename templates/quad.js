
var game = {
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
    ANSWERS:4,
    TURNTIME:50,

    startGame:function () {

        this.s = null;  //setInterval (for the countdown timer)
        this.turn = 1; // turn count
        this.sec_left = null; // number of seconds left for the countdown timer
        this.submitted = true;
        this.id = null;
        // setup click handlers for answers
        $('.ab').each(function () {
            $(this).click(game.answer_click1);
        });
        $('#complete').click(game.answer_click2);

        // grab the word list
        console.log("before initialize_quad");
        $.ajax({
            url:'{% url initialize_quad %}',
            cache:'false',
            dataType:'json',
            async:'false',
            success:function (quad_tasks) {

                game.wl = quad_tasks;
                // preload images
                jQuery.each(game.wl, function (index, value) {

                    if (index == game.wl.length - 1) {
                        // last image has loaded
                        game.new_turn();
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

        game.id = $(this).attr('id');
        for (var i = 0; i < game.ANSWERS; i++) {
            if (game.id == 'a' + i) {
                $('#game').hide();
                $('#taskscreen').fadeIn('500');
                $('#task_info').html('<p>' + game.wl[i]['content'] + '</p>');
                $('#complete').html('<p><a href="javascript:void(0)"> Click here when complete!</a></p>');


            }
        }
    },

    answer_click2:function () {
        if (game.submitted) {
            return false;
        } else {
            game.submitted = true;
        }
        // check to see if the word is correct

        for (var i = 0; i < game.ANSWERS; i++) {
            if (game.id == 'a' + i) {
                $.ajax({
                    url:'/listigain/'+game.wl[i]['id']+'/return_quad',
                    cache:'false',
                    dataType:'json',
                    async:'false',
                    success:function (quad_tasks) {

                        game.wl = quad_tasks;
                        // preload images
                        jQuery.each(game.wl, function (index, value) {

                            if (index == game.wl.length - 1) {
                                // last image has loaded
                                game.new_turn();
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
        for (var cnt = 0; cnt < game.ANSWERS; cnt++) {
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
        clearInterval(game.s);
        if (game.turn > game.ROUNDS) {
            console.log('game over');
            $('#a0').unbind();
            $('#a1').unbind();
            $('#a2').unbind();
            $('#a3').unbind();
            game_over.showscreen();

        } else {
            $('.game-questions').fadeOut('slow', function () {
                //$('.game-info').html('Turn ' + game.turn + ' / 10');
                time = game.unix_time();
                game.sec_left = game.TURNTIME;
                for (var j = 0; j < game.ANSWERS; j++) {
                    $('div#a' + j + ' .answer').html('');
                }
                //$('.ct').html(game.sec_left);
                game.s = setInterval(function () {
                    if (game.sec_left <= 1) {
                        if (game.submitted) {
                            return false;
                        } else {
                            game.submitted = true;
                        }
                       // clearInterval(game.s); // stop the countdown timer
                      //  $('.nt').css({
                     //       'backgroundImage':'url("{{STATIC_PREFIX}}img/outoftime.png")'
                      //  });
                       // $('.nt').fadeIn('slow', function () {
                       //     game.show_answer();
                       // });

                    } else {
                        game.sec_left = game.TURNTIME - (game.unix_time() - time);
                        if (game.sec_left >= 1) {
                            // just to be paranoid..
                          //  $('.ct').html(game.sec_left);
                        }
                    }
                }, 1000);
                $('#qb').html('The Quad');
                // reset the answer board
                $('.ab').each(function () {
                    $(this).removeAttr("style");
                });

                for (var j = 0; j < game.ANSWERS; j++) {
                    if (j == game.ANSWERS - 1) {
                        if (game.wl[j]['id'] == -1) {
                            window.location.replace('finished_quad');
                        }
                    }
                    if (game.wl[j]['id'] != -1) {
                        break;
                    }
                }
                for (var j = 0; j < game.ANSWERS; j++) {
                    if (game.wl[j]['id'] == -1) {
                        continue;
                    }
                    else {
                    $('div#a' + j + ' .answer').html('<a href="javascript:void(0)" ><div class="span-12 center" style=" background-color: grey; height: 100px; display: table; ">' +
                        '<div style="display: table-cell; vertical-align: middle; font: bold; font-size: 16pt;"> <p>' + game.wl[j]['content'] + '</p></div></div></a>');
                    }
                }
                $('.game-questions').fadeIn('slow', function () {
                    $('#taskscreen').hide();
                    $('#game').fadeIn('500'); // for the first time
                    game.submitted = false; // finally we allow clicks
                });
                game.turn++;

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
                game.startGame();
            });

        });
        // on the main page load we show the splash screen
        // and register start and highscores for clicks




        $('.splash').fadeIn('500');
    });

