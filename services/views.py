from django.views.generic.list_detail import object_list, object_detail
from django.shortcuts import render_to_response


from services.models import Company
from services.forms import CompanyForm


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


def company_create(request, template="services/company_create.html"):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(form.next())
    
    ctx = {
        "form": form
    }
    
    return render_to_response(template, ctx)
    
    