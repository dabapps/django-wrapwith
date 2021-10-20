django-wrapwith
===============

**A Django template tag for wrapping a template block in a reusable enclosing template.**

Provides a block tag called `wrapwith` which behaves exactly like [the built-in `include` tag](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#include), but injects the contents of the block into the included template.

It is intended to make wrapper markup reusable, encouraging you to break your template into "components" which might have a particular enclosing structure but varying contents. It is particularly useful with design systems that provide components (cards, blockquotes, accordians etc) that have reusable structure but arbitrary content.

A toy example: imagine your design includes a box component which has a coloured border, but can contain any other markup inside it.

First, create a wrapper template, `wrappers/box.html`:

```html
<div style="border: 1px solid {{ bordercol }}">
  {{ wrapped }}
</div>
```

Note the special `{{ wrapped }}` variable, which will be replaced with your wrapped content.

Then, in your main page template:

```html
{% load wrapwith %}

<html>
  <body>
    <h1>welcome to my page</h1>

    {% wrapwith "wrappers/box.html" with bordercol="red" %}
      <p>this is inside a red box</p>
    {% endwrapwith %}

    {% wrapwith "wrappers/box.html" with bordercol="green" %}
      <p>this is inside a green box</p>
      <p>and here's another paragraph inside the green box</p>
    {% endwrapwith %}
  </body>
</html>
```

### Optional: aliasing templates

If you find writing out the full template path every time you use a component too verbose, you can define a dictionary of "aliases" in your Django settings, using the setting name `WRAPWITH_TEMPLATES`. This dictionary can be nested. You can then use a dotted path into this dictionary in your templates.

In your `settings.py`:

```python
WRAPWITH_TEMPLATES = {
  "wrappers": {
    "box": "wrappers/box.html",
  },
}
```

In your template:

```html
{% wrapwith wrappers.box with bordercol="red" %}
  <p>this is inside a red box</p>
{% endwrapwith %}
```

Tested on Python 3 with all currently supported Django versions.

## Installation

    pip install django-wrapwith

Then add `wrapwith` to your `INSTALLED_APPS`.

## Code of conduct

For guidelines regarding the code of conduct when contributing to this repository please review https://www.dabapps.com/open-source/code-of-conduct/
