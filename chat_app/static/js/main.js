
$('#send-msg').click(function () {
    
    var inputData = $("#message").val();
    $('#main-chat').append('<div><p class="left-chat">'+inputData+'</p></div>');
    $('#main-chat').append('<div><p class="right-chat" id="lastpost">...</p></div>');
    $.ajax({
        type: "post",
        url: "/chat/",
        data: {"text":inputData},
        success: function(data){
            let msg = data.msg;
            $('#main-chat #lastpost:last').fadeOut()
            $('#main-chat').append('<div><p class="right-chat">'+msg+'</p></div>');
            location.reload()
        },
        error: function (response){
            alert(response.responseJSON.msg)
            location.reload()
        }
    });
});
