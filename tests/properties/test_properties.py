import unittest

from configparser import NoSectionError, NoOptionError
from lib.properties import Properties


class PropertiesTests(unittest.TestCase):

    def test_properties_getvalues(self):
        """
        Test is passed when values are retrieved successfully from Properties()
        """
        prop = Properties('./tests/properties/test_properties.ini')
        host = prop.config.get('section_a', 'host')
        port = prop.config.get('section_a', 'port')
        self.assertEqual(host, 'localhost')
        self.assertEqual(port, "8080")  # INI always return values as strings

    def test_properties_nosectionerror(self):
        """
        Test is passed when a NoSectionError is raised because of referencing a non-existing section
        """
        with self.assertRaises(NoSectionError) as e:
            prop = Properties('./tests/properties/test_properties.ini')
            host = prop.config.get('section_b', 'host')

    def test_properties_nooptionerror(self):
        """
        Test is passed when a NoOptionError is raised because of referencing a non-existing option
        """
        with self.assertRaises(NoOptionError) as e:
            prop = Properties('./tests/properties/test_properties.ini')
            host = prop.config.get('section_a', 'hostx')

    def test_properties_webapp_nosection(self):
        """
        Test is passed when Properties().webapp() returns None because expected section was not found
        """
        prop = Properties('./tests/properties/test_properties.py.ini').webapp()
        self.assertEqual(prop, None)

    def test_properties_webapp_nooption(self):
        """
        Test is passed when Properties().webapp() returns None because expected option was not found
        """
        prop = Properties('./tests/properties/test_webapp_nooption.ini').webapp()
        self.assertEqual(prop, None)

    def test_properties_webapp_expected(self):
        """
        Test is passed when Properties().webapp() returns expected values
        """
        prop = Properties('./tests/properties/test_webapp_expected.ini').webapp()
        self.assertEqual(prop['host'], 'localhost')
        self.assertEqual(prop['port'], '8080')


if __name__ == '__main__':
    unittest.main()