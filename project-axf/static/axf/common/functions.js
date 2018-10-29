function addCart(goods_id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/axf/addCart/',
        type: 'POST',
        data: {'goods_id': goods_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if (data.code === 200) {
                count_price();
                $('#num_' + goods_id).text(data.c_num)
            } else if (data.code === 900) {
                // 不用处理
            } else {
                alert(data.msg)
            }
        },
        error: function () {
            alert('请求失败')
        }
    });
}


function subCart(goods_id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/axf/subCart/',
        type: 'POST',
        data: {'goods_id': goods_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if (data.code === 200) {
                count_price();
                $('#num_' + goods_id).html(data.c_num)
            } else if (data.code === 900) {
                // 不用处理
            } else {
                alert(data.msg)
            }
        },
        error: function () {
            alert('请求失败')
        }
    });
}

function changeSelectStatus(cart_id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url: '/axf/changeSelectStatus/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
            if (data.code === 200) {
                if (data.is_select) {
                    $('#cart_id_' + cart_id).html('√');
                    count_price();
                } else {
                    $('#cart_id_' + cart_id).html('x');
                    count_price();
                }
            }
        },
        error: function () {
            alert('请求失败')
        }
    });
}


function change_order(order_id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url: '/axf/changeOrderStatus/',
        type: 'POST',
        data: {'order_id': order_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if (msg.code === 200) {
                location.href = '/axf/mine/'
            }
        },
        error: function () {
            alert('订单状态修改失败')
        }
    })
}


function all_select(i) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/axf/changeCartAllSelect/',
        type: 'POST',
        data: {'all_select': i},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if (msg.code === 200) {
                count_price();
                for (var i = 0; i < msg.ids.length; i++) {
                    if (msg.flag) {
                        var s1 = '<span onclick="cartchangeselect(' + msg.ids[i] + ')">x</span>';
                        $('#changeselect_' + msg.ids[i]).html(s1);

                        $('#all_select_id').attr({'onclick': 'all_select(1)'});
                        $('#select_id').html('√')
                    } else {
                        var s2 = '<span onclick="cartchangeselect(' + msg.ids[i] + ')">√</span>';
                        $('#changeselect_' + msg.ids[i]).html(s2);

                        $('#all_select_id').attr({'onclick': 'all_select(0)'});
                        $('#select_id').html('x')
                    }
                }
            }
        },
        error: function () {
            alert('请求失败');
        }
    });
}

function count_price() {

    $.get('/axf/countPrice/', function (msg) {
        if (msg.code === 200) {
            $('#count_price').html('总价:' + msg.count_price);
        }
    })
}

$.get('/axf/countPrice/', function (msg) {
    if (msg.code === 200) {
        $('#count_price').html('总价:' + msg.count_price);
    }
});

