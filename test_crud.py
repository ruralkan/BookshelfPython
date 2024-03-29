
import re

from conftest import flaky_filter
from flaky import flaky
import pytest


# Mark all test cases in this class as flaky, so that if errors occur they
# can be retried. This is useful when databases are temporarily unavailable.
@flaky(rerun_filter=flaky_filter)
# Tell pytest to use both the app and model fixtures for all test cases.
# This ensures that configuration is properly applied and that all database
# resources created during tests are cleaned up. These fixtures are defined
# in conftest.py
@pytest.mark.usefixtures('app', 'model')
class TestCrudActions(object):

    def test_list(self, app, model):
        for i in range(1, 12):
            model.create({'title': u'Book {0}'.format(i)})

        with app.test_client() as c:
            rv = c.get('/books')

        assert rv.status == '200 OK'

    def test_add(self, app):
        data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'genre': 'Test Genre',
            'description': 'Test Description',
            'read': False
        }

        with app.test_client() as c:
            rv = c.post('/books', data=data, follow_redirects=True)

        assert rv.status == '200 OK'
        body = rv.data.decode('utf-8')
        assert 'Test Book' in body
        assert 'Test Author' in body
        assert 'Test Genre' in body
        assert 'Test Description' in body

    def test_edit(self, app, model):
        existing = model.create({'title': "Temp Title"})

        with app.test_client() as c:
            rv = c.post(
                '/books/%s' % existing['id'],
                data={'title': 'Updated Title'},
                follow_redirects=True)

        assert rv.status == '200 OK'
        body = rv.data.decode('utf-8')
        assert 'Updated Title' in body
        assert 'Temp Title' not in body

    def test_delete(self, app, model):
        existing = model.create({'title': "Temp Title"})

        with app.test_client() as c:
            rv = c.get(
                '/books/%s' % existing['id'],
                follow_redirects=True)

        assert rv.status == '200 OK'
        assert not model.read(existing['id'])