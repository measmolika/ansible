# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from units.compat import unittest

from ansible.config.data import ConfigData
from ansible.config.manager import Setting


mykey = Setting('mykey', 'myvalue', 'test', 'string')
mykey2 = Setting('mykey2', 'myvalue2', ['test', 'test2'], 'list')
mykey3 = Setting('mykey3', 'myvalue3', 11111111111, 'integer')
server_conf_id = Setting('server_conf_id','conf_id', 'staging', 'string')
server_conf_id1 = Setting('server_conf_id1','conf_id1', 'testing', 'string')

class TestConfigData(unittest.TestCase):

    def setUp(self):
        self.cdata = ConfigData()

    def tearDown(self):
        self.cdata = None

    def test_update_setting(self):
        for setting in [mykey, mykey2, mykey3]:
            self.cdata.update_setting(setting)
            self.assertEqual(setting, self.cdata._global_settings.get(setting.name))

    def test_update_setting_with_plugin(self):
        pass

    def test_get_setting(self):
        self.cdata._global_settings = {'mykey': mykey}
        self.assertEqual(mykey, self.cdata.get_setting('mykey'))

    def test_get_settings(self):
        all_settings = {'mykey': mykey, 'mykey2': mykey2}
        self.cdata._global_settings = all_settings

        for setting in self.cdata.get_settings():
            self.assertEqual(all_settings[setting.name], setting)

    def test_update_conf_setting(self):
        for setting in [server_conf_id, server_conf_id]:
            self.cdata.update_conf_setting(setting)
            self.assertEqual(setting, self.cdata._global_settings.get(setting.name))

    def test_get_conf_setting(self):
        self.cdata._global_settings = {'server_conf_id': server_conf_id}
        self.assertEqual(server_conf_id, self.cdata.get_conf_setting('server_conf_id'))
