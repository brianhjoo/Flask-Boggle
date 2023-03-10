from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""  #TODO: Ask about session

        with self.client as client:
            response = client.get('/')


            # test that you're getting a template
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<!-- Test: Main Boggle Page -->', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            ...
            # Test that: the route returns JSON with a string game id, and a list-of-lists for the board
            # The route stores the new game in games dict.

            response = client.post('/api/new-game')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertIn("game_id", data)
            self.assertIn("board", data)
            self.assertIn(data['game_id'], games)





