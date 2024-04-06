from django.contrib import admin

from .models import EventModel
from django.utils.html import format_html


class EventAdmin(admin.ModelAdmin):

    def illustration_img(self, obj):
        try:
            obj.illustration_image.url
            return format_html('<a href="{}" style="display: inline;"><img src="{}" style="max-width:100px; max-height:100px; background-position:center; background-size:cover;"/></a>'.format(obj.illustration_image.url, obj.illustration_image.url))
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")
    
    def illustration_vdeo(self, obj):
        try:
             return format_html(f'''<iframe width="100px" height="100px" src="{obj.illustration_video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>''')
        except:
                return format_html("<div style='width:100px; height:100px; background-color: #121212'></div>")

    list_display = ("title", "published", "start_at", "end_at", "created_at", "illustration_img", "illustration_vdeo")
    list_editable = ("published", )


admin.site.register(EventModel, EventAdmin)
