const app = getApp()

Page({
  data: {
    hasUserInfo: false,
  },
  onLoad() {
    if(!app.globalData.user_id){
      my.getAuthCode({
        scopes: ['auth_base'],
        success: (res) => {
          my.getAuthCode({
          scopes: ['auth_base'],
          success: (res) => {
          console.info(res.authCode);

          my.request({
            url: app.globalData.domain + 'alipayMiniApp/login/'+ res.authCode+'/',
            success: (res) => {
              console.info(res)
              if(res.data.success){
                app.globalData.user_id = res.data.user_id
                console.info(app.globalData)

              }
            },
          });

          },
        });
      },
    });
    }
    
  },
  
  to_mine: function(){
    my.navigateTo({url:'../mine/mine/'});
  },
  to_pay: function(){
    my.navigateTo({url:'../pay/pay/'});
  }
});


