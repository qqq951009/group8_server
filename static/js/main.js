// 等待畫面元素載入完成以後再執行程式
$(document).ready(function () {
    // 畫面元素載入完成後要執行的流程
    // 為.navbar裡面的.nav-link綁定點擊事件
    $('.navbar .nav-link, #goBackBtn').click(function () {
        console.log("這個按鈕被點擊了");
        // 1. 取得移動的目標
        var target = $(this).attr('href');
        // 2. 取得目標的y座標
        var position = $(target).offset().top;
        // 3. (停止並)執行動畫 .animate({}, 動畫時間)
        $('html, body').stop().animate({
            scrollTop: position
        }, 300);
    });
});