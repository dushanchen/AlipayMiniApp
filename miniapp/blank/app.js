App({
  onLaunch(options) {
    // 第一次打开
    // options.query == {number:1}
    console.info('App onLaunch');
    
  },
  onShow(options) {
    // 从后台被 scheme 重新打开
    // options.query == {
  },
  globalData:{
    // domain: 'http://10.145.107.7:8000/'
    domain: 'https://zhuti.metatype.cn/'
  }
});
