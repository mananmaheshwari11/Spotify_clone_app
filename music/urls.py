from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('listen',views.listen,name="listen"),
    path('song/<int:pid>',views.song,name="song"),
    path('song/artist/<int:pid>',views.artist,name="artist"),
    path('library',views.get_libraries,name="libraries"),
    path('library/songs/<int:lid>',views.get_library_songs,name="getsong"),
    path('libraries/new/', views.library_create, name='library_create'),
    path('add-to-library/', views.AddToLibraryView.as_view(), name='add_to_library'),
    path('delete_library/<int:libid>',views.delete_library,name='delete_library'),
    path('delete_from_library/<int:song_id>/<int:library_id>',views.delete_from_library,name="delete_from library"),
    path('info',views.info,name="info"),
    path('signout',views.logout_view,name="signout"),
    path('log_history', views.log_history, name='log_history'),
    path('search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)