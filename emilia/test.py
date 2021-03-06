from django.test import TestCase
from django.core.urlresolvers import reverse


class TestHomePage(TestCase):
    def test_uses_index_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "emilia/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")


class TestLoginPage(TestCase):
    def test_uses_login_template(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "emilia/login.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "base.html")
