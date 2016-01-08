$('{% for id in task_ids %}#task_{{id}}{% if not forloop.last %},{% endif %}{% endfor %}').remove();

{% include 'projects/base.js' %}