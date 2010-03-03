from django.db import models

states = (
    (1, "unapproved"),
    (2, "approved"),
    (3, "denied"),
)

levels = (
    (1, "none"),
    (2, "sponsor"),
)

class Company(models.Model):
    # contact email / name
    # contact phone#
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=255)

    
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to="companies")
    country = models.CharField(max_length=255)
    state = models.IntegerField(choices=states)
    sponsorship_level = models.IntegerField(choices=levels)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    slug = models.SlugField()
    
    # notes = 
    
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
   
    
    
#    def save(self):
#    forms.DateField(initial=datetime.date.today)
    
    
    def __unicode__(self):
        return self.name

#     def get_absolute_url(self):
#         return "/%s/" % self.slug