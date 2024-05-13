from pytube import YouTube
from pytube import Playlist
from sys import argv

# TODO: check if provided link actually links to a YT playlist or video
def validateLink(link):
    if(1):
        return True
    return False

# TODO: check automatically if link provided is a playlist or a video and proceed accordingly
def detectVideoOrPlaylist(link):
    print("Hello World")

# download single video
def downloadVideo(videoLink):
    video = YouTube(videoLink)
    print("Downloading Video: ", video.title)
    downloader = video.streams.get_highest_resolution()
    downloader.download('/Users/bastiangerkum/Desktop')

def downloadPlaylist(playlistLink):
    print("Playlist")
    playlist = Playlist(playlistLink)
    plTitle = playlist.title
    print("Downloading Playlist: ", plTitle)
    #TODO: depending on OS create folder named after plTitle (if doesnt exist already)
    plLength = playlist.length-1
    videoCounter = 0
    for videoURL in playlist.video_urls:
        downloadVideo(videoURL)
        videoCounter+=1
        print("Progress: ", videoCounter, "/", plLength, " Videos")

# get link via argument 
# TODO: check if argument is empty: print error message "a link to video/playlist needs to be provided"
link = argv[1]
downloadVideo(link)