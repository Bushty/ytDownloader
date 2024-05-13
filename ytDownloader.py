from pytube import YouTube
from pytube import Playlist
from sys import argv
import os

# check which OS the script is being run on
def isWindows():
    if os.name == "nt":
        return True
    return False

# depending on OS select Downloadpath
def getDownloadPath():
    homePath = os.path.expanduser("~")
    desktopPath = os.path.join(homePath, "Desktop")
    downloadFolderPath = os.path.join(desktopPath, "ytDownloads")
    if not os.path.exists(downloadFolderPath):
        os.makedirs(downloadFolderPath)
        print(f"Folder #{downloadFolderPath} created successfully")
    return downloadFolderPath

def makePlaylistFolder(playlistName):
    print("testFolder");

# TODO: check if provided link actually links to a YT playlist or video
def validateLink(link):
    if(1):
        return True
    return False

# TODO: check automatically if link provided is a playlist or a video and proceed accordingly
def isPlaylist(link):
    if link.startswith("https://www.youtube.com/playlist?list="):
        return True
    return False

# download single video
def downloadVideo(videoLink, playlistFolder=None):
    downloadPath = getDownloadPath()
    if playlistFolder is not None:
        downloadPath = os.path.join(downloadPath, playlistFolder)
        if not os.path.exists(downloadPath):
            os.makedirs(downloadPath)
            print(f"Folder #{downloadPath} created successfully")
    video = YouTube(videoLink)
    print("Downloading Video: ", video.title)
    downloader = video.streams.get_highest_resolution()
    downloader.download(downloadPath)

# download all videos in a playlist
def downloadPlaylist(playlistLink):
    playlist = Playlist(playlistLink)
    plTitle = playlist.title
    plLength = playlist.length
    print("Downloading Playlist: ", plTitle)
    print(f"Playlist contains of {plLength} videos")
    videoCounter = 0
    for videourl in playlist.video_urls[:3]:
        downloadVideo(videourl, plTitle)
        videoCounter+=1
        print("Progress: ", videoCounter, "/", plLength, " Videos")


# get link via argument 
# TODO: check if argument is empty: print error message "a link to video/playlist needs to be provided"
link = argv[1]
if isPlaylist(link):
    downloadPlaylist(link)
    print("Playlist Download successfull")
else:
    downloadVideo(link)
    print("Video Download successfull")