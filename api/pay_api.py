import requests
from api.account_api import AccountApi


class PayApi:

    @staticmethod
    def api_creat_user_service(phone, count, item):
        # step1:删除用户数据
        AccountApi.delete_account(phone)
        # 调用api中台接口创建用户
        data = {
            "phone": phone,
            "count": count,
            "item": item
        }
        # 调用创建用户的中台api
        res = requests.post(data=data)
        return res

    @staticmethod
    def h():
        return "lala"