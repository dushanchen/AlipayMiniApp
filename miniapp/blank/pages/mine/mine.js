const app = getApp()
Page({
  data: {
    userInfo:{},
    show_btn: false
  },
  onLoad() {
     my.request({
       url: app.globalData.domain + 'alipayMiniApp/user/',
       method: 'POST',
       data:{
         action: 'get',
         user_id: app.globalData.user_id
       },
       success: (res) => {
         if(!res.data.success){
           this.setData({
             show_btn:true
           })
         }else{
           this.setData({
             userInfo:res.data.result
           })
         }
       },
     });
  },
  onGetAuthorize(res) {
     my.getOpenUserInfo({
      fail: (res) => {
      },
      success: (res) => {
        let userInfo = JSON.parse(res.response).response // 以下方的报文格式解析两层 response
        if(userInfo){
          this.setData({
            userInfo: userInfo
          })
          console.info(app.globalData)
          my.request({
            url: app.globalData.domain+'alipayMiniApp/user/',
            method:'post',
            data:{
              user_id: app.globalData.user_id,
              action: 'save',
              avatar_url: userInfo.avatar ?userInfo.avatar:'',
              nick_name: userInfo.nickName?userInfo.nickName:'',
              city: userInfo.city?userInfo.city:'',
              province:userInfo.province?userInfo.province:''
            },
            success: (res) => {
              
            },
          });
        }
      }
    });
    },
});
