from pytube import YouTube
from pytube import Playlist
from sys import argv
import os

# checks which OS the script is being run on (currently obsolete)
def isWindows():
    if os.name == "nt":
        return True
    return False

# return Downloadpath depending on OS 
def getDownloadPath():
    homePath = os.path.expanduser("~")
    desktopPath = os.path.join(homePath, "Desktop")
    downloadFolderPath = os.path.join(desktopPath, "ytDownloads")
    if not os.path.exists(downloadFolderPath):
        os.makedirs(downloadFolderPath)
        print(f"Folder #{downloadFolderPath} created successfully")
    return downloadFolderPath

# checks if provided link actually links to a YT playlist or video
def validYTLink(link):
    if link.startswith("https://www.youtube.com/") | link.startswith("https://youtu.be/"):
        return True
    return False

# TODO: check automatically if link provided is a playlist or a video and proceed accordingly
def isPlaylist(link):
    if link.startswith("https://www.youtube.com/playlist?list="):
        return True
    return False

# downloads single video
def downloadVideo(videoLink, playlistFolder=None):
    downloadPath = getDownloadPath()
    if playlistFolder is not None:
        downloadPath = os.path.join(downloadPath, playlistFolder)
        if not os.path.exists(downloadPath):
            os.makedirs(downloadPath)
            print(f"Folder #{downloadPath} created successfully")
    video = YouTube(videoLink)
    print("Downloading Video: ", video.title, " by ", video.author)
    downloader = video.streams.get_highest_resolution()
    downloader.download(downloadPath)

# downloads all videos in a playlist
def downloadPlaylist(playlistLink):
    playlist = Playlist(playlistLink)
    plTitle = playlist.title
    plLength = playlist.length
    plOwner = playlist.owner
    print()
    print("Downloading Playlist: ", plTitle, " by ", plOwner, " (",plLength, "videos )")
    print()
    videoCounter = 0
    for videourl in playlist.video_urls:
        downloadVideo(videourl, plTitle)
        videoCounter+=1
        print("Progress: ", videoCounter, "/", plLength, " Videos")
        print()



## Script Start ##
print()
print("Please provide a valid Youtube Link for downloading")
print("This tool can download single videos or playlists (playlist has to be public)")

# Repeated User Input prompt till valid Link is entered
inputValid = False
ytLink = ""
while not inputValid:
    user_input = input("Enter Youtube Link: ")
    if user_input == "":
        print()
        print("Exiting Tool")
        print()
        break
    elif validYTLink(user_input):
        ytLink = user_input
        inputValid = True
        break
    else:
        print("Entered Link is not a valid URL.")
        print("Please enter a valid Link or Press Enter to exit")
        print()

# depending if video / playlist calls appropiate download function
if inputValid:
    if isPlaylist(ytLink):
        downloadPlaylist(ytLink)
        print()
        print("Playlist Download finished")
        print()
    else:
        downloadVideo(ytLink)
        print()
        print("Video Download finished")
        print()