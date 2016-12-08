$(function() {
    getAlarmTimes();
    getLog();
    $("#log-lines").on('change', getLog);

    $("[data-behaviour='log-level']").click(function() {
        var level = $(this).data('log-level');
        $.get('/loglevel/' + level, function() {
            getLog();
        });
    });

    $("[data-behaviour='reboot']").click(function() {
        if (confirm("Do you really want to reboot the clock?")) {
            $.get("/reboot");
        }
    });

    function getAlarmTimes() {
        $.get('/data/alarm_time', function(response) {
            var html = formatDateDiff(response) + " (" + formatDate(response) + ")";
            $("#next-alarm").html(html);
        })

        $.get('/data/alarm_time_check', function(response) {
            var html = formatDateDiff(response) + " (" + formatDate(response) + ")";
            $("#alarm-updated").html(html);
        })
    }

    function getLog() {
        var lines = $("#log-lines").val();
        $.get('/log/' + lines, function(response) {
            $("#log-entries").html(response);
        })
    }

    function formatDate(dateString) {
        // strip off the timezone - Javascript can't cope with this.
        dateString = dateString.substring(0, 19);
        var date = new Date(Date.parse(dateString));
        return date.toDateString() + " " + date.getHours() + ":" + (date.getMinutes()<10?'0':'') + date.getMinutes();
    }

    function formatDateDiff(dateString) {
        // strip off the timezone - Javascript can't cope with this.
        dateString = dateString.substring(0, 19);
        var diff = Date.parse(dateString) - (new Date).getTime();
        var absDiff = Math.abs(diff);

        var hours = Math.floor(absDiff / 3600000);
        var minutes = Math.floor((absDiff - (hours * 3600000)) / 60000);
        var timeDiff;

        if (hours > 0) {
            timeDiff = hours + " hours " + minutes + " minutes";
            }
        else {
            timeDiff = minutes + " minutes";
        }

        return diff > 0 ? "in " + timeDiff : timeDiff + " ago";
    }
});