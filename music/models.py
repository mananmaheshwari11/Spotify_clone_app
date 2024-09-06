from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.
class Artist(models.Model):
    artist_name=models.CharField(_("Artist Name"),max_length=50)
    artist_image=models.ImageField(_("Artist Image"),upload_to='artist/',null=True)
    created=models.DateTimeField(_("CreatedAt"),auto_now_add=True)
    last_update=models.DateTimeField(_("UpdatedAt"),auto_now=True)

    class Meta:
        verbose_name=_("Artist")
        verbose_name_plural=_("Artists")
    

    def __str__(self):
        return self.artist_name
    
class Album(models.Model):
    artist=models.ForeignKey("Artist",verbose_name=_("Album's Artist"),on_delete=models.CASCADE)
    album_name=models.CharField(_("Album Name"),max_length=50)
    created=models.DateTimeField(_("CreatedAt"),auto_now_add=True)
    last_update=models.DateTimeField(_("UpdatedAt"),auto_now=True)


    class Meta:
        verbose_name=_("Album")
    
    def __str__(self):
        return self.album_name
    
class Song(models.Model):
    album=models.ForeignKey("Album",on_delete=models.CASCADE,verbose_name=_("Song Album"))
    songThumbnail=models.ImageField(_("Song Thumbnail"),upload_to='thumbnail/',help_text=".jpg, .png, .jpeg, .svg supported")
    song_name=models.CharField(_("Song Name"),max_length=50)
    song=models.FileField(_("song"),upload_to='songs/',help_text="mp3* required")
    created=models.DateTimeField(_("CreatedAt"),auto_now_add=True)
    last_update=models.DateTimeField(_("UpdatedAt"),auto_now=True)
    artists = models.ManyToManyField(Artist)
    class Meta:
        verbose_name=_("Song")
    
    def __str__(self):
        return self.song_name
class Library(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(_("Library Name"),max_length=50,null=False)
    song=models.ManyToManyField(Song,blank=True)
    class Meta:
        verbose_name=_("Library")
    
    def __str__(self):
        return self.name
    

class userHistory(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song=models.ForeignKey(Song,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.first_name
    