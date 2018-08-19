$(document).ready(function(){
    setTimeout(function(){
        initTopSwiper();
        initMenuSwiper();
    }, 100)

})

function initTopSwiper() {
    var mySwiper1 = new Swiper('#topSwiper', {
        direction: 'horizontal',
        loop: true,
        speed: 500,
        autoplay: 2000,
        pagination: '.swiper-pagination',
        control: true,
    });
};

function initMenuSwiper() {
    var mySwiper2 = new Swiper('#swiperMenu', {
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 2,
        loop: false,
    });
};
