from typing import List
from cloudforet.plugin.lib.model.cloud_service_type_model import BaseCloudServiceType

_METADATA = {
    'view': {
        'search': [
            {
                'key': 'data.id',
                'name': 'Member ID'
            },
            {
                'key': 'data.part',
                'name': 'Part',
            },
            {
                'key': 'data.email',
                'name': 'Email'
            },
            {
                'key': 'data.join_date',
                'name': 'Join Date'
            }
        ],
        'table': {
            'layout': {
                'name': '',
                'type': 'query-search-table',
                'options': {
                    'default_sort': {
                        'key': 'data.id',
                        'desc': False
                    },
                    'fields': [
                        {
                            'type': 'text',
                            'key': 'data.id',
                            'name': 'Member ID'
                        },
                        {
                            'type': 'text',
                            'key': 'data.part',
                            'name': 'Part',
                        },
                        {
                            'type': 'text',
                            'key': 'data.email',
                            'name': 'Email',
                        },
                        {
                            'type': 'text',
                            'key': 'data.join_date',
                            'name': 'Join Date',
                        }
                    ]
                }
            }
        },
        'widget': [

        ],
        "sub_data": {
            "layouts": [
                {
                    "name": "Details",
                    "type": "list",
                    "options": {
                        "layouts": [
                            {
                                "options": {
                                    "fields": [
                                        {
                                            'key': 'data.id',
                                            'name': 'Member ID'
                                        },
                                        {
                                            'key': 'data.part',
                                            'name': 'Part',
                                        }
                                    ]
                                },
                                "name": "Division",
                                "type": "item"
                            },
                            {
                                "options": {
                                    "fields": [
                                        {
                                            'key': 'data.email',
                                            'name': 'Email'
                                        },
                                        {
                                            'key': 'data.join_date',
                                            'name': 'Join Date'
                                        }
                                    ]
                                },
                                "name": "Private",
                                "type": "item"
                            }
                        ]
                    }
                }
            ]
        }
    }
}


class CloudServiceType(BaseCloudServiceType):
    group: str = 'Design'
    is_primary: bool = True
    is_major: bool = True
    metadata: dict = _METADATA
    labels: List[str] = ['Application Integration', 'Management']
    tags: dict = {
        'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/spaceone.svg'
    }
