# Audio-Download-Play

This is a Python script that allows you to download audio from YouTube videos and play them using the VLC media player. You can create a playlist of YouTube audio, download the files, and then play them sequentially. The script also provides basic control options like play, pause, and skip.

## Prerequisites

- Python 3.x
- VLC media player
- pynput
- pytube

You can install the required Python libraries using the following command:

```bash
pip install pynput pytube3
```

## Usage

1. Clone this repository to your local machine.

2. Install VLC media player on your system. You can download it from [VLC's official website](https://www.videolan.org/vlc/index.html).

3. Open a terminal and navigate to the repository's directory.

4. Create a text file named `song_url.txt` (change the directory path in `line 3`) and add YouTube URLs of the songs you want to download, each on a separate line.

5. Run the script using the following command:

```bash
python3 -u audioPlay.py
```

6. The script will ask if you want to download the songs. Type `y` and press Enter to initiate the download (respond within 3 seconds otherwise by default it takes `n`).

7. The script will download the audio files and save them in the "Music" directory. If the directory doesn't exist, it will be created (remember to change the directory path in `line 5`).

8. The VLC media player will launch and play the downloaded audio files in sequence. You can control playback using the following commands:
   - Press Enter to play the next song.
   - Type a number followed by Enter to play a specific song from the playlist.
   - Type any other keyword followed by Enter to pause the current song. Press Enter again to resume playback.

9. The playlist will continue playing until all songs have been played.

10. To integrate this player in terminal, `python3 -u audioPlay.py` can be aliased in ~/.bashrc or ~/.bash_aliases.
    Example of alias line in to be added in ~/.bashrc or ~/.bash_aliases:
```bash
alias bhojpuri="python3 -u /full/path/to/audioPlay.py"
```
   Here, the player can be invoked by ccommand `bhojpuri`.

## Notes

- Make sure to have a stable internet connection while running the script to ensure successful song downloads.
- The script uses VLC media player for playback. Ensure VLC is properly installed on your system before running the script.



---

Feel free to contribute, report issues, or suggest improvements!
