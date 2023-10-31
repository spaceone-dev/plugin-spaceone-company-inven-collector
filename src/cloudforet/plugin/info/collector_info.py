from spaceone.core import utils
from spaceone.api.inventory.plugin import collector_pb2
from spaceone.core.pygrpc.message_type import *

__all__ = ['PluginInfo', 'ResourceInfo']


def PluginInfo(plugin_data):
    info = {
        'metadata': change_struct_type(plugin_data['metadata']),
    }

    return collector_pb2.PluginInfo(**info)


def ResourceInfo(resource_data):
    info = {
        'state': resource_data['state'],
        'message': resource_data.get('message', ''),
        'resource_type': resource_data['resource_type'],
        'match_rules': change_struct_type(resource_data.get('match_rules')),
        'resource': change_struct_type(resource_data.get('resource'))
    }

    return collector_pb2.ResourceInfo(**info)
