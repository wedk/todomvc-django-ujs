# middlewares.py
from django.http import QueryDict


class MethodOverrideMiddleware(object):
    """Override POST HTTP method to seemlessly support PUT and DELETE verbs.
    cf. https://github.com/rack/rack/blob/master/lib/rack/method_override.rb
    """

    ALLOWED_METHOD              = 'POST'
    HTTP_METHODS                = ['PUT', 'DELETE']
    METHOD_OVERRIDE_PARAM_KEY   = '_method'
    HTTP_METHOD_OVERRIDE_HEADER = 'HTTP_X_HTTP_METHOD_OVERRIDE'

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == self.ALLOWED_METHOD:
            method = self._method_override(request)

            if method in self.HTTP_METHODS:
                request.method = method
                request.META['REQUEST_METHOD'] = method

        return None

    def _method_override(self, request):
        method = request.POST.get(self.METHOD_OVERRIDE_PARAM_KEY)
        if not method:
            method = request.META.get(self.HTTP_METHOD_OVERRIDE_HEADER)
        return method.upper() if method else None


class FormParamsMiddleware(object):
    """Populate request.PUT if the content-type of a PUT request is a form type.
    To insert after "MethodOverrideMiddleware".
    """

    ALLOWED_METHOD   = 'PUT'
    PERCENT_ENCODING = 'application/x-www-form-urlencoded'

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == self.ALLOWED_METHOD:

            if request.META.get('CONTENT_TYPE', '').startswith(self.PERCENT_ENCODING):
                query_string = request.body
            else:
                query_string = ''

            setattr(request, request.method, QueryDict(query_string, request.encoding))

        return None
