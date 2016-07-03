from django.conf.urls import url
from django.conf.urls import include
from lotka_volterra import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_calc/$', views.add_calculation),
    url(r'^calc_result/(?P<calc_id>[0-9]+)$', views.calculation_result),
    url(r'^calc_report/(?P<calc_id>[0-9]+)$', views.get_xls_for_calc),
    url(r'^calc_history/$', views.my_calculations),
]
