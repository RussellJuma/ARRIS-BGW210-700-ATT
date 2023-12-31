from typing import Tuple

from bs4 import BeautifulSoup
from requests import Response
from bs4.element import ResultSet
from Config import Config


class Tools:
    class Network:
        @classmethod
        def resolve_ip(cls) -> str:
            pass

        @classmethod
        def resolve_secure(cls) -> str:
            if True:
                return 'http://'
            else:
                return 'https://'

        @classmethod
        def set_credentials(cls) -> Tuple[str, str, str]:
            if True:
                credentials = Config.BGW210.Credentials.Remote
            else:
                credentials = Config.BGW210.Credentials.Remote
            return credentials.url, credentials.username, credentials.password

        def login_required(self) -> bool:
            pass

        # if html_body.find('title').text == 'Login':

    class Parser:
        @staticmethod
        def get_nonce(response: Response) -> str:
            return BeautifulSoup(response.content, features="html.parser").find('input').attrs.get('value')

        @staticmethod
        def get_table_data(response: Response) -> ResultSet:
            rows = BeautifulSoup(response.content, features="html.parser").findAll('tr')
            return rows

        @staticmethod
        def get_field(response: Response, fields: list) -> dict:
            data = {}
            html_body = BeautifulSoup(response.content, features="html.parser")
            for field in fields:
                data[field] = html_body.find('input', {"name": field}).attrs.get('value')
            return data

        @classmethod
        def parse_fields(cls, response: Response) -> dict:
            data = {}
            rows = cls.get_table_data(response)
            for row in rows:
                try:
                    data[row.find('th').text.split('Default')[0]] = row.find('td').find('input').attrs.get('value')
                except AttributeError:
                    pass
            return data
