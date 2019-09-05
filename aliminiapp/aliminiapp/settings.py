"""
Django settings for aliminiapp project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h@rkjwn)ufh8760!cd9i5&r2cjw91&zcz$8!u4hczksp!^llut'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'backend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aliminiapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aliminiapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False 

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = './media/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


ALIPAY = {
    'SERVER_URL': 'https://openapi.alipay.com/gateway.do',
    'APP_ID': '2019090366819854',
    'APP_PRIVATE_KEY':'MIIEpAIBAAKCAQEAhwRNIv3AECr1pmIbFJY4yHODBbeZG59ihDYViJq/qGuAWMZFQ6hPOmhqpiX+e4fkgfOiK18AYXFFiBkJ2yI7w4s4aJBR7tXDv8S78s/Nal6BhD8aNj5lZPoywDh8twRpT9u9jGmJDRK/4Cqcp6kgLeH+8Gjm8JLReNf9k3n7BJu4ziax43ZgSuyhR7cOe95QhSaOZISI6x547hDGPI/U9hos2Ylsn0StAzXK1GzjTVUvnb6IIT14/dZkkYs8w3w2+ndPmAOaZJXM/mmtiY2Acsvu8hvgVi2o6vnhU0Cd1lAn0bCDb54lBr+w2a6qWSKGL5+7mtfcmcKxZj0mr6IhGwIDAQABAoIBAFwEYXHckJ40ORD5Qc2JCBANMZme5DlAKgtDNO/Rz5dAFMvr7N7MgZqj+TNdJ5AXMHQkkDyQ1ZiTczjrH516OlLtujcBTOXCSFOVCCbW2v+IgyqXOw0G/2GPZzE8DjtJRWDIuOlOL7p6MczcHcHicOz0XiSIygPhe+OpCMgO1TXwy1SZ4fGL1X2slgnztxpcat6/vUfAEQh7R5tKR6lYo8+MGVquOt/n/jMDJsb5/Fpn4N/MRRA6ajVIrrKUSaitDHi8k8ijj17MOyoWKZLWQm6B4rU5+tPn791xMueMCRHj8RjAaC3FoQwJapBXIDbEC7+cr+6p7QC7fBVKo1vOW9ECgYEA6SvNCIsoLHhhg4QDh1WCcxJBoMeiwwMaqtlxsnnbKCYVFLtQ0BSTW/t+DzsKRlArkV9+31aLw8MGWC7YU7F2HpnsFVyC4WjNVSsYcbBCy6FPzBKDf6PMOCpywauLLPQF4oZDiRItxK29OXeyfQjOY9cEdvAIx2WIm18wOnmpMKkCgYEAlDxcl8refoHn3DiUom/15MFuJyekFG/cyLfhNUrVkUtXMY/LWP6dOJizf5bKSKQdozhSSC77cpisXSLNtbdCsyovfDUHqRxdEIv1IqWrLDDWyQlOOPdfayOBdvFElUM3ZwhHEeLjTnv+DioKhpDzUcnGC6LfHDRGk3+TRESW6iMCgYEAjf2LVQmQxEvmbfUlRPOQhcx3RJZtij3IroPN1faYu8E9EyviUWRGPDxRDqtQXXMSpOs3Un/cirCnm2mjeIvXt1jaSEPWu7dbWuLsdsb0VhZ8hnQ7ua2gfg9zZHa3QP+02bYTSFRWpK98TJOUkMmdDXVxlZAkeHBfGOaFcwaFPkkCgYAyzlV1+SQ0+9U6F3JqEjGXC+zzIpUMJCLp8IwRtepo+AeUhxJNGEdOpJew/T+rkgROcvlQoDmyVz2MVmdnBr6npafMzGgpv/zttOp5y4pVhQ+4q6XRxIdBs1OmLp8xAW61s5KYQMljlv/GXwZohLnAqIVma5ZIlmoyF6Gj3lZTPQKBgQCCBmuNgALBYND5nU7AJ/Hd7QpkA5HO1AQ+dPJts70pDYNXsaKmwwVxL3lim3BzDpMTR6e7Jd/bylfVdlRsLrOVxX8s4zRiSP6sR2z1ec9beYhRfhBKy74PGeJ9qYLI3TytI7ORSap5CQ+jt94zdUME/75xdhN0OsRnvCAqIjWWuw==',
    'ALIPAY_PUBLIC_KEY':'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqL8In988psipfmna060xMC30mw80n+2KAYNDCGchLEs6P5uEmUyyiNgim1WjffOr3cS61tlfkbcxiohVDG366jh9ZSIRJFEg6zhqP/2KUcJ5PwOa11QTrB9uS+0ZxTWKBhsa9xk/2hFSvNJp/9fz1cw/h3qPK3a/CvOMRpR1pC0BbCZYrbcXN7h61YTDx6EOIX+D+wGJs74JuqUX0++4AhWYlk0ZHTQk78655ycBK2MF47iM4q9KAbgb0u/0soBzB5ab4ShhPsrM34NA2ugdCYLi6bYV5FUu5KJtwZo9GzaJCdDC0SBXruOuec1ZVtX8yqePDwhW4c4pm/i/eo5NUQIDAQAB',
}







