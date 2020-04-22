from django import http
from django.conf import settings
from meiduo_mall.settings import dev
from django.shortcuts import render
from django.views import View
from QQLoginTool.QQtool import OAuthQQ
from meiduo_mall.utils.response_code import RETCODE


class OAuthQQURLView(View):
    def get(self, request):
        next_url = request.GET.get('next')

        # 创建授权对象
        oauthqq = OAuthQQ(
            settings.QQ_CLIENT_ID,
            settings.QQ_CLIENT_SECRET,
            settings.QQ_REDIRECT_URI,
            next_url
        )
        # 生成授权地址
        login_url = oauthqq.get_qq_url()

        # 响应
        return http.JsonResponse({
            'code': RETCODE.OK,
            'errmsg': "OK",
            'login_url': login_url
        })


class OAuthQQOpenidView(View):
    def get(self, request):
        code = request.GET.get('code')

        oauthqq = OAuthQQ(
            settings.QQ_CLIENT_ID,
            settings.QQ_CLIENT_SECRET,
            settings.QQ_REDIRECT_URI,
            request.GET.get('next')
        )

        # 1.根据code获取token
        token = oauthqq.get_access_token(code)

        # 2.根据token获取openid
        openid = oauthqq.get_open_id(token)

        return http.HttpResponse(openid)