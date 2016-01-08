{% load include_as_js_str %}
$('#task_{{task.id}}').replaceWith("{% include_as_js_str 'projects/_task.html' %}");