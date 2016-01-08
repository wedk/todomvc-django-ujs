{% load include_as_js_str %}
$('.project-list').append("{% include_as_js_str 'projects/_project.html' %}");
$('.new-project').val('');