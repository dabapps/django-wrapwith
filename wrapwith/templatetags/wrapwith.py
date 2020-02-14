from django.template import Library
from django.template.base import token_kwargs
from django.template.loader_tags import construct_relative_path, do_include, IncludeNode

register = Library()

"""
The {% wrapwith %} template tag is exactly like {% include %}, but it's a block tag. The
rendered contents of the block up to {% endwrapwith %} are injected into the included
template as a variable called {{ wrapped }}.

This code is structured to reuse the built-in {% include %} tag implementation as much
as possible, to avoid copy-pasting duplicated code.
"""


class PassThroughVariable:
    """
    Quacks like a template.Variable, but just passes through its wrapped
    value when resolved. Used to inject the rendered nodelist into the
    included wrapper template
    """

    def __init__(self, var):
        self.var = var

    def resolve(self, context):
        return self.var


class WrapWithNode(IncludeNode):
    """
    Subclass of the node used by {% include %} which just injects the rendered
    contents of the block into the included template's context as {{ wrapped }}.
    """

    context_key = "__wrapwith_context"

    def __init__(self, template, nodelist, *args, **kwargs):
        self.nodelist = nodelist
        super().__init__(template, *args, **kwargs)

    def render(self, context):
        self.extra_context["wrapped"] = PassThroughVariable(
            self.nodelist.render(context)
        )
        return super().render(context)


@register.tag(name="wrapwith")
def do_wrapwith(parser, token):
    """
    Calls the do_include function, and converts the returned IncludeNode into
    a WrapWithNode, passing in the nodelist inside the block.
    """
    include_node = do_include(parser, token)
    nodelist = parser.parse(("endwrapwith",))
    parser.delete_first_token()
    return WrapWithNode(
        include_node.template,
        nodelist,
        extra_context=include_node.extra_context,
        isolated_context=include_node.isolated_context,
    )
