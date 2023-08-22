from django.contrib import admin
from.models import *
from django_summernote.models import Attachment
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

admin.site.unregister(Attachment)
admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.register(Slider)
admin.site.register(Testimonial)
admin.site.register(Partner)


class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created')
    summernote_fields = ('blog',) 
admin.site.register(Blog,BlogAdmin)

class ReadOnlyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Disable the "Add" button
        return True
    
    def has_change_permission(self, request, obj=None):
        # Allow editing
        return True
    
    def has_delete_permission(self, request, obj=None):
        # Disable the "Delete" button
        return False

@admin.register(CompanySetup)
class CompanySetupAdmin(ReadOnlyModelAdmin):
    pass

@admin.register(HomeContent)
class HomeContentAdmin(ReadOnlyModelAdmin):
    pass