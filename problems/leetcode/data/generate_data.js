(function() {
    var rows = $('#result_testcases').find('tbody tr');

    var inputs = [];
    var outputs = [];
    $.each(rows, function(i, tr) {
        inputs.push(tr.children[0].textContent);
        outputs.push(tr.children[1].textContent);
    });

    window.webkitRequestFileSystem(
        window.TEMPORARY,
        1024*1024,
        function(fs) {
            fs.root.getFile(
                '.input',
                {
                    create: true
                },
                function(fileEntry) {
                    fileEntry.createWriter(
                        function(fileWriter) {
                            fileWriter.onwriteend = function(e) {
                                console.log('Input completed.');
                            };
                            var blob = new Blob([inputs.join('\n')]);
                            fileWriter.write(blob);
                        }
                    );
                }
            );
            fs.root.getFile(
                '.output',
                {
                    create: true
                },
                function(fileEntry) {
                    fileEntry.createWriter(
                        function(fileWriter) {
                            fileWriter.onwriteend = function(e) {
                                console.log('Output completed.');
                            };
                            var blob = new Blob([outputs.join('\n')]);
                            fileWriter.write(blob);
                        }
                    );
                }
            );
        }
    );
})();