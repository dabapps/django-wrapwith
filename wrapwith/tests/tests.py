from django.template.loader import render_to_string
from django.test import TestCase


class WrapWithTestCase(TestCase):
    def test_simple_wrapper(self):
        rendered = render_to_string("simple.html")
        self.assertHTMLEqual(rendered, "<div>hello!</div>")
