from django.contrib import admin

from  embed_video.admin  import  AdminVideoMixin
from .models  import  tutorial
#Register your models here.

class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(tutorial, tutorialAdmin)