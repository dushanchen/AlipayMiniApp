
const app = getApp()

Page({
  data: {},
  onLoad() {
   
  },
  pay:function(){
    console.info(app.globalData)
     my.request({
      url: app.globalData.domain + 'alipayMiniApp/pay/',//须加httpRequest域白名单
      method: 'POST',
      data: {//data里的key、value是开发者自定义的
        user_id: app.globalData.user_id,
        money: 0.01,
        subject: 'meta 测试产品',
      },
      dataType: 'json',
      success: function(res) {
        console.info(res)
        if(res.data.success){
          my.tradePay({
            tradeNO: res.data.trade_no,  
            success: function(res) {
              console.info(res)
              my.alert({title:'支付成功, 恭喜你成为脉塔VVIP会员!!', buttonText:'好滴!'})
            },
            fail: function(res) {
                  console.info(res.resultCode);
              },
          });
        }
        
      },
      fail: function(res) {
       my.alert(res);
      },
      complete: function(res) {
        my.hideLoading();
        console.info(res);
      }
    });
  }
});
