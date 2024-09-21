import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Song,Album,Artist,Library, userHistory
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from mutagen.mp3 import MP3
from .forms import LibraryForm, UserProfileForm
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request,'music/index.html')

def listen(request):
    song=Song.objects.all()
    artist=Artist.objects.all()
    album=Album.objects.all()
    return render(request,'music/music.html',{'song':song,'artist':artist,'album':album})

def get_audio_duration(file_path):
    if file_path.endswith('.mp3'):
        audio = MP3(file_path)
    return audio.info.length if hasattr(audio, 'info') else audio.duration_seconds
def format_duration(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}:{seconds:02}"

# // song fetch
@login_required
def song(request,pid=0):
    if pid:
        song=Song.objects.get(id=pid)
        libraries=Library.objects.filter(user=request.user)
        artists=song.artists.all()
        return render(request,'music/desc.html',{'song':song , "artists":artists,"libraries":libraries})

# get song for each artist
@login_required
def artist(request,pid=0):
    if pid:
        artist=Artist.objects.get(id=pid)
        songs = Song.objects.filter(artists=artist)
        for song in songs:
            file_path=song.song.path
            duration = get_audio_duration(file_path)
            song.song_duration=format_duration(duration)
        return render(request,'music/artist.html',{'artist':artist,"songs":songs})
    
# getting libraries for the user
@login_required
def get_libraries(request):
        libraries=Library.objects.filter(user=request.user)
        form=LibraryForm()
        return render(request,'music/library.html',{'libraries':libraries, 'form':form})


# creating the library
@login_required
def library_create(request):
    if request.method == "POST":
        form = LibraryForm(request.POST)
        if form.is_valid():
            library = form.save(commit=False)
            library.user = request.user
            library.save()
            form.save_m2m()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request'})


def delete_library(request, libid=0):
    if libid:
        # Fetch the library object by its ID
        lib = get_object_or_404(Library, id=libid)
        lib.delete()  # Deletes the library object

        # Redirect to the library list page after deletion
        return redirect('/music/library')  # Adjust 'library_list' to your actual list view

    # If the request is not POST, return an error response
    return HttpResponse("Invalid request", status=400)


# adding the song to the library of personal user
@login_required
@csrf_exempt
def add_to_library(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        song_id = data.get('song_id')
        library_id = data.get('library_id')

        song = get_object_or_404(Song, id=song_id)
        library = get_object_or_404(Library, id=library_id, user=request.user)

        library.songs.add(song)
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

#for posting the song into library using xhr in fetch the secure ajax 
class AddToLibraryView(View):
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        song_id = data.get('song_id')
        library_id = data.get('library_id')

        song = get_object_or_404(Song, id=song_id)
        library = get_object_or_404(Library, id=library_id, user=request.user)

        library.song.add(song)
        return JsonResponse({'success': True})


#getting the song of the particular library 
@login_required
def get_library_songs(request,lid=0):
    if lid:
        lib=Library.objects.get(id=lid)
        songs=lib.song.all()
        for song in songs:
            file_path=song.song.path
            duration = get_audio_duration(file_path)
            song.song_duration=format_duration(duration)
        return render(request,'music/libmusic.html',{'lib':lib,'songs':songs})
@login_required
@csrf_exempt
def delete_from_library(request,song_id,library_id):
    if request.method == 'POST':
        try:
            s = get_object_or_404(Song, id=song_id)
            library = get_object_or_404(Library, id=library_id, user=request.user)
            # Remove the song from the library
            library.song.remove(s)
            return JsonResponse({'success': True, 'message': 'Song removed from library'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@login_required
def info(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('listen')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'music/info.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('signin')


def log_history(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        song = get_object_or_404(Song, id=song_id)
        userHistory.objects.create(user=request.user, song=song)
        return HttpResponse(status=204)
    return HttpResponse(status=400)


def delete_library(request, libid=0):
    if libid:
        # Fetch the library object by its ID
        lib = get_object_or_404(Library, id=libid)
        lib.delete()  # Deletes the library object

        # Redirect to the library list page after deletion
        return redirect('/music/library')  # Adjust 'library_list' to your actual list view

    # If the request is not POST, return an error response
    return HttpResponse("Invalid request", status=400)
    
def search_results(request):
    query = request.GET.get('q', '')
    songs = Song.objects.filter(song_name__icontains=query)  # Adjust field name as necessary
    libraries = Library.objects.filter(name__icontains=query)  # Adjust field name as necessary
    artists = Artist.objects.filter(artist_name__icontains=query)  # Adjust field name as necessary

    context = {
        'query': query,
        'songs': songs,
        'libraries': libraries,
        'artists': artists
    }
    return render(request, 'music/search.html', context) 