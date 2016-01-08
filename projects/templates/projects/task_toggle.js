{% with completed=task.completed|yesno:"true,false" %}
  $('#task_{{task.id}}')
    .toggleClass('completed', {{completed}})
    .find('input.toggle')
    .prop('checked', {{completed}});
{% endwith %}

{% include 'projects/base.js' %}