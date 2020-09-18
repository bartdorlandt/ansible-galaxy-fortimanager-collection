#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_system_admin_profile_datamaskcustomfields
short_description: Customized datamask fields.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded

options:
    bypass_validation:
        description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters
        required: false
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root
        required: false
        type: str
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: false
        type: int
        default: 300
    state:
        description: the directive to create, update or delete an object
        type: str
        required: true
        choices:
          - present
          - absent
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    profile:
        description: the parameter (profile) in requested url
        type: str
        required: true
    system_admin_profile_datamaskcustomfields:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            field-category:
                description: no description
                type: list
                choices:
                 - log
                 - fortiview
                 - alert
                 - ueba
                 - all
            field-name:
                type: str
                description: 'Field name.'
            field-status:
                type: str
                default: 'enable'
                description:
                 - 'Field status.'
                 - 'disable - Disable field.'
                 - 'enable - Enable field.'
                choices:
                    - 'disable'
                    - 'enable'
            field-type:
                type: str
                default: 'string'
                description:
                 - 'Field type.'
                 - 'string - String.'
                 - 'ip - IP.'
                 - 'mac - MAC address.'
                 - 'email - Email address.'
                 - 'unknown - Unknown.'
                choices:
                    - 'string'
                    - 'ip'
                    - 'mac'
                    - 'email'
                    - 'unknown'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Customized datamask fields.
      fmgr_system_admin_profile_datamaskcustomfields:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         profile: <your own value>
         state: <value in [present, absent]>
         system_admin_profile_datamaskcustomfields:
            field-category:
              - log
              - fortiview
              - alert
              - ueba
              - all
            field-name: <value of string>
            field-status: <value in [disable, enable]>
            field-type: <value in [string, ip, mac, ...]>

'''

RETURN = '''
request_url:
    description: The full url requested
    returned: always
    type: str
    sample: /sys/login/user
response_code:
    description: The status of api request
    returned: always
    type: int
    sample: 0
response_message:
    description: The descriptive message of the api response
    type: str
    returned: always
    sample: OK.

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import check_parameter_bypass


def main():
    jrpc_urls = [
        '/cli/global/system/admin/profile/{profile}/datamask-custom-fields'
    ]

    perobject_jrpc_urls = [
        '/cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-custom-fields}'
    ]

    url_params = ['profile']
    module_primary_key = 'field-name'
    module_arg_spec = {
        'bypass_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'profile': {
            'required': True,
            'type': 'str'
        },
        'system_admin_profile_datamaskcustomfields': {
            'required': False,
            'type': 'dict',
            'options': {
                'field-category': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'log',
                        'fortiview',
                        'alert',
                        'ueba',
                        'all'
                    ]
                },
                'field-name': {
                    'required': True,
                    'type': 'str'
                },
                'field-status': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'default': 'enable',
                    'type': 'str'
                },
                'field-type': {
                    'required': False,
                    'choices': [
                        'string',
                        'ip',
                        'mac',
                        'email',
                        'unknown'
                    ],
                    'default': 'string',
                    'type': 'str'
                }
            }

        }
    }

    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_admin_profile_datamaskcustomfields'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.process_curd()
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()