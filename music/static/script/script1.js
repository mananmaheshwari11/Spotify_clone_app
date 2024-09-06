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

    // Handle song URL and play the music
    const songUrlElement = document.getElementById('song-url');
    if (songUrlElement) {
        const songUrl = songUrlElement.src;
        audioPlayer.src = songUrl;
        audioPlayer.load();
        audioPlayer.play();
        playPauseBtn.innerHTML = '<i class="fa fa-pause"></i>';
        isPlaying = true;
    }
});
// showBTN functionality
document.addEventListener('DOMContentLoaded', () => {
    const showMoreBtn = document.getElementById('showMoreBtn');
    const cards = document.querySelectorAll('.card');
    let visibleCardsCount = 4;

    showMoreBtn.addEventListener('click', () => {
        // Show 4 more cards or all remaining if fewer than 4
        for (let i = visibleCardsCount; i < visibleCardsCount + 4 && i < cards.length; i++) {
            cards[i].style.display = 'block';
        }

        // Update the number of visible cards
        visibleCardsCount += 4;

        // Hide the Show More button if no more cards to show
        if (visibleCardsCount >= cards.length) {
            showMoreBtn.style.display = 'none';
        }
    });
});

// artist button
document.addEventListener('DOMContentLoaded', () => {
    const showMoreBtn = document.getElementById('showMoreBtn1');
    const hiddenCards = document.querySelectorAll('.card.hidden');
    let visibleCardsCount = 4;

    showMoreBtn.addEventListener('click', () => {
        // Show 4 more cards or all remaining if fewer than 4
        for (let i = visibleCardsCount; i < visibleCardsCount + 4 && i < hiddenCards.length; i++) {
            hiddenCards[i].style.display = 'block';
        }

        // Update the number of visible cards
        visibleCardsCount += 4;

        // Hide the Show More button if no more cards to show
        if (visibleCardsCount >= hiddenCards.length) {
            showMoreBtn.style.display = 'none';
        }
    });
});
//play via playlist
function playSongAndShowPlayer(songSrc) {
    const audioPlayerContainer = document.querySelector('.player-container');
    const audioPlayer = document.getElementById('audio-player');
    const playPauseButton = document.getElementById('play-pause').querySelector('i');

    // Set the audio source
    audioPlayer.src = songSrc;
    
    // Make the audio player container visible
    audioPlayerContainer.style.display = 'block';
    
    // Play the audio
    audioPlayer.play();

    // Change the play/pause button icon to pause
    playPauseButton.classList.remove('fa-play');
    playPauseButton.classList.add('fa-pause');
}
