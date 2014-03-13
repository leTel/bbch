from django.contrib import admin

import forum.models

class ForumAdmin(admin.ModelAdmin):

	list_display = ('name', 'area', 'languages', 'link')
	list_filter = [ 'languages']
	search_fields = ['name', 'area']


admin.site.register(forum.models.Forum, ForumAdmin)