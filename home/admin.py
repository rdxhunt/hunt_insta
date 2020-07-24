from django.contrib import admin

# Register your models here.

from .models import Victimsinfo
from .models import Userinfo


admin.site.register(Victimsinfo)
admin.site.register(Userinfo)
