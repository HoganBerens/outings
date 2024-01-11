from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main_app.views import (
    home,
    signup,
    events_index,
    EventCreate,
    EventUpdate,
    EventDelete,
    events_detail,
    add_comment,
    my_events,
    edit_comment,
    delete_comment,
)


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home)

    def test_accounts_signup_url_resolves(self):
        url = reverse("signup")
        self.assertEquals(resolve(url).func, signup)

    def test_events_index_url_resolves(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, events_index)

    def test_events_create_url_resolves(self):
        url = reverse("events_create")
        self.assertEquals(resolve(url).func.view_class, EventCreate)

    def test_events_update_url_resolves(self):
        url = reverse("events_update", args=[7])
        self.assertEquals(resolve(url).func.view_class, EventUpdate)

    def test_events_delete_url_resolves(self):
        url = reverse("events_delete", args=[7])
        self.assertEquals(resolve(url).func.view_class, EventDelete)

    def test_events_detail_url_resolves(self):
        url = reverse("detail", args=[7])
        self.assertEquals(resolve(url).func, events_detail)

    def test_events_add_comment_url_resolves(self):
        url = reverse("add_comment", args=[7])
        self.assertEquals(resolve(url).func, add_comment)

    def test_events_myevents_url_resolves(self):
        url = reverse("my_events")
        self.assertEquals(resolve(url).func, my_events)

    def test_events_edit_comment_url_resolves(self):
        url = reverse("edit_comment", args=[7, 7])
        self.assertEquals(resolve(url).func, edit_comment)

    def test_events_delete_comment_url_resolves(self):
        url = reverse("delete_comment", args=[7, 7])
        self.assertEquals(resolve(url).func, delete_comment)
