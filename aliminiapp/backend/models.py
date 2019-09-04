from django.db import models

# Create your models here.



class User(models.Model):

	user_id = models.CharField(primary_key=True, max_length=100)
	alipay_user_id = models.CharField(null=True, default=None, max_length=100)

	avatar_url = models.CharField(null=True, max_length=200)
	nick_name = models.CharField(null=True, max_length=200)
	province = models.CharField(null=True, max_length=200)
	city = models.CharField(null=True, max_length=200)

	updated = models.BooleanField(default=False)

	def __str__(self):
		return self.nick_name if self.nick_name else self.user_id



class Order(models.Model):

	out_trade_no = models.CharField(primary_key=True, max_length=100)
	trade_no = models.CharField(max_length=100, null=True)

	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	money = models.FloatField()
	subject = models.CharField(max_length=100)


	create_time = models.DateTimeField(auto_now_add=True)
