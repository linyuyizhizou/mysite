from django.contrib import admin

from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display =("id","title","author","is_deleted","content","create_time","last_updated_time")
    ordering = ("id",)


admin.site.register(Article,ArticleAdmin)



