# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  

    OpenAPI spec version: 1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import
import os
import sys
sys.path.append(os.environ["SWAGGER_CLIENT_PATH"])


import unittest
import testutils

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.user_group import UserGroup  
from swagger_client.models.configurations import Configurations 
from pprint import pprint

#Testcase
#12-01-LDAP-usergroup-add
#12-02-LDAP-usergroup-update
#12-03-LDAP-usergroup-delete

class TestUserGroup(unittest.TestCase):
    """UserGroup unit test stubs"""
    product_api = testutils.GetProductApi("admin", "Harbor12345")
    groupId = 0
    def setUp(self):
        result = self.product_api.configurations_put(configurations=Configurations(ldap_group_attribute_name="cn", ldap_group_base_dn="ou=groups,dc=example,dc=com", ldap_group_search_filter="objectclass=groupOfNames", ldap_group_search_scope=2))
        pprint(result)        
        pass

    def tearDown(self):
        if self.groupId > 0 :
            self.product_api.usergroups_group_id_delete(group_id=self.groupId)
        pass

    def testAddUpdateUserGroup(self):
        """Test UserGroup"""
        user_group = UserGroup(group_name="harbor_group123", group_type=1, ldap_group_dn="cn=harbor_group,ou=groups,dc=example,dc=com")
        result = self.product_api.usergroups_post(usergroup=user_group)
        pprint(result)
        
        user_groups = self.product_api.usergroups_get()
        found = False
        
        for ug in user_groups :
            if ug.group_name == "harbor_group123" :
                found = True
                print("Found usergroup")
                pprint(ug)
                self.groupId = ug.id
        self.assertTrue(found)

        result = self.product_api.usergroups_group_id_put(self.groupId, usergroup = UserGroup(group_name = "newharbor_group"))

        new_user_group = self.product_api.usergroups_group_id_get(group_id=self.groupId)
        self.assertEqual("newharbor_group", new_user_group.group_name)

        pass


if __name__ == '__main__':
    unittest.main()
