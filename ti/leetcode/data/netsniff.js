var page = require('webpage').create();

// add cookies
phantom.addCookie({
    name: 'PHPSESSID',
    value: 'mfhvzo1ilv2vi40wctgqz2wvbehxe4w4',
    domain: 'oj.leetcode.com'
});
phantom.addCookie({
    name: 'csrftoken',
    value: 'A8TmvFbgmqFRRZh4qc78Nunf9n0HDZju',
    domain: 'oj.leetcode.com'
});

page.onLoadStarted = function () {
    console.log('Start loading...');
};

page.onLoadFinished = function (status) {
    console.log('Loading finished.');
    phantom.exit();
};

page.open('http://oj.leetcode.com/submissions/detail/972337');
