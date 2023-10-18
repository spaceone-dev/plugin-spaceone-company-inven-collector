import logging
from spaceone.core.error import ERROR_REQUIRED_PARAMETER
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)


class MyServiceConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def verify_client(self, options: dict, secret_data: dict, schema: str):
        """
        """
        self._check_secret_data(secret_data)

    def get_department_id(self, options: dict, secret_data: dict, schema: str):
        """
        """
        pass

    def list_department_member(self, options: dict, secret_data: dict, schema: str):
        """
        """
        pass

    @staticmethod
    def _check_secret_data(secret_data: dict):
        if 'spaceone_id' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.api_key')

        if 'api_key' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.api_key')
