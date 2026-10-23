from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from core.models import Profile, Project, Hobbie, Contact, CodeLanguage

# Register your models here.
class ProfileAdmin(TranslationAdmin):
    list_display = ['image','about']

class ProjectAdmin(TranslationAdmin):
    list_display = ['name','url', 'image']

class HobbieAdmin(TranslationAdmin):
    list_display = ['name','image']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','image']

class CodeLanguageAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Hobbie, HobbieAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(CodeLanguage, CodeLanguageAdmin)

