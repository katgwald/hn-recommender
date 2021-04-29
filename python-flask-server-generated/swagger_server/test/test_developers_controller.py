# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.article import Article  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_suggest_articles(self):
        """Test case for suggest_articles

        returns suggested articles from list
        """
        response = self.client.open(
            '/teamkat/hnpredictor/1.0.0/articles',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
