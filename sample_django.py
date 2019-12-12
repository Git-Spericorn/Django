from datetime import datetime
import requests
from django.template.loader import render_to_string
from test.utils import request_retry
from test import settings


class UserMixins(object):

    def __init__(self):
        self.user = user

    def get_user_data(self, user):
        """
                    get data of an employee
                    :user headers: user object
                    :return: queryset
                """
        email = str(user.email)

        data = {
            "email": email
        }
        url = self.url + '/auth/login'
        headers = None
        params = None
        response = request_retry(url, headers=headers, params=params, data=data, method='post')
        if response.json().get('success'):
            return response.json()['data'].get('token')
        else:
            return False
