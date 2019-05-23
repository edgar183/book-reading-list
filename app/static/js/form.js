/*
    javaScript code to interfere HTML form submission for a category, author and publisher and refresh only specific div in new book form.
    This action preserves data entered in form from being deleted.
*/
$(document).ready(function() {
    $('#add-cat-form').submit(function(e) {
        e.preventDefault();
        console.log("Category form submitted!");
        var catName = $('#Name').val();
        var data = {
            catName: catName
        }
        $.post("/category/categories/add", data).done(function(response) {
            // do stuff with response
            $('#option-div-1').html(response);
            $('#catModal').modal('hide');
        })
        // add additional functionality here

    });
});
$(document).ready(function() {
    $('#add-publisher-form').submit(function(e) {
        e.preventDefault();
        console.log("Publisher form submitted!");
        var publisherName = $('#publisherName').val();
        var data = {
            publisherName: publisherName
        }
        $.post("/publisher/publishers/add", data).done(function(response) {
            // do stuff with response
            $('#option-div-2').html(response);
            $('#publisherModal').modal('hide');
        })
        // add additional functionality here
    });
});
$(document).ready(function() {
    $('#add-author-form').submit(function(e) {
        e.preventDefault();
        console.log("Author form submitted!");
        var authorName = $('#full_name').val();
        var data = {
            authorName: authorName
        }
        $.post("/author/authors/add", data).done(function(response) {
            // do stuff with response
            $('#option-div-3').html(response);
            $('#authorModal').modal('hide');
        })
        // add additional functionality here

    });

});
