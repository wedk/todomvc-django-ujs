from django.shortcuts import render


def render_for(template_dir, extension='.html', content_type=None):
    """render method factory"""

    def _render(request, template_name, *args, **kwargs):
        kwargs.setdefault('content_type', content_type)
        template_name = template_dir + '/' + template_name + extension
        return render(request, template_name, *args, **kwargs)

    return _render
