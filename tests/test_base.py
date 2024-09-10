from flask_testing import TestCase
from flask import current_app, url_for
from app import create_app

class MainTest(TestCase):
    def create_app(self):
        create_app.config['TESTING'] = True
        create_app.config['WTF_CSRF_ENABLED'] = False

        return create_app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.location, '/hello')

    def test_hello_get(self):
        response = self.client.get(url_for ('hello'))

        self.assert200(response)

    def text_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-pwsd'
        }
        response = self.client.post(url_for('index'), data=fake_form)
        self.assertEqual(response.location, '/hello')