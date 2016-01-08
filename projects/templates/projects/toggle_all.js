{% with js_completed=completed|yesno:"true,false" %}
  $('{% for id in task_ids %}#task_{{id}}{% if not forloop.last %},{% endif %}{% endfor %}')
    .toggleClass('completed', {{js_completed}})
    .find('input.toggle')
    .prop('checked', {{js_completed}});
{% endwith %}

{% include 'projects/base.js' %}