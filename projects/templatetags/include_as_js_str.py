# templatetags/include_as_js_str.py
from django import template
from django.template.loader_tags import do_include
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


def _escape_html_for_js(value):
  return mark_safe(force_text(value).lstrip()
                   .replace('\\', '\\\\').replace('</', '<\/').replace('"', '\\"').replace("'", "\\'")
                   .replace('\r\n', '\\n').replace('\n', '\\n').replace('\r', '\\n'))


class IncludeAsJsStrNode(template.Node):

    def __init__(self, include_node):
        self.include_node = include_node

    def render(self, context):
        return _escape_html_for_js(self.include_node.render(context))


@register.tag('include_as_js_str')
def do_include_as_js_str(parser, token):
    return IncludeAsJsStrNode(do_include(parser, token))
