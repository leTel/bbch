from django.contrib import admin
from django.db import models

import news.models

class NewAdmin(admin.ModelAdmin):

	list_display = ('title', 'categories', 'language', 'published_date')
	list_filter = [ 'categories', 'language', 'published_date']
	search_fields = ['title', 'content']

class NewCategoryAdmin(admin.ModelAdmin):

	list_display = ('name', 'category')
	list_filter = [ 'category']
	search_fields = ['name', 'description']

class LanguageAdmin(admin.ModelAdmin):
	pass

admin.site.register(news.models.New, NewAdmin)
admin.site.register(news.models.NewCategory, NewCategoryAdmin)
admin.site.register(news.models.Language, LanguageAdmin)