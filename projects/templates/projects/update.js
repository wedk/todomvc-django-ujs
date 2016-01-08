{% load include_as_js_str %}
$('h1').replaceWith("{% include_as_js_str 'projects/_project_title.html' %}");