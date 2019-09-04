import datetime
import hmac
import hashlib
import requests

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# RSA签名
def rsa_sign(data, rsa_key):
    signature = ''
    try:
        h = SHA256.new(data)
        signature = pkcs1_15.new(rsa_key).sign(h)
    except Exception as err:
        print('RSA签名失败', '', err)
    return signature


def jm_sha256(key, value):
    '''
    sha256加密
    return:加密结果转成16进制字符串形式，并大写
    '''
    hsobj = hashlib.sha256(key.encode("utf-8"))
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest().upper()



params = {}

url = 'https://openapi.alipay.com/gateway.do'
params['app_id'] = '2019090266796417'
params['method'] = 'alipay.system.oauth.token'
params['format'] = 'JSON'
params['charset'] = 'utf-8'
params['sign_type'] = 'RSA2'
params['timestamp'] = '2019-09-02 20:21:12'#datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
params['version'] = '1.0'

app_private_key = 'MIIEowIBAAKCAQEAhIL/TjjOwiKXMEaclEBVJbOyeALKbaSTrCAZez/XYFma3sJrJCHJoBTtJ5T9YQm/MQP7mgSy4kn30195a8lWd0xlpfUtDMdvI4xKoGRst9NwoPDmqvBlzsAQHFREb1vZrYpRjbbv6nlS1p54R78klr/p0UAyo2HUxGDN3T4bnqI2OA7WIPQjbEaN4vg65509IKN5f0k1+HxXynbCMnte4VFeDe/y2Lc4yt1GR7qF/xBZrNAOt3LkYwF2nxEBouRXnE6kT5/RySh4/kokBy4PYTK0ioN+lBQCGxTXoZEVM3O9c44TpjVocR+6x98Uwq6bC5kPgzM10j5n+67zs5h6OwIDAQABAoIBABC5uB/Xa8F1PEALqZfMxvKLS+t57rMIItuG8bBsznKK3NFhGMTmvtxFx+lHFPQ6lrdJGWjHTwzg6Tb0xg6kyxUjv3DDEXybb5u9CW5VPqO1PHIT9gl9blw6Qc5RlJG5tjABVWndvUqLJbmRJv1nUub0Mj8HK10T7BcdYN6cCEBtaSumP0zH47jbOTANqXCwVDQcp/mKHwJAHmTK/c5nXnNuj83f6lfArBH2N6s2aApduXNlnc4q/3l/EiF91dP67VQ5kpGB/0cqu5DG6QdgcS7nmmS7InZEnfnUYsumALgXfXw6S8UceGaklXT5aRVneC8KPtxWM/Hm2PqJUIlJ7YECgYEA6sMfWvSIIp0xaVMF2CuD/zQv2Liygx5RsQd2irCoYp6hL0PUH4T5KLQ8ClHwoHrazsoFz4xvLYlBA85lFm0DK3/rX/9P8iu6JY+kmqReNek1Exf0W5L/jp1AL6gCk/++7KUeL4toWrAsibAKlqFnlybEAm1o8jA5UZOA00hWJwUCgYEAkH/Y3CHNCjGnJy8tgvizlO9lY63D/T05+0hnoDDzw3o9NFi5h1RkUd0etTsr1qM54YFFgWcm8aLVYXeLAuwTo3jFGWL8qVvCa1bNV21plKk8OpEWltRLxzjuA5RFVTD591BsrCthrhczrxBwCNANppn8uq8iZQ2ht8moFu4nYD8CgYB6/+qQvCgLgrKdzWr1fK826f/bm8Gj4yHID/Hy7mX67cPjwLUGIqRsyCng+leJrXSw/bYXrSue/xe6R8w8+La9dtM6w8j+SBzKiz0h7NaThnFRZK6ZwCX3cbpsfamEI23EDSsInBD72uwq47pYe46L6jquTua6ZbvSWucXTAIfhQKBgQCCWLFYsazyGyQ7dpVJZeso2GLPbfozwD1DbWb82+uoU+ZOCBMj/n6YUizXMs8yyP73atM2DcTViBuP1nQxaJ+2gMTbR62/YCSbCywkR3BMR/Uqp6KG4G6TAcnCtMduN8Xk0EmXbXKpxgg7TUqiyHrn5FRUWpNeMNPGpEPam24tpQKBgG2SXkaK8QbOMmNiPB+GTAJbnzEaodRCIFMrpzEx9pts/+KJJ+K0snVsRGssq/YyCm2ByAZB3HewAgiA01Xc0KuTjZ7moxvP/hzI6Q3sQY6DI85olQ7j2WzXibzBSXccZeHjbP5fjq6rgZh3otVPsYAQyXeGQ6GnROG+FfgaOdRs'



stringA = '&'.join(["{0}={1}".format(k, params.get(k))for k in sorted(params)])
# sign = rsa_sign(stringA, app_private_key)
# print(sign)

params['sign'] = 'QoUD1Da3B0yKy/sAL0jI5XqGUdroAXj5YheoFEN3TF5AkELeMUjzkq35ZhnCU0KgNu9wNy9P0i8n3Ra/1Ts16xMDyFrl5zijr5CCX5rWkAS624zGmV8aav5o7Lcao5ft5vde6JewRMphpuacFGFlnsPmmM4bN5uxRAPHbuYr/T1YUddQSgU+2C3iMeNl8Jt72d/Apogl5xIeS5a2GwstE7F9AgqwcfLbE9UYXhpBIXZ6ZJxI8yz20F/PkUuwj2wPSCF2Ye5Dqu23bN8tJstCDRnNMPtzKcKoWStzy42p5qWI6ZEaWzfvoWWMt+IJB64Pj/26RJIr/ECA4r4I3YKXQg=='

params['grant_type'] = 'authorization_code'
params['code'] = '5d24f06f268b4a129e4e0bbdf1ddUX94'
import json

resp = requests.post(url, data=params)
print(resp.text)
