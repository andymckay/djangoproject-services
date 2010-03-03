from django.conf.urls.defaults import *

urlpatterns = patterns('services.views',
    (r'', 'company_list', {}, "company_list"),
    (r'(?P<slug>\w+)/$', 'company_detail', {}, 'company_detail'),
)
