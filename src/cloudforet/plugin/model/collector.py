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
        'filter_format': []
    }
