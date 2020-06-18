from django.contrib import admin
from polls.models import AccessRecord, Topic, Webpage, Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']

class TopicAdmin(admin.ModelAdmin):
    fields = ['top_name']

class WebpageAdmin(admin.ModelAdmin):
    fields = ["topic", "name", "url"]

class AccessRecordAdmin(admin.ModelAdmin):
    fields = ["name", "date"]

admin.site.register(AccessRecord, AccessRecordAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Webpage, WebpageAdmin)