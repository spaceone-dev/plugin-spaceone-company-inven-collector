from enum import Enum
from pydantic import BaseModel
from cloudforet.plugin.lib.model.plugin_info_model import ResourceType


class State(str, Enum):
    success = 'SUCCESS'
    failre = 'FAILURE'


class ResourceInfo(BaseModel):
    state: State
    message: str = None
    resource_type: ResourceType
    match_rules: dict = None
    resource: dict = None
