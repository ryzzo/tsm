from rest_framework import viewsets
from .models import League, Team, Player, Match
from django.db.models import F
from .serializers import LeagueSerializer, TeamSerializer, PlayerSerializer, MatchSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by(
        F('points').desc(),
        F('goal_difference').desc(),
        F('goals_scored').desc(),
    )
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
