# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.article import Article  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_add_article(self):
        """Test case for add_article

        adds a chosen article
        """
        article = Article()
        response = self.client.open(
            '/teamkat/hnpredictor/1.0.0/articles',
            method='POST',
            data=json.dumps(article),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
