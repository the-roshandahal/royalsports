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
admin.site.register(Contact)


class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created')
    summernote_fields = ('blog',) 
admin.site.register(Blog,BlogAdmin)


class ParticipationAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',) 
admin.site.register(Participation,ParticipationAdmin)




class RcsAdmin(SummernoteModelAdmin):
    summernote_fields = ('bottom_text','booking_details2','booking_details1') 
admin.site.register(JoinRcs,RcsAdmin)

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







class ImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1 

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Gallery, GalleryAdmin)
