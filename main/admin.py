from django.contrib import admin

# Register your models here.
from main.models import *


class KabarAdmin(admin.ModelAdmin):
    class Meta:
        model = Kabar

    list_display = 'title icon date'.split()

    def icon(self, obj):
        return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url

    icon.allow_tags = True


class NpaAdmin(admin.ModelAdmin):
    class Meta:
        model = Npa

    list_display = 'name number date'.split()


class EducationAdmin(admin.ModelAdmin):
    class Meta:
        model = Education

    list_display = 'name category date'.split()


class AttestationAdmin(admin.ModelAdmin):
    class Meta:
        model = Atestation

    list_display = 'name number date'.split()


class ProtocolAdmin(admin.ModelAdmin):
    class Meta:
        model = Protocol

    list_display = 'name date'.split()


admin.site.register(Kabar, KabarAdmin)
admin.site.register(Npa, NpaAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Atestation, AttestationAdmin)
admin.site.register(Protocol, ProtocolAdmin)
