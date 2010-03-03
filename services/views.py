from django.views.generic.list_detail import object_list, object_detail

from models import Company


def company_list(request):
    queryset = Company.objects.all()
    kwargs = {
        "template_object_name": "company",
        "template_name": "services/company_list.html",
        "extra_context": {},        
    }
    return object_list(request, queryset, **kwargs)

def company_detail(request, slug):
    queryset = Company.objects.all()
    kwargs = {
        "template_object_name": "company",
        "template_name": "services/company_detail.html",
        "extra_context": {},
    }
    return object_detail(request, queryset, **kwargs)
