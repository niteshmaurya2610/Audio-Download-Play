## User Foder Path Defenition

url_listPath ="/home/nitesh/Scripts/Python/Audio-Download-Play/song_url.txt"  ## set the path to txt file having youtube urls

output_path = "/home/nitesh/Scripts/Python/Audio-Download-Play/Music"  ## set the path to Music Folder where media will be downloaded


#################################################################################
import os,time
import vlc
import select
import sys
from pynput import keyboard
from pytube import YouTube

def download_audio(youtube_url, output_path):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = os.path.join(output_path, audio_stream.default_filename)
    
    if not os.path.exists(audio_file):
        audio_stream.download(output_path)
        print("Downloaded:", yt.title)
    else:
        print("File already downloaded:", yt.title)
    
    return audio_file

def play_audio(audio_file, media_player):
    media_player.set_mrl(audio_file)
    media_player.play()

def stop_audio(media_player):
    media_player.stop()

def pause_audio(media_player):
    media_player.pause()

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False

def get_input_with_timeout(prompt, timeout):
    # sys.stdout.write(prompt)
    # sys.stdout.flush()

    start_time = time.time()
    input_given = False

    while time.time() - start_time < timeout:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            user_input = input()
            input_given = True
            break

    if not input_given:
        user_input = ""

    return [input_given,user_input]

def controller(media_player,idx):
    key_pressed = ""
    print("Press Enter to play next song,\n or num+Enter to play that song number in playlist,\n or any other keyword+Enter to pause...\n")
    while media_player.get_state() != vlc.State.Ended:
        inOut=get_input_with_timeout("",timeout_seconds)
        if (inOut[0]):
            key_pressed = inOut[1]
            break


    if key_pressed == "":
        # Continue to the next song
        stop_audio(media_player)
        idx=idx+1
    elif key_pressed.isdigit():
        stop_audio(media_player)
        idx = abs(int(key_pressed)-1)
    else:
        # Pause the current song
        pause_audio(media_player)
        input("Press Enter to resume.")
        # Resume the song if the user presses any other key
        media_player.play()
        idx=controller(media_player,idx)
    return idx



def main():
    
    youtube_urls = [
        
        # Add URLs as needed
    ]
    if os.path.exists(url_listPath):
        with open(url_listPath) as file:
            for line in file:
                if(line.startswith("https://")):
                    youtube_urls.append(line)
    else:
        print(url_listPath, " Given url path does not exists.")

    
    
    if not os.path.exists(output_path):
        print("Making Dir", output_path)
        os.makedirs(output_path)
    # else:
    #     print(output_path, "Music Directory Exists.")
    print("Do you want to download the songs? (y/n) [3s Default: 'n']" )
    if(get_input_with_timeout("",3)=='y'):
    # Download or locate all audio files
        for url in youtube_urls:
            try:
                audio_file = download_audio(url, output_path)
            except:
                print("Failed to download ", audio_file,". Proceeding... ")
    else:
        print("Proceeding with already existing media.")
    # Initialize VLC media player
    vlc_args = ["--quiet"]  # Use --quiet argument to suppress output
    instance = vlc.Instance(vlc_args)
    media_player = instance.media_player_new()

    # List and play music files
    music_files = [f for f in os.listdir(output_path) if f.endswith(".mp3") or f.endswith(".mp4")]

    print("Playlist of available music files:")
    music_list=[]
    for idx, music_file in enumerate(music_files):
        print(f"{idx + 1}. {music_file}")
        total_idx=idx+1
        music_list.append(music_file)
    total_idx = len(music_list)
    idx = 0
    while idx<total_idx:
        music_file=music_list[idx]
        print(f"\033[96mNow Playing - {idx + 1}/{total_idx}. {music_file}\033[0m") # print in cyan blue
        play_audio(os.path.join(output_path, music_file), media_player)
        idx=controller(media_player,idx)

    print("\033[91mPlaylist Over.\033[0m") #print in red





timeout_seconds = 1
default_input = "default_value"
if __name__ == "__main__":
    main()


