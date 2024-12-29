from rest_framework.routers import DefaultRouter
from .views import LeagueViewSet, TeamViewSet, PlayerViewSet, MatchViewSet

router = DefaultRouter()
router.register(r'leagues', LeagueViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [

] + router.urls