import json
import logging
import traceback

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.domain.AlipayTradeAppPayModel import AlipayTradeAppPayModel
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayOfflineMaterialImageUploadRequest import AlipayOfflineMaterialImageUploadRequest
from alipay.aop.api.request.AlipayTradeAppPayRequest import AlipayTradeAppPayRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.request.AlipayTradeCreateRequest import AlipayTradeCreateRequest


from alipay.aop.api.response.AlipayOfflineMaterialImageUploadResponse import AlipayOfflineMaterialImageUploadResponse
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')


if __name__ == '__main__':
    """
    设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
    """
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
    alipay_client_config.app_id = '2019090366819854'
    alipay_client_config.app_private_key = 'MIIEpAIBAAKCAQEAhwRNIv3AECr1pmIbFJY4yHODBbeZG59ihDYViJq/qGuAWMZFQ6hPOmhqpiX+e4fkgfOiK18AYXFFiBkJ2yI7w4s4aJBR7tXDv8S78s/Nal6BhD8aNj5lZPoywDh8twRpT9u9jGmJDRK/4Cqcp6kgLeH+8Gjm8JLReNf9k3n7BJu4ziax43ZgSuyhR7cOe95QhSaOZISI6x547hDGPI/U9hos2Ylsn0StAzXK1GzjTVUvnb6IIT14/dZkkYs8w3w2+ndPmAOaZJXM/mmtiY2Acsvu8hvgVi2o6vnhU0Cd1lAn0bCDb54lBr+w2a6qWSKGL5+7mtfcmcKxZj0mr6IhGwIDAQABAoIBAFwEYXHckJ40ORD5Qc2JCBANMZme5DlAKgtDNO/Rz5dAFMvr7N7MgZqj+TNdJ5AXMHQkkDyQ1ZiTczjrH516OlLtujcBTOXCSFOVCCbW2v+IgyqXOw0G/2GPZzE8DjtJRWDIuOlOL7p6MczcHcHicOz0XiSIygPhe+OpCMgO1TXwy1SZ4fGL1X2slgnztxpcat6/vUfAEQh7R5tKR6lYo8+MGVquOt/n/jMDJsb5/Fpn4N/MRRA6ajVIrrKUSaitDHi8k8ijj17MOyoWKZLWQm6B4rU5+tPn791xMueMCRHj8RjAaC3FoQwJapBXIDbEC7+cr+6p7QC7fBVKo1vOW9ECgYEA6SvNCIsoLHhhg4QDh1WCcxJBoMeiwwMaqtlxsnnbKCYVFLtQ0BSTW/t+DzsKRlArkV9+31aLw8MGWC7YU7F2HpnsFVyC4WjNVSsYcbBCy6FPzBKDf6PMOCpywauLLPQF4oZDiRItxK29OXeyfQjOY9cEdvAIx2WIm18wOnmpMKkCgYEAlDxcl8refoHn3DiUom/15MFuJyekFG/cyLfhNUrVkUtXMY/LWP6dOJizf5bKSKQdozhSSC77cpisXSLNtbdCsyovfDUHqRxdEIv1IqWrLDDWyQlOOPdfayOBdvFElUM3ZwhHEeLjTnv+DioKhpDzUcnGC6LfHDRGk3+TRESW6iMCgYEAjf2LVQmQxEvmbfUlRPOQhcx3RJZtij3IroPN1faYu8E9EyviUWRGPDxRDqtQXXMSpOs3Un/cirCnm2mjeIvXt1jaSEPWu7dbWuLsdsb0VhZ8hnQ7ua2gfg9zZHa3QP+02bYTSFRWpK98TJOUkMmdDXVxlZAkeHBfGOaFcwaFPkkCgYAyzlV1+SQ0+9U6F3JqEjGXC+zzIpUMJCLp8IwRtepo+AeUhxJNGEdOpJew/T+rkgROcvlQoDmyVz2MVmdnBr6npafMzGgpv/zttOp5y4pVhQ+4q6XRxIdBs1OmLp8xAW61s5KYQMljlv/GXwZohLnAqIVma5ZIlmoyF6Gj3lZTPQKBgQCCBmuNgALBYND5nU7AJ/Hd7QpkA5HO1AQ+dPJts70pDYNXsaKmwwVxL3lim3BzDpMTR6e7Jd/bylfVdlRsLrOVxX8s4zRiSP6sR2z1ec9beYhRfhBKy74PGeJ9qYLI3TytI7ORSap5CQ+jt94zdUME/75xdhN0OsRnvCAqIjWWuw=='
    alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqL8In988psipfmna060xMC30mw80n+2KAYNDCGchLEs6P5uEmUyyiNgim1WjffOr3cS61tlfkbcxiohVDG366jh9ZSIRJFEg6zhqP/2KUcJ5PwOa11QTrB9uS+0ZxTWKBhsa9xk/2hFSvNJp/9fz1cw/h3qPK3a/CvOMRpR1pC0BbCZYrbcXN7h61YTDx6EOIX+D+wGJs74JuqUX0++4AhWYlk0ZHTQk78655ycBK2MF47iM4q9KAbgb0u/0soBzB5ab4ShhPsrM34NA2ugdCYLi6bYV5FUu5KJtwZo9GzaJCdDC0SBXruOuec1ZVtX8yqePDwhW4c4pm/i/eo5NUQIDAQAB'
    client = DefaultAlipayClient(alipay_client_config, logger)

    """
    得到客户端对象。
    注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
    logger参数用于打印日志，不传则不打印，建议传递。
    """
    client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)

    """
    系统接口示例：alipay.trade.pay
    """
    # 对照接口文档，构造请求对象
    # model = AlipayTradePayModel()
    # model.auth_code = "d1ededeca46940b38787b8245eadTX94"
    # model.body = "Iphone6 16G"
    # goods_list = list()
    # goods1 = GoodsDetail()
    # goods1.goods_id = "apple-01"
    # goods1.goods_name = "ipad"
    # goods1.price = 10
    # goods1.quantity = 1
    # goods_list.append(goods1)
    # model.goods_detail = goods_list
    # model.operator_id = "20880065172953653710813653018594"
    # model.out_trade_no = "20180510AB014"
    # model.product_code = "FACE_TO_FACE_PAYMENT"
    # model.scene = "bar_code"
    # model.store_id = ""
    # model.subject = "huabeitest"
    # model.timeout_express = "90m"
    # model.total_amount = 1


    # request = AlipayTradePayRequest(biz_model=model)

    # model = AlipayTradePagePayModel()
    # model.out_trade_no = "pay201805020000226"
    # model.total_amount = 0.01
    # model.subject = "测试"
    # model.body = "支付宝测试"
    # model.product_code = "FAST_INSTANT_TRADE_PAY"
    # settle_detail_info = SettleDetailInfo()
    # settle_detail_info.amount = 1
    # settle_detail_info.trans_in_type = "userId"
    # settle_detail_info.trans_in = "20880065172953653710813653018594"
    # settle_detail_infos = list()
    # settle_detail_infos.append(settle_detail_info)
    # settle_info = SettleInfo()
    # settle_info.settle_detail_infos = settle_detail_infos
    # model.settle_info = settle_info
    # sub_merchant = SubMerchant()
    # sub_merchant.merchant_id = "2088301300153242"
    # model.sub_merchant = sub_merchant
    # request = AlipayTradePagePayRequest(biz_model=model)
    # # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
    # response = client.page_execute(request, http_method="GET")
    # print("alipay.trade.page.pay response:" + response)


    request = AlipayTradeCreateRequest()
    request.biz_content = {
        'out_trade_no':'pay201805020000226',
        'total_amount':0.01,
        'subject':'meta测试产品',
        'buyer_id':'2088602252901946'}

    response_content = client.execute(request)

    print(response_content)
    # response_content = None
    # try:
    #     response_content = client.execute(request)
    # except Exception as e:
    #     print(e)
    # if not response_content:
    #     print("failed execute")
    # else:
    #     response = AlipayTradePayResponse()
    #     # 解析响应结果
    #     response.parse_response_content(response_content)
    #     print(response.body)
    #     if response.is_success():
    #         # 如果业务成功，则通过respnse属性获取需要的值
    #         print("get response trade_no:" + response.trade_no)
    #     else:
    #         # 如果业务失败，则从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
    #         print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)
