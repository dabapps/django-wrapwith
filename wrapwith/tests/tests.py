from django.template.loader import render_to_string
from django.test import TestCase


class WrapWithTestCase(TestCase):
    def test_simple_wrapper(self):
        rendered = render_to_string("simple.html")
        self.assertHTMLEqual(rendered, "<div>hello!</div>")

    def test_arguments(self):
        rendered = render_to_string("arguments.html")
        self.assertHTMLEqual(rendered, "<div class='arg'>hello!</div>")

    def test_only(self):
        rendered = render_to_string("only.html")
        self.assertHTMLEqual(rendered, "<div class='arg'>hello!</div>")
