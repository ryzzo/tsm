from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import League, Team, Player, Match
from django.db.models.functions import TruncDate
from django.db.models import F
from .serializers import LeagueSerializer, TeamSerializer, PlayerSerializer, MatchSerializer
from django.http import JsonResponse


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


class MatchesByDateViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def list(self, request, *args, **kwargs):
        matches = self.queryset.annotate(match_date=TruncDate('date')).order_by('match_date')
        grouped_matches = {}

        for match in matches:
            date = match.date.strftime('%Y-%m-%d')
            if date not in grouped_matches:
                grouped_matches[date] = []
            grouped_matches[date].append(self.get_serializer(match).data)

        return Response(grouped_matches)


def match_detail(request, id):
    try:
        match = Match.objects.get(id=id)
        home_team_players = match.home_team.player_set.all()
        away_team_players = match.away_team.player_set.all()

        def format_formation(formation, players):
            return {
                position: [player.name for player in players.filter(id__in = player_ids)]
                for position, player_ids in formation.items()
            }
        
        data = {
            "id":match.id,
            "home_team":match.home_team.name,
            "away_team":match.away_team.name,
            "date":match.date,
            "formation_home_team":format_formation(match.formation_hometeam, home_team_players),
            "formation_away_team":format_formation(match.formation_awayteam, away_team_players),
        }
        
        return JsonResponse(data)
    except Match.DoesNotExist:
        return JsonResponse({"error":"Match not found"}, status=404)