$(function () {

    $("#order_payed_list").click(function () {
        window.open("/axf/payed/", target = "_self");
    });

    $("#wait_pay_list").click(function () {
        window.open("/axf/waitPay/", target = "_self");
    });

});