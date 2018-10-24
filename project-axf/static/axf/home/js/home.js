$(document).ready(function () {
    setTimeout(function () {
        initTopSwiper();
        initMenuSwiper();
    }, 100)
});

function initTopSwiper() {
    var mySwiper1 = new Swiper('#topSwiper', {
        direction: 'horizontal', // 横向轮播
        loop: true, // 是否循环轮播
        speed: 500, // 轮播速度
        autoplay: 2000, // 切换的时间
        pagination: '.swiper-pagination', // 小圆点
        control: true // 控制左右
    });
}

function initMenuSwiper() {
    var mySwiper2 = new Swiper('#swiperMenu', {
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 2,
        loop: false
    });
}
