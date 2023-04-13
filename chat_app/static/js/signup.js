  
$("#registerForm").submit(function(e) {
    e.preventDefault()
    var serializeddata = $(this).serialize();
    console.log(serializeddata)
    $.ajax({
        type: 'POST',
        url: '/',
        data: serializeddata,
        processData: false,
        success: function(data){
            $("#register-success").append('<h3>Register successfully Please login<\h3>')
            location.replace("/login/")

        },
        error: function (response) {
            alert(response.responseJSON.msg)
        }
    });
})