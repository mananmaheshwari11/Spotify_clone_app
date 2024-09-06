from django.contrib import admin
from .models import Artist,Album,Song,Library,userHistory
# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display=("id","artist_name","artist_image","created","last_update")

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=("id","song_name","display_artists","album","song","created","last_update")

    def display_artists(self, obj):
        return ', '.join([artist.artist_name for artist in obj.artists.all()])

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=("id","album_name","artist","created","last_update")

@admin.register(Library)
class AlbumAdmin(admin.ModelAdmin):
    list_display=("user","count_lib","display_song")
    def count_lib(self,obj):
        return', '.join([x.name for x in Library.objects.filter(user=obj.user)])
    def display_song(self, obj):
        return ', '.join([song.song_name for song in obj.song.all()])
    
@admin.register(userHistory)
class HistoryAdmin(admin.ModelAdmin):
    list_display=("user","song")
    