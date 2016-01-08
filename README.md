# todomvc-django-ujs

TodoMVC-like experiment using [Django](https://www.djangoproject.com/) and [jquery-ujs](https://github.com/rails/jquery-ujs).

This experiment differs from classic TodoMVC implementations by allowing to create multiple projects ; each project containing its own set of tasks (todo items).

* based on [TodoMVC](http://todomvc.com/)
* database persistence
* CRUD projects
* CRUD tasks (todo items)


### Technical details

* use [jquery-ujs](https://github.com/rails/jquery-ujs), the unobtrusive scripting adapter for [jQuery](http://jquery.com/), developed for the Ruby on Rails framework
* custom Django middlewares to support PUT / DELETE http verbs
* custom Django template tag to include / render an HTML template as a JavaScript string
* custom CSRF header name for compatibility with [jquery-ujs](https://github.com/rails/jquery-ujs)


### Prerequisites

* Python 3.5.x
* Django 1.9.x
* Node.js 4.x (and npm 2.x) to build assets (SASS/CSS, JS) with Grunt
* ruby 1.9.x to build SASS files with the SASS gem


### Acknowledgements

This experiment was especially inspired by the following work:

* [The TodoMVC Project on Rails 4](http://www.mattdeleon.net/) by Matt De Leon


### License

MIT