from django.contrib import admin
from .models import League, Team, Player, Match

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('tier',)
    list_filter = ('tier',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'coach', 'league', 'matches_played', 'wins', 'draws', 'losses', 
        'goals_scored', 'goals_conceded', 'goal_difference', 'points'
    )
    search_fields = ('name',)
    list_filter = ('league',)
    readonly_fields = ('matches_played', 'wins', 'draws', 'losses', 'goal_difference', 'points')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'position')
    search_fields = ('name',)
    list_filter = ('team', 'position')
    ordering = ('team', 'name')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'league', 'date', 'home_score', 'away_score', 'status')
    list_filter = ('league', 'status', 'date')
    ordering = ('-date',)


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]