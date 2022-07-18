from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from . import views

urlpatterns = [
    path('musicians/', views.MusicianView.as_view()),
    path('musicians/<int:musician_id>/', views.MusicianDetailView.as_view()),
    path('musicians/<int:musician_id>/albums/', views.MusicianAlbumView.as_view()),
    path('musicians/<int:musician_id>/albums/<int:album_id>/songs/', views.MusicianAlbumSongView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
