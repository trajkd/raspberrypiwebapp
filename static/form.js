$(document).on("click touch", "#sendButton", function() {
    name = $("#name").val();
    surname = $("#name").val();
    $.ajax({
        url: '/',
        dataType: 'json',
        method: 'POST',
        data: {name: $("#name").val(), surname: $("#surname").val()},
        success: function(res) {
            $("#success").html("Data sent succesfully");
            return false;
        },
        error: function(error) {
            $("#success").html(error.responseText);
            return false;
        }
    });
});