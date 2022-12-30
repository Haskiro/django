from email.policy import default
from django.db import router
from rest_framework.routers import DefaultRouter
from artist.views import ArtistViewSet
from album.views import AlbumViewSet
from authentication.views import UserViewSet
from track.views import TrackViewSet
from playlist.views import PlaylistViewSet
from genre.views import GenreViewSet

router = DefaultRouter()
 
router.register('artists', ArtistViewSet)
router.register('albums', AlbumViewSet)
router.register('genres', GenreViewSet)
router.register('playlists', PlaylistViewSet)
router.register('tracks', TrackViewSet)
router.register('auth', UserViewSet)
