from django.contrib import admin
from mysite.models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date') #admin 中可以看到的內容
admin.site.register(Post,PostAdmin)


