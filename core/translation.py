from modeltranslation.translator import register, TranslationOptions
from .models import Profile, Hobbie, Project

@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('languages', 'city','country', 'about')

@register(Hobbie)
class HobbieTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name',)
