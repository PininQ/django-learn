$(document).ready(function () {

    $("#username").change(function () {

        var username = $("#username").val();
        $.getJSON("/user/checkuser/", {"username": username}, function (data) {

            if (data["status"] === "200") {
                $("#username_info").html(data["desc"]).css("color", "green");
            } else if (data["status"] === "900") {
                $("#username_info").html(data["desc"]).css("color", "red");
            }

        })
    });

    $("#password").change(function () {
        var password = $("#password").val();
        if (password.length < 6 || password.length > 16) {
            $("#password_info").html("密码长度为6-16").css("color", "red");
        }else{
            $("#password_info").html("");
        }
    });

    $("#password_confirm").change(function () {
        var password = $("#password").val();
        var password_confirm = $(this).val();

        if (password === password_confirm) {
            $("#password_confirm_info").html("两次一致").css("color", "green");
        } else {
            $("#password_confirm_info").html("两次输入不一致").css("color", "red");
        }
    });

});
