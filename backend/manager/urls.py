from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from core.views import IndexView
from rest_framework import routers
from clubs import views as club_views
from competitions import views as competition_views
from matches import views as matches_views
from profiles import views as profiles_views

router = routers.DefaultRouter()
router.register(r"clubs", club_views.ClubViewSet, 'clubs')
router.register(r"teams", club_views.TeamViewSet, "teams")
router.register(r"age-categories", competition_views.AgeCategoryViewSet, "age-category")
router.register(r"seasons", competition_views.SeasonViewSet, "season")
router.register(r"competition", competition_views.CompetitionsViewSet, "competition")
router.register(r"matches_list", matches_views.GameListViewSet, "matches_list")
router.register(r"profiles", profiles_views.UserProfileViewSet, "profiles")

urlpatterns = [
    path("admin/", admin.site.urls),
    # API
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    
    # Main page
    path('', IndexView.as_view(), name="index"),

    # Clubs
    path('clubs/', include("clubs.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)