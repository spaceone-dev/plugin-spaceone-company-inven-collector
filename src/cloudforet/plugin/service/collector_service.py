import logging
import itertools
from typing import Generator

from spaceone.core.service import *
from cloudforet.plugin.lib.manager.collector_manager import CollectorManager
from cloudforet.plugin.conf.application_conf import SERVICE_GROUP_MAP

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

        collector_mgr: CollectorManager = self.locator.get_manager(CollectorManager)
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

        execute_managers = self._get_execute_manger(options)
        for execute_manager in execute_managers:
            collector_mgr = self.locator.get_manager(execute_manager)
            collector_mgr.verify_client(options, secret_data, schema)

    @transaction
    @check_required(['options', 'secret_data'])
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

        execute_managers = self._get_execute_manger(options)
        for execute_manager in execute_managers:
            collector_mgr = self.locator.get_manager(execute_manager)
            yield from collector_mgr.collect(options, secret_data, schema)

    def _get_execute_manger(self, options):
        if 'cloud_service_types' in options:
            execute_managers = self._match_execute_manager(options['cloud_service_types'])
        else:
            execute_managers = SERVICE_GROUP_MAP.values()

        return list(itertools.chain(*execute_managers))

    @staticmethod
    def _match_execute_manager(service_groups):
        return [SERVICE_GROUP_MAP[service_group] for service_group in service_groups
                if service_group in SERVICE_GROUP_MAP]
