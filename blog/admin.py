from django.contrib import admin
from blog.models import *
from user.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Hobbies)
admin.site.register(Comment)