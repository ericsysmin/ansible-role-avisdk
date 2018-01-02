#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_errorpageprofile
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of ErrorPageProfile Avi RESTful Object
description:
    - This module is used to configure ErrorPageProfile object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete"]
    app_name:
        description:
            - Name of the virtual service which generated the error page.
            - Field introduced in 17.2.4.
            - Default value when not specified in API or module is interpreted by Avi Controller as VS Name.
    company_name:
        description:
            - Name of the company to show in error page.
            - Field introduced in 17.2.4.
            - Default value when not specified in API or module is interpreted by Avi Controller as Avi Networks.
    error_pages:
        description:
            - Defined error pages for http status codes.
            - Field introduced in 17.2.4.
    host_name:
        description:
            - Fully qualified domain name for which the error page is generated.
            - Field introduced in 17.2.4.
            - Default value when not specified in API or module is interpreted by Avi Controller as Host Header.
    name:
        description:
            - Field introduced in 17.2.4.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 17.2.4.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Field introduced in 17.2.4.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create ErrorPageProfile object
  avi_errorpageprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_errorpageprofile
"""

RETURN = '''
obj:
    description: ErrorPageProfile (api/errorpageprofile) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from pkg_resources import parse_version
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or (sdk_version and
            (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    from avi.sdk.utils.ansible_utils import avi_ansible_api
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        app_name=dict(type='str',),
        company_name=dict(type='str',),
        error_pages=dict(type='list',),
        host_name=dict(type='str',),
        name=dict(type='str',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'errorpageprofile',
                           set([]))

if __name__ == '__main__':
    main()