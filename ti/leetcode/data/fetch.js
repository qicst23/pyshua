function waitFor(testFx, onReady, timeOutMillis) {
    var maxtimeOutMillis = timeOutMillis ? timeOutMillis : 8000,
        start = new Date().getTime(),
        condition = false,
        interval = setInterval(function() {
            if (
                (new Date().getTime() - start < maxtimeOutMillis) &&
                    !condition) {
                // If not time-out yet and condition not yet fulfilled
                condition =
                    (typeof(testFx) === 'string' ? eval(testFx) : testFx());
            } else {
                if (!condition) {
                    console.log("'waitFor()' timeout");
                    phantom.exit(1);
                } else {
                    // Condition fulfilled (timeout and/or condition is 'true')
                    typeof(onReady) === 'string' ? eval(onReady) : onReady();
                    clearInterval(interval); //< Stop this interval
                }
            }
        }, 250); //< repeat check every 250ms
}


var page = require('webpage').create();
var fs = require('fs');

// add cookies
phantom.addCookie({
    name: 'PHPSESSID',
    value: '5qd9rcnszk8gsfxnixm4q3szmnx3nttg',
    domain: 'oj.leetcode.com'
});
phantom.addCookie({
    name: 'csrftoken',
    value: 'A8TmvFbgmqFRRZh4qc78Nunf9n0HDZju',
    domain: 'oj.leetcode.com'
});

function fetchSubmissionDetails(url) {
    page.open(url, function(status) {
        if (status !== 'success') {
            console.log('Unable to access network');
        } else {
            page.evaluate(function() {
                $('#show_all').click();
            });
            // Wait for 'signin-dropdown' to be visible
            waitFor(function() {
                // Check in the page if a specific element is now visible
                return page.evaluate(function() {
                    return $('#result_testcases').is(':visible');
                });
            }, function() {
                var pageResults = page.evaluate(function() {
                    var rows = $('#result_testcases').find('tbody tr');
                    var inputs = [];
                    var outputs = [];
                    $.each(rows, function(i, tr) {
                        inputs.push(tr.children[0].textContent);
                        outputs.push(tr.children[1].textContent);
                    });
                    return {
                        inputs: inputs,
                        outputs: outputs
                    };
                });
                fs.write(
                    'input', pageResults.inputs.join('\n')
                );
                fs.write(
                    'output', pageResults.outputs.join('\n')
                );
                phantom.exit();
            });
        }
    });
}

var url = 'http://oj.leetcode.com/submissions/detail/' + require('system').args[1] + '/';
fetchSubmissionDetails(url);