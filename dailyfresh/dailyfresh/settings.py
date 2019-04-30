#coding=utf-8
"""
Django settings for dailyfresh project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import logging
import django.utils.log
import logging.handlers
import time

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ps1j8s+n@zn2f)f(+6021e7t_devt$(v=o^echzt)(lj8^oq4#'

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
    'df_user',
    'df_goods',
    'tinymce',
    'df_cart',
    'df_order',
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

ROOT_URLCONF = 'dailyfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,('templates'))],
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

WSGI_APPLICATION = 'dailyfresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'localhost',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'aaa',
        'NAME':'tiantian',


    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

STATIC_ROOT = '/var/www/dailyfresh/static/'

#开发阶段上传文件的目录
MEDIA_ROOT = os.path.join(BASE_DIR,'static')
#部署后的上传文件目录
#MEDIA_ROOT = '/var/www/dailyfresh/static'


TINYMCE_DEFAULT_CONFIG = {
    'theme':'advanced',
    'width': 600,
    'height':400,
}

HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# HAYSTACK_DEFAULT_OPERATOR = 'OR'
# 设置每页显示的数目，默认为20，可以自己修改
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20

rq = time.strftime('%Y%m%d', time.localtime(time.time()))

BASE_LOG_DIR = os.path.join(BASE_DIR,"logs")

# LOGGING = {
#     'version': 1,#指明dictConnfig的版本
#     'disable_existing_loggers': False,# 设置True将禁用所有的已经存在的日志配置
#     'formatters': {#格式器
#         'verbose': {#详细
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {#简单
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#      'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {#处理器，在这里定义了三个处理器
#         # 'null': {#Null处理器，所有高于（包括）debug的消息会被传到/dev/null
#         #     'level':'DEBUG',
#         #     'class':'django.utils.log.NullHandler',
#         # },
#         'console':{#流处理器，所有的高于（包括）debug的消息会被传到stderr，使用的是simple格式器
#             'level':'NOTSET',
#             'class':'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'mail_admins': {# 邮件处理器，所有高于（包括）而error的消息会被发送给站点管理员，使用的是special格式器
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false']
#         },
#         'file_handler': {# 文件处理器，所有高于（包括）而error的消息会被发送给站点管理员，使用的是special格式器
#             'level': 'NOTSET',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when':'W0',   # 日志文件每周第一天翻转
#             'filename':'log.txt',   #  日志文件的存储地址
#             'backupCount':500,   # 最多可以保存500个文件
#             'formatter':'verbose'
#         }
#     },
#     'loggers': { # 定义了三个记录器
#         'django': { # django记录器是捕捉所有消息的记录器，没有消息是直接发往django记录器的。使用null处理器，所有高于（包括）info的消息会被发往null处理器，向父层次传递信息
#             'handlers':['console','file_handler'],
#             'propagate': True,
#             'level':'NOTSET',
#         },
#         'django.request': {#所有高于（包括）error的消息会被发往mail_admins处理器，消息不向父层次发送
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'myproject.custom': {# 所有高于（包括）info的消息同时会被发往console和mail_admins处理器，使用special过滤器
#             'handlers': ['console', 'mail_admins'],
#             'level': 'INFO',
#             'filters': ['special']
#         }
#     }
# }


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
#         },
#     },
#     'filters': {
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         },
#         'default': {
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(STATIC_ROOT+'/logs/','all.log'), #或者直接写路径：'c:\logs\all.log',
#             'maxBytes': 1024*1024*5, # 5 MB
#             'backupCount': 5,
#             'formatter':'standard',
#         },
#         'console':{
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         'request_handler': {
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(STATIC_ROOT+'/logs/','script.log'), #或者直接写路径：'filename':'c:\logs\request.log''
#             'maxBytes': 1024*1024*5, # 5 MB
#             'backupCount': 5,
#             'formatter':'standard',
#         },
#         'scprits_handler': {
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(STATIC_ROOT+'/logs/','script.log'), #或者直接写路径：'filename':'c:\logs\script.log'
#             'maxBytes': 1024*1024*5, # 5 MB
#             'backupCount': 5,
#             'formatter':'standard',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default','console'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#         'XieYin.app':{
#             'handlers': ['default','console'],
#             'level': 'DEBUG',
#             'propagate': True
#         },
#         'django.request': {
#             'handlers': ['request_handler'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#         'scripts': { # 脚本专用日志
#             'handlers': ['scprits_handler'],
#             'level': 'INFO',
#             'propagate': False
#         },
#     }
# }

LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
     'handlers': {
         'console':{
             'level':'DEBUG',
             'class':'logging.StreamHandler',
         },
     },
     'loggers': {
         'django.db.backends': {
             'handlers': ['console'],
             'propagate': True,
             'level':'DEBUG',
         },
     }
 }