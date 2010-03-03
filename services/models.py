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
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to="companies")
    country = models.CharField(max_length=255)
    state = models.IntegerField(choices=states)
    sponsorship_level = models.IntegerField(choices=levels)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name

#     def get_absolute_url(self):
#         return "/%s/" % self.slug