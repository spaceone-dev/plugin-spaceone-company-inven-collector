import logging
from spaceone.core.error import ERROR_REQUIRED_PARAMETER
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)


class DevelopmentMemberConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def verify_client(self, options: dict, secret_data: dict, schema: str):
        """
        """
        self._check_secret_data(secret_data)

    def list_members(self, department_name) -> dict:
        """
        """
        response = {
            'department_name': department_name,
            'members': [
                {
                    'id': 'dev-01', 'name': 'yongsuk', 'part': 'frontend',
                    'email': 'yongsuk@spaceone.com', 'join_year': '2002-03-01'
                },
                {
                    'id': 'dev-02', 'name': 'hyunsuk', 'part': 'frontend',
                    'email': 'hyunsuk@spaceone.com', 'join_year': '2016-02-01'
                },
                {
                    'id': 'dev-03', 'name': 'youngho', 'part': 'backend',
                    'email': 'youngho@spaceone.com', 'join_year': '2020-10-01'
                },
                {
                    'id': 'dev-04', 'name': 'yongsoo', 'part': 'backend',
                    'email': 'yongsoo@spaceone.com', 'join_year': '2018-07-01'
                }
            ]
        }
        return response

    @staticmethod
    def _check_secret_data(secret_data: dict):
        if 'user_email' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.user_email')

        if 'api_key' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.api_key')
