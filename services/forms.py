from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from services.models import Company


class CompanyForm(forms.ModelForm):
    
    class Meta:
        model = Company
        fields = [
            "name", "description", "country", "contact_name", "contact_phone",
            "contact_email", "logo"
        ]
        
    def save(self):
        pass
        # TODO: send an email with a link to go approve the rest...
        
        
#         
#         send_mail()            
#         ctx = {"company": self, "company_list": Companies.object.all()}
#         body = render_to_string("services/company_create_email.html", ctx)
#         send_mail('Subject here', 'Here is the message.', 'from@example.com',
#     ['to@example.com'], fail_silently=False)    
#     
#     
# """
# 
# when you submit your company:
# 
# check against other companies,
# 
# 
# """