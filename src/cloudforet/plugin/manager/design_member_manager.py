import logging
import datetime

from cloudforet.plugin.lib.manager.collector_manager import CollectorManager
from cloudforet.plugin.model.design_member_model import CloudServiceType
from cloudforet.plugin.connector.design_member_connector import DesignMemberConnector

_LOGGER = logging.getLogger(__name__)


class DesignMemberManager(CollectorManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.design_connector: DesignMemberConnector = self.locator.get_connector(DesignMemberConnector)
        self.provider = 'spaceone_company'
        self.cloud_service_group = 'Design'
        self.cloud_service_type = 'Member'

    def verify_client(self, options: dict, secret_data: dict, schema: str = None) -> None:
        self.design_connector.verify_client(options, secret_data, schema)

    def collect(self, options, secret_data, schema):

        try:
            # Collect Cloud Service Type
            cloud_service_type = CloudServiceType(group=self.cloud_service_group, name=self.cloud_service_type,
                                                  provider=self.provider)
            yield self.make_response(
                cloud_service_type.dict(),
                {'1': ['name', 'group', 'provider']},
                resource_type='inventory.CloudServiceType'
            )

            # Collect Cloud Services (Design members)
            department_name = 'design'
            design_members = self.design_connector.list_members(department_name)

            for member_result in self._make_member_result(design_members):
                yield self.make_response(
                    member_result,
                    {'1': ['reference.resource_id', 'provider', 'cloud_service_type', 'cloud_service_group', 'account']}
                )

        except Exception as e:
            yield self.error_response(e)

    def _make_member_result(self, team_members):
        results = []
        design_members = team_members.get('members', [])

        for design_member in design_members:
            design_member['department'] = team_members.get('department_name', 'Unknown')

            member_result = {
                'name': design_member['name'],
                'reference': {
                    'resource_id': design_member['id']
                },
                'data': design_member,
                'metadata': {
                    'view': {
                        'sub_data': {
                            'reference': {
                                'resource_type': 'inventory.CloudServiceType',
                                'options': {
                                    'provider': self.provider,
                                    'cloud_service_group': self.cloud_service_group,
                                    'cloud_service_type': self.cloud_service_type,
                                }
                            }
                        }
                    }
                },
                'account': design_member['department'],
                'provider': self.provider,
                'cloud_service_group': self.cloud_service_group,
                'cloud_service_type': self.cloud_service_type,
                'region_code': 'global'
            }

            results.append(member_result)

        return results
