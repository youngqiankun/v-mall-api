from flask import jsonify, request, current_app
from flask_restful import Resource

from ExtendRegister.db_register import db
from app.models.user.user import User


class UserApi(Resource):

    @staticmethod
    def get():
        # 从路径获取手机号

        mobile = request.args.get('mobile')
        current_app.logger.info('==> mobile:' + mobile)
        # user = User(mobile='15857162166', name='xx')
        # db.session.add(user)
        # db.session.commit()
        return jsonify({
            'code': 0
        })

    @staticmethod
    def put():
        current_app.logger.info('===> put method')
        return jsonify({
            'code': 0,
            'msg': 'put method'
        })

    @staticmethod
    def post():
        current_app.logger.info('===> post method')
        return jsonify({
            'code': 0,
            'msg': 'post method'
        })

    @staticmethod
    def delete():
        current_app.logger.info('===> delete method')
        return jsonify({
            'code': 0,
            'msg': 'delete method'
        })
