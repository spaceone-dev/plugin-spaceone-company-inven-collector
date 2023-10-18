from pydantic import BaseModel
from cloudforet.plugin.lib.model.plugin_info_model import ResourceType


class ResourceInfo(BaseModel):
    message: str = None
    resource_type: ResourceType
    match_rules: dict = None
    resource: dict = None
