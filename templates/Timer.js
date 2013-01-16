/**
 * Created with PyCharm.
 * User: Garner
 * Date: 11/5/12
 * Time: 9:56 PM
 * To change this template use File | Settings | File Templates.
 */
var c=0;
var t;
var timer_is_on= false;

function timedCount() {
    document.getElementById('txt').value=c;
    c++;
    if (timer_is_on) {
        t= setTimeout(timedCount,1000);
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
        stopCount();
    }
}