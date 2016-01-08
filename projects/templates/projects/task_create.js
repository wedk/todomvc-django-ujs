{% load include_as_js_str %}
$('.todo-list').append("{% include_as_js_str 'projects/_task.html' %}");
$('.new-todo').val('');

{% include 'projects/base.js' %}