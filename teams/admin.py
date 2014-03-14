from django.contrib import admin
import teams.models

class PlayersInLine(admin.StackedInline):
    model = teams.models.Player
    extra = 11

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Team information', {'fields': ['size', 'value']}),
    ]
    inlines = [PlayersInLine]

admin.site.register(teams.models.Team, TeamAdmin)