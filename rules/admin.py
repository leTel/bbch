from django.contrib import admin

import rules.models

class RulesAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'release_date', 'comments')
    list_filter = [ 'language']
    search_fields = ['description', 'name', 'comment']

class LanguageAdmin(admin.ModelAdmin):
	pass

class SkillAdmin(admin.ModelAdmin):
	pass

class SkillTypeAdmin(admin.ModelAdmin):
	pass

class SkillFRAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,	{'fields': ['name', 's_type', 'description']}),
]

class SkillTypeFRAdmin(admin.ModelAdmin):
	pass

admin.site.register(rules.models.Rule, RulesAdmin)
admin.site.register(rules.models.Language, LanguageAdmin)
admin.site.register(rules.models.Skill, SkillAdmin)
admin.site.register(rules.models.SkillType, SkillTypeAdmin)
admin.site.register(rules.models.SkillFR, SkillFRAdmin)
admin.site.register(rules.models.SkillTypeFR, SkillTypeFRAdmin)