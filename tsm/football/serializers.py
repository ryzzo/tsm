from rest_framework import serializers
from .models import League, Team, Player, Match

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['tier']


class TeamSerializer(serializers.ModelSerializer):
    league_name = serializers.ReadOnlyField(source='league.tier')

    class Meta:
        model = Team
        fields = [
            'id', 'name', 'coach', 'league', 'league_name', 'matches_played', 'wins', 'draws', 'losses', 
            'goals_scored', 'goals_conceded', 'goal_difference', 'points'
        ]

    def validate_league(self, value):
        if not League.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("selected league does not exist")
        return value


class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.ReadOnlyField(source='team.name')

    class Meta:
        model = Player
        fields = ['id', 'name', 'team_name', 'position']


class MatchSerializer(serializers.ModelSerializer):
    home_team_name = serializers.ReadOnlyField(source='home_team.name')
    away_team_name = serializers.ReadOnlyField(source='away_team.name')
    league_name = serializers.ReadOnlyField(source='league.tier')

    class Meta:
        model = Match
        fields = ['id', 'home_team', 'away_team', 'home_team_name', 'away_team_name', 'league_name', 'date', 'home_score', 'away_score', 'status']
        extra_kwargs = {
            'home_score':{'required':False},
            'away_score':{'required':False},
        }