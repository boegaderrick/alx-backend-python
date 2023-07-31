#!/usr/bin/env python3
"""This module contains tests for contents of the client module"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrgClient test class"""
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org, get_json_mock):
        """This module tests the org method"""
        get_json_mock.return_value = {'json': 'test'}
        client = GithubOrgClient(org)
        self.assertEqual(client.org, {'json': 'test'})

    def test_public_repos_url(self):
        """Tests '_public_repos_url' property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as org_mock:
            org_mock.return_value = {'repos_url': 'test value'}
            client = GithubOrgClient('test')
            self.assertEqual(client._public_repos_url, 'test value')

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """Tests the public_repos method"""
        get_json_mock.return_value = [
            {'name': 'hello'},
            {'name': 'json'},
            {'name': 'test'}
        ]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as prop_mock:
            prop_mock.return_value = 'test string'
            client = GithubOrgClient('test')
            self.assertEqual(client.public_repos(), ['hello', 'json', 'test'])
            self.assertTrue(get_json_mock.assert_called_once)
            self.assertTrue(prop_mock.assert_called_once)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """Tests has_license method"""
        client = GithubOrgClient('test')
        self.assertEqual(client.has_license(repo, license), expected)
