from django.test import TestCase, Client
from django.urls import reverse
from main_app.models import Event, Comment
import json


class TestViews(TestCase):
    """def test_home_GET(self):
    client = Client()
    response = client.get(reverse("home"))
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, "home.html")"""

    """ def test_events_index_GET(self):
        client = Client()
        response = client.get(reverse("index"))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, "events/index.html") """

    """ def test_events_details_GET(self):
        client = Client()
        response = client.get(reverse("detail", args=[7]))
        self.assertEquals(response.status_code, 302) """

    """ def test_events_details_GET(self):
        w = self.create_whatever()
        resp = self.client.get(reverse("detail", args=[7]))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content) """
