/*$(document).ready(function() {
    $('.addCatButton').on('click', function(e) {
        console.log('button triger');
        e.preventDefault();
        console.log('ajax triger');
        $.ajax({
            type: "POST",
            url: "{{ url_for('categories.add_category') }}",
            data: $(this).serialize(),
            success: function(response) {
                alert(response['response']);
            },
            error: function() {
                alert('error');
            }
        });
        console.log('endof ajax');
        return false;
    });
});
*/