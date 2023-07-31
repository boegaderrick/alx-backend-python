#!/usr/bin/env python3
"""This module contains a test class"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """Test class definition"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests the return value of 'access_nested_map' function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, msg):
        """Tests if 'access_nested_map' raises an exception when necessary"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(msg, error.exception.__str__().strip("'"))


class TestGetJson(unittest.TestCase):
    """'utils.get_json' test class definition"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, requests_mock):
        """This method tests the 'utils.get_json' function"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        requests_mock.get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
        self.assertEqual(requests_mock.get.call_count, 1)
