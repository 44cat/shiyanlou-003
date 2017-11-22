""" rmon.views.auth

实现用户认证登录功能
"""

from datetime import datetime
from flask import request

from rmon.models import User
from rmon.common.errors import AuthenticationError
from rmon.common.rest import RestView


class AuthView(RestView):
    """认证视图控制器
    """

    def post(self):
        """登录认证用户

        用户可以使用昵称或者邮箱进行登录，登录成功后返回用于后续认证的 token
        """

        # FIXME 没有处理 data 为 None 的情况
        data = request.get_json()
        if data is None:
            raise AuthenticationError(403, 'Data Is None')
        name = data.get('name')
        password = data.get('password')
        # 每次在虚拟环境下DEBUG就会生成admin/123456
        if not name or not password:
            raise AuthenticationError(403, 'user name or password required')

        # FIXME 只有管理员用户允许登录管理后台
        # 管理员默认登录邮箱为amin＠rmon.com
        user = User.authenticate(name, password)
        # 对user用户进行判断，是否为管理员用户
        if not user.is_admin:
            raise AuthenticationError(403, 'user name or password required')
        user.login_at = datetime.utcnow()
        user.save()
        return {'ok': True, 'token': user.generate_token()}
