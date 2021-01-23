from django.contrib import admin
from .models import Article
from .models import Contact


admin.site.register(Contact)

admin.site.register(Article)