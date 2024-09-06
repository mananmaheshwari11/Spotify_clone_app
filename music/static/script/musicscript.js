// function to play the song on player 
function playSongAndShowPlayer(songSrc,songId) {
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
playPauseButton.classList.remove('fa fa-play');
playPauseButton.classList.add('fa fa-pause');


//to add this in user history
document.getElementById('song_id').value = songId;
document.getElementById('logHistoryForm').submit();
}
