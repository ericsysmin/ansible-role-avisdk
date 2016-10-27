#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: not supported
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from ansible.module_utils.basic import AnsibleModule
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields, avi_ansible_api)

EXAMPLES = """
- code: 'avi_seproperties controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_seproperties'
description: "Adds/Deletes SeProperties configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_seproperties
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: SeProperties Configuration
description:
    - This module is used to configure SeProperties object
    - more examples at <https://github.com/avinetworks/avi-ansible-samples>
requirements: [ avisdk ]
version_added: 2.1.2
options:
    controller:
        description:
            - location of the controller
        required: true
    username:
        description:
            - username to access the Avi
        required: true
    password:
        description:
            - password of the Avi user
        required: true
    tenant:
        description:
            - tenant for the operations
        default: admin
    tenant_uuid:
        description:
            - tenant uuid for the operations
        default: ''
    state:
        description:
            - The state that should be applied on the entity.
        required: false
        default: present
        choices: ["absent","present"]
    se_agent_properties:
        description:
            - Not present.
        type: SeAgentProperties
    se_bootup_properties:
        description:
            - Not present.
        type: SeBootupProperties
    se_runtime_properties:
        description:
            - Not present.
        type: SeRuntimeProperties
    url:
        description:
            - url
        required: true
        type: string
    uuid:
        description:
            - Not present.
        default: default
        type: string
'''

RETURN = '''
obj:
    description: SeProperties (api/seproperties) object
    returned: success, changed
    type: dict
'''


def main():
    try:
        module = AnsibleModule(
            argument_spec=dict(
                controller=dict(required=True),
                username=dict(required=True),
                password=dict(required=True),
                tenant=dict(default='admin'),
                tenant_uuid=dict(default=''),
                state=dict(default='present',
                           choices=['absent', 'present']),
                se_agent_properties=dict(
                    type='dict',
                    ),
                se_bootup_properties=dict(
                    type='dict',
                    ),
                se_runtime_properties=dict(
                    type='dict',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'seproperties',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()