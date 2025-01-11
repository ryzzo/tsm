from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import LeagueViewSet, TeamViewSet, PlayerViewSet, MatchViewSet, MatchesByDateViewSet

router = DefaultRouter()
router.register(r'leagues', LeagueViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'matches-by-date', MatchesByDateViewSet, basename='match-by-date')

urlpatterns = [
    
] + router.urls