#!/usr/bin/env python3
"""This module contains tests for contents of the client module"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrgClient test class"""
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org, get_json_mock):
        """This module tests the org method"""
        get_json_mock.return_value = {'json': 'test'}
        client = GithubOrgClient(org)
        self.assertEqual(client.org, {'json': 'test'})
