{% load include_as_js_str %}
var mainSection = $('section.main');
mainSection.toggle(mainSection.find('.todo-list li').length > 0);
mainSection.find('.toggle-all').prop('checked', {% if remaining_tasks_count == 0 %}true{% else %}false{% endif %});
$('footer.footer').replaceWith("{% include_as_js_str 'projects/_footer.html' %}");