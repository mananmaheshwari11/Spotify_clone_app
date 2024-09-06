document.addEventListener('DOMContentLoaded', () => {
    const audioPlayer = document.getElementById('audio-player');
    const playPauseBtn = document.getElementById('play-pause');
    const progressBar = document.getElementById('progress-bar');
    const progress = document.getElementById('progress');
    const volumeControl = document.getElementById('volume');
    let isPlaying = false;

    // Play/Pause button functionality
    playPauseBtn.addEventListener('click', () => {
        if (isPlaying) {
            audioPlayer.pause();
            playPauseBtn.innerHTML = '<i class="fa fa-play"></i>';
        } else {
            audioPlayer.play();
            playPauseBtn.innerHTML = '<i class="fa fa-pause"></i>';
        }
        isPlaying = !isPlaying;
    });

    // Update progress bar
    audioPlayer.addEventListener('timeupdate', () => {
        const percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        progress.style.width = percent + '%';
    });

    // Seek functionality
    progressBar.addEventListener('click', (event) => {
        const rect = progressBar.getBoundingClientRect();
        const offsetX = event.clientX - rect.left;
        const percent = offsetX / progressBar.offsetWidth;
        audioPlayer.currentTime = percent * audioPlayer.duration;
    });

    // Volume control
    volumeControl.addEventListener('input', (event) => {
        audioPlayer.volume = event.target.value;
    });

    // AJAX navigation
    document.querySelectorAll('.ajax-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            fetchPage(this.href);
            history.pushState(null, '', this.href);
        });
    });

    function fetchPage(url) {
        fetch(url, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
            .then(response => response.text())
            .then(data => {
                document.getElementById('main-content').innerHTML = data;
                reattachEventListeners();
            })
            .catch(error => console.error('Error:', error));
    }

    // Handle browser back/forward buttons
    window.addEventListener('popstate', function() {
        fetchPage(location.href);
    });

    // Reattach event listeners for AJAX-loaded content
    function reattachEventListeners() {
        document.querySelectorAll('.ajax-link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                fetchPage(this.href);
                history.pushState(null, '', this.href);
            });
        });

        // Handle song URL and play the music after AJAX navigation
        const songUrlElement = document.getElementById('song-url');
        if (songUrlElement) {
            const songUrl = songUrlElement.src;
            audioPlayer.src = songUrl;
            audioPlayer.load();
            audioPlayer.play();
            playPauseBtn.innerHTML = '<i class="fa fa-pause"></i>';
            isPlaying = true;
        }
    }
});
