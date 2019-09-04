from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import * 

import json
import random
import datetime
from .ALIPAY import alipay_login, create_order
# Create your views here.



def login(request, code):
	ctx = {}

	result = alipay_login(code)
	if result:
		if 'user_id' in result:
			user_id = result['user_id']
			alipay_user_id = result['alipay_user_id']
			request.session['user_id'] = user_id

			exists = True

			if not User.objects.filter(user_id=user_id).exists():
				User.objects.create(user_id=user_id, alipay_user_id=alipay_user_id)
				exists = False

			return JsonResponse({'success':True, 'user_id': result['user_id'], 'exists': exists})

	return JsonResponse({'success':False})


@csrf_exempt
def user(request):
	ctx = {}
	if request.method == 'POST':
		print(request.body)
		if isinstance(request.body, bytes):
			params = json.loads(request.body.decode('utf-8'))
		else:
			params = json.loads(request.body)

		if params['action'] == 'save':
			user_id = params['user_id']
			avatar_url = params['avatar_url']
			nick_name = params['nick_name']
			province = params['province']
			city = params['city']

			User.objects.filter(user_id=user_id).update(avatar_url=avatar_url, nick_name=nick_name, city=city, province=province, updated=True)
			return JsonResponse({'success':True})

		if params['action'] == 'get':
			user_id = params['user_id']
			user = User.objects.filter(user_id=user_id, updated=True).first()
			if user:
				return JsonResponse({'success':True, 'result':{
					'avatar': user.avatar_url,
					'nickName': user.nick_name,
					'city': user.city,
					'province': user.province,
				}})
			else:
				return JsonResponse({'success':False})


@csrf_exempt
def pay(request):

	if isinstance(request.body, bytes):
		params = json.loads(request.body.decode('utf-8'))
	else:
		params = json.loads(request.body)
	print(params)
	user_id = params['user_id']
	money = params['money']
	subject = params['subject']
	out_trade_no = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.random()).replace('.','')

	user = User.objects.filter(user_id=user_id).first()
	my_order = Order.objects.create(
		out_trade_no=out_trade_no,
		user=user,
		money=money,
		subject=subject
		)

	order = create_order(out_trade_no, money, subject, user_id)
	if 'trade_no' in order: 
		my_order.trade_no = order['trade_no']
		my_order.save()

		return JsonResponse({'success': True, 'trade_no': order['trade_no']})
	else:
		msg = '下单失败 '

		if 'msg' in order:
			msg = order['msg']
		if 'sub_msg' in order:
			msg += order['sub_msg']
		return JsonResponse({'success': False, 'msg': msg})











