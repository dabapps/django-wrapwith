from django.conf import settings
from django.template import Library
from django.template.loader_tags import do_include

register = Library()

"""
The {% wrapwith %} template tag is exactly like {% include %}, but it's a block tag. The
rendered contents of the block up to {% endwrapwith %} are injected into the included
template as a variable called {{ wrapped }}.

This code is structured to reuse the built-in {% include %} tag implementation as much
as possible, to avoid copy-pasting duplicated code.
"""


class RenderNodelistVariable:
    """
    Quacks like a template.Variable, but wraps a nodelist which is rendered when the
    variable is resolved. Used to inject the rendered nodelist into the
    included wrapper template.
    """

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def resolve(self, context):
        return self.nodelist.render(context)


class ResolveWithAliases:
    """
    Wraps a FilterExpression and injects the WRAPWITH_TEMPLATES alias
    dictionary into its context before resolving the variable name.
    """

    def __init__(self, template):
        self.template = template
        self.aliases = getattr(settings, "WRAPWITH_TEMPLATES", {})

    def resolve(self, context):
        with context.push(self.aliases):
            return self.template.resolve(context)


@register.tag(name="wrapwith")
def do_wrapwith(parser, token):
    """
    Calls the do_include function, but injects the contents of the block into
    the extra_context of the included template.
    """
    include_node = do_include(parser, token)
    nodelist = parser.parse(("endwrapwith",))
    parser.delete_first_token()
    include_node.template = ResolveWithAliases(include_node.template)
    include_node.extra_context["wrapped"] = RenderNodelistVariable(nodelist)
    return include_node
