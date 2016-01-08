from django.conf.urls import url

from . import views


urlpatterns = [
    url( r'^$',                                              views.index,                           name='index'            ),
    url( r'^(?P<pk>[0-9]+)/$',                               views.show,                            name='detail'           ),
    url( r'^(?P<pk>[0-9]+)/active/$',                        views.show, { 'filter': 'active'    }, name='detail_active'    ),
    url( r'^(?P<pk>[0-9]+)/completed/$',                     views.show, { 'filter': 'completed' }, name='detail_completed' ),
    url( r'^create/$',                                       views.create,                          name='create'           ),
    url( r'^(?P<pk>[0-9]+)/update/$',                        views.update,                          name='update'           ),
    url( r'^(?P<pk>[0-9]+)/delete/$',                        views.delete,                          name='delete'           ),
    url( r'^(?P<pk>[0-9]+)/clear_completed/$',               views.clear_completed,                 name='clear_completed'  ),
    url( r'^(?P<pk>[0-9]+)/toggle/all/$',                    views.toggle_all,                      name='toggle_all'       ),
    url( r'^(?P<project_id>[0-9]+)/create/$',                views.create_task,                     name='create_task'      ),
    url( r'^(?P<project_id>[0-9]+)/update/(?P<pk>[0-9]+)/$', views.update_task,                     name='update_task'      ),
    url( r'^(?P<project_id>[0-9]+)/delete/(?P<pk>[0-9]+)/$', views.delete_task,                     name='delete_task'      ),
    url( r'^(?P<project_id>[0-9]+)/toggle/(?P<pk>[0-9]+)/$', views.toggle_task,                     name='toggle_task'      ),
]