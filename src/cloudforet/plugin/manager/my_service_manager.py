import logging

from cloudforet.plugin.lib.manager.collector_manager import CollectorManager
from cloudforet.plugin.connector.my_service_connector import MyServiceConnector
from cloudforet.plugin.model.collector import CollectorPluginInfo

_LOGGER = logging.getLogger(__name__)


class MyServiceManager(CollectorManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_service_connector: MyServiceConnector = self.locator.get_connector(MyServiceConnector)
        self.provider = 'custom_provider'
        self.cloud_service_group = 'Custom'
        self.cloud_service_type = None

    @staticmethod
    def init_response(options: dict) -> dict:
        return CollectorPluginInfo.metadata.dict()

    def verify_client(self, options: dict, secret_data: dict, schema: str = None) -> None:
        self.my_service_connector.verify_client(options, secret_data, schema)

    def collect(self, options, secret_data, schema):
        pass
