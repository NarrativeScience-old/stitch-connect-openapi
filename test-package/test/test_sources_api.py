# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.sources_api import SourcesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSourcesApi(unittest.TestCase):
    """SourcesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.sources_api.SourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_get_sources(self):
        """Test case for api_get_sources

        Lists the sources for an account, including active, paused, and deleted sources.   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
