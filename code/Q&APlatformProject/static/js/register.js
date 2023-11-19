// html 从上到下执行
function bindEmailCaptchaClick(){
    $(function(){
    // 通过#获取id标签
    $('#captcha-btn').on("click", function(event){
        // $(this)获取当前jQuery对象
        var curButton = $(this);
        // 阻止默认的点击事件（有可能是提交整个表单）
        event.preventDefault();
        //获取邮箱
        // 这样获取name
        var email = $("input[name='email']").val();
        $.ajax({
            // 不需要完全域名，默认当前所在域名
            url: "/auth/email/captcha?email=" + email,
            method: "GET",
            success:function(result){
                var code = result["code"];
                if(code === 200){
                    var countDown = 5;
                    // 开始倒计时之前，取消按钮的点击事件
                    curButton.off("click")
                    var timer = setInterval(function(){
                        curButton.text(countDown);
                        countDown -= 1;
                        if (countDown <= 0){
                        // 归零定时器
                            clearInterval(timer);
                            curButton.text("获取验证码");
                        //     重新绑定click函数
                            bindEmailCaptchaClick();
                        }
                    }, 1000)
                     // alert("邮箱验证码发送成功")
                }else{
                    alert(result['message']);
                }
            },
            fail: function(error){
                console.log(error);
            }
        })
    })
});
}
// $()这样会在页面完全加载之后才会执行
$(function(){
    bindEmailCaptchaClick();
})