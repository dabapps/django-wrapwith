from django.template.loader import render_to_string
from django.test import override_settings, TestCase


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

    def test_nested(self):
        rendered = render_to_string("nested.html")
        self.assertHTMLEqual(
            rendered,
            """
            something before
            <div class="outer">
                hello!
                <div class="inner1">
                    inner1
                </div>
                <div class="inner2">
                    inner2
                </div>
            </div>
            something after
        """,
        )

    @override_settings(WRAPWITH_TEMPLATES={"div": "wrappers/div.html"})
    def test_alias(self):
        rendered = render_to_string("alias.html")
        self.assertHTMLEqual(rendered, "<div>hello!</div>")

    @override_settings(WRAPWITH_TEMPLATES={"a": {"b": {"c": "wrappers/div.html"}}})
    def test_dotted_alias(self):
        rendered = render_to_string("alias_with_dots.html")
        self.assertHTMLEqual(rendered, "<div>hello!</div>")
