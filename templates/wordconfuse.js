
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
        this.wd = null;  // current word group in quiz
        this.count = 0; // number of correct answers
        this.submitted = true;
        // setup click handlers for answers
        $('.ab').each(function () {
            $(this).click(game.answer_click);
        });
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

    answer_click:function () {
        if (game.submitted) {
            return false;
        } else {
            game.submitted = true;
        }
        // check to see if the word is correct
        id = $(this).attr('id');
        if (id == 'a' + game.wd['s']) {
            clearInterval(game.s); // stop the countdown timer
            game.count++; // increase the correct answer count
            $(this).css({
                'opacity':'.6',
                'background':'#3366cc'
            });
            $('.nt').css({
                'backgroundImage':'url("{{STATIC_PREFIX}}img/goodjob.png")'
            });
            $('.nt').fadeIn('slow', function () {
                setTimeout(game.show_answer, 300);
            });

        } else {
            $('.nt').css({
                'backgroundImage':'url("{{STATIC_PREFIX}}img/wronganswer.png")'
            });
            $('.nt').fadeIn('slow', function () {
                setTimeout(game.show_answer, 300);
            });
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
                $('.game-info').html('Turn ' + game.turn + ' / 10');
                game.wd = game.wl[game.turn - 1];
                time = game.unix_time();
                game.sec_left = game.TURNTIME;
                $('.ct').html(game.sec_left);
                game.s = setInterval(function () {
                    if (game.sec_left <= 1) {
                        if (game.submitted) {
                            return false;
                        } else {
                            game.submitted = true;
                        }
                        clearInterval(game.s); // stop the countdown timer
                        $('.nt').css({
                            'backgroundImage':'url("{{STATIC_PREFIX}}img/outoftime.png")'
                        });
                        $('.nt').fadeIn('slow', function () {
                            game.show_answer();
                        });

                    } else {
                        game.sec_left = game.TURNTIME - (game.unix_time() - time);
                        if (game.sec_left >= 1) {
                            // just to be paranoid..
                            $('.ct').html(game.sec_left);
                        }
                    }
                }, 1000);
                $('.qb').html('QUAD TITLE');
                // reset the answer board
                $('.ab').each(function () {
                    $(this).removeAttr("style");
                });
                for (var j = 0; j < game.ANSWERS; j++) {
                    $('div#a' + j + ' .answer').html('<p><a href="javascript:void(0)">' + game.wl[j]['content'] + '</a></p>');
                }
                $('.game-questions').fadeIn('slow', function () {
                    $('.game').fadeIn('500'); // for the first time
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

