from django.contrib import admin
from polls.models import AccessRecord, Topic, Webpage, Person

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Person)
admin.site.register(Topic)
admin.site.register(Webpage)