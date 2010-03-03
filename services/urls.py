from django.conf.urls.defaults import *

urlpatterns = patterns('services.views',
    (r'create/$', 'company_create', {}, "company_create"),
    (r'(?P<slug>\w+)/$', 'company_detail', {}, 'company_detail'),
    (r'', 'company_list', {}, "company_list"),
)
