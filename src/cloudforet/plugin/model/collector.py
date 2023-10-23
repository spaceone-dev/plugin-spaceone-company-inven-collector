from cloudforet.plugin.lib.model.plugin_info_model import PluginInfo, PluginMetadata, ResourceType, ScheduleType, \
    Feature


class CollectorPluginInfo(PluginInfo):
    metadata: PluginMetadata = {
        'supported_resource_type': [
            ResourceType.cloud_service,
            ResourceType.cloud_service_type
        ],
        'supported_schedules': [
            ScheduleType.hours
        ],
        'supported_features': [
            Feature.garbage_collection
        ],
        'filter_format': [],
        'options_schema': {
            'required': ['regions'],
            'order': ['regions'],
            'type': 'object',
            'properties': {
                'regions': {
                    'title': 'Region Filter',
                    'type': 'array',
                    'items': {
                        'enum': [
                            'ap-northeast-1',
                            'ap-northeast-2'
                        ]
                    }
                }
            }
        }
    }
