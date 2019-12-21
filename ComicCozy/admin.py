from django.contrib import admin
from preferences.admin import PreferencesAdmin

from ComicCozy.preferences import NavigationBarSetting
from .models import Comic

admin.site.site_header = "ComicCozy Admin"


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']
#     date_hierarchy = 'pub_date'
#
#
class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'path', 'alt_text', 'is_published')
    list_filter = ['post_date']
    date_hierarchy = 'post_date'


admin.site.register(Comic, ComicAdmin)
admin.site.register(NavigationBarSetting, PreferencesAdmin)
