from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'^page/(?P<page_id>\d+)/$', views.page, name='page'),
    url(r'^add_category/$', views.add_category, name='add_category'),
]
