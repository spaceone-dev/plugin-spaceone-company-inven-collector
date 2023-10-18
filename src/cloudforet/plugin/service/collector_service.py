import logging
from typing import Generator

from spaceone.core.service import *
from cloudforet.plugin.manager.my_service_manager import MyServiceManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler
class CollectorService(BaseService):
    def __init__(self, metadata):
        super().__init__(metadata)

    @check_required(['options'])
    def init(self, params):
        """ init plugin by options

        Args:
            params (dict): {
                'options': 'dict',
                'domain_id': 'str'
            }

        Returns:
            plugin_data (dict)
        """

        options = params.get('options', {})

        collector_mgr: MyServiceManager = self.locator.get_manager(MyServiceManager)
        return collector_mgr.init_response(options)

    @transaction
    @check_required(['options', 'secret_data'])
    def verify(self, params):
        """ Verifying collector plugin

        Args:
            params (dict): {
                'options': 'dict',
                'schema': 'str',
                'secret_data': 'dict',
                'domain_id': 'str'
            }

        Returns:
            None
        """
        options = params['options']
        secret_data = params['secret_data']
        schema = params.get('schema')

        collector_mgr: MyServiceManager = self.locator.get_manager(MyServiceManager)
        collector_mgr.verify_client(options, secret_data, schema)

    @transaction
    @check_required(['options', 'secret_data', 'filter'])
    def collect(self, params):
        """ Collect external data

        Args:
            params (dict): {
                'options': 'dict',
                'schema': 'str',
                'secret_data': 'dict',
                'domain_id': 'str'
            }

        Returns:
            generator of resource_data (dict)
        """

        options = params['options']
        secret_data = params['secret_data']
        schema = params.get('schema')

        collector_mgr: MyServiceManager = self.locator.get_manager(MyServiceManager)
        iterator: Generator = collector_mgr.collect(options, secret_data, schema)

        for resource_data in iterator:
            yield resource_data
