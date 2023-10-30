import logging
import datetime

from cloudforet.plugin.lib.manager.collector_manager import CollectorManager
from cloudforet.plugin.model.design_member_model import CloudServiceType
from cloudforet.plugin.connector.development_member_connector import DevelopmentMemberConnector

_LOGGER = logging.getLogger(__name__)


class DevelopmentMemberManager(CollectorManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dev_connector: DevelopmentMemberConnector = self.locator.get_connector(DevelopmentMemberConnector)
        self.provider = 'spaceone_company'
        self.cloud_service_group = 'Development'
        self.cloud_service_type = 'Member'

    def verify_client(self, options: dict, secret_data: dict, schema: str = None) -> None:
        self.dev_connector.verify_client(options, secret_data, schema)

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

            # Collect Cloud Services (Development members)
            department_name = 'development'
            dev_members = self.dev_connector.list_members(department_name)

            for member_result in self._make_member_result(dev_members):
                yield self.make_response(
                    member_result,
                    {'1': ['reference.resource_id', 'provider', 'cloud_service_type', 'cloud_service_group', 'account']}
                )

        except Exception as e:
            yield self.error_response(e)

    def _make_member_result(self, team_members):
        results = []
        dev_members = team_members.get('members', [])

        for dev_member in dev_members:
            dev_member['department'] = team_members.get('department_name', 'Unknown')

            member_result = {
                'name': dev_member['name'],
                'reference': {
                    'resource_id': dev_member['id']
                },
                'data': dev_member,
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
                'account': dev_member['department'],
                'provider': self.provider,
                'cloud_service_group': self.cloud_service_group,
                'cloud_service_type': self.cloud_service_type,
                'region_code': 'global'
            }

            results.append(member_result)

        return results

    @staticmethod
    def _generate_duration(join_date):
        today = datetime.datetime.now()
        join_date = datetime.datetime.strptime(join_date, '%Y-%m-%d')
        duration = today - join_date
        return duration.days
