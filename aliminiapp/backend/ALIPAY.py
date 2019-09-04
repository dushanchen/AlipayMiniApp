from django.conf import settings

import logging
import json

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.request.AlipaySystemOauthTokenRequest import AlipaySystemOauthTokenRequest
from alipay.aop.api.request.AlipayUserInfoShareRequest import AlipayUserInfoShareRequest
from alipay.aop.api.request.AlipayTradeCreateRequest import AlipayTradeCreateRequest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')


print(settings.ALIPAY['APP_ID'])
alipay_client_config = AlipayClientConfig()
alipay_client_config.server_url = settings.ALIPAY['SERVER_URL']
alipay_client_config.app_id = settings.ALIPAY['APP_ID']
alipay_client_config.app_private_key = settings.ALIPAY['APP_PRIVATE_KEY']
alipay_client_config.alipay_public_key = settings.ALIPAY['ALIPAY_PUBLIC_KEY']

client = DefaultAlipayClient(alipay_client_config, logger)


def alipay_login(code):
# if __name__ == '__main__':
    # 实例化客户端
 
    
    r = AlipaySystemOauthTokenRequest()
    r.grant_type = 'authorization_code'
    r.code = code

    token = ''
    # 执行API调用
    try:
        response_content = client.execute(r)
        print(response_content)
        return json.loads(response_content)
         
    # "access_token":"authbseB422d57c797db438985f83503236e1X94","alipay_user_id":"20881036483092214769432543019494","expires_in":31536000,"re_expires_in":31536000,"refresh_token":"authbseB7c9bf9bc296140bc9f6bfeefa93caD94","user_id":"2088602252901946"}
    except Exception as e:
        print(e)
        return {}


def create_order(out_trade_no, total_amount, subject, user_id):
 

    request = AlipayTradeCreateRequest()
    request.biz_content = {
        'out_trade_no': out_trade_no,
        'total_amount': total_amount,
        'subject': subject,
        'buyer_id': user_id
    }
    try:
        response_content = client.execute(request)
        result = json.loads(response_content)
        return result
    except:
        return {}


