# download_videos_using_links
Scraped all video id's from a specific channel using youtube-dl, Youtube Data API, a cloud server, and python. 

The purpose of downloading the videos from this channel was to make sure the channel would not be taken down given that the account was given warning that it was going to be no longer accessible. The purpose of usage of the cloud server was to be able to download all videos without receiving the 429 HTTP error from Youtube's servers by using the youtube-dl command tool. 

Transfered files on the cloud via scp and ssh to run the script, used python3.8, used screen to ensure script process could easily be checked.

The exclude.txt file was later added due to space limitations on the cloud server.

###
INSTALLATION
###
Need to install termcolor:
	pip3 install termcolor
Need to install youtube-dl to wherever you are downloading:
	youtube-dl

###
USAGE
###

You need a videos/ directory in order to properly download the videos. 

Due to memory limitations for the cloud server used to originally use this script, the script downloads only 6 videos at a time. The exclude.txt file is used to exclude video titles that have already been downloaded. Each line is the name of the file that is already downloaded. The code will skip downloading these videos. 

###
SERVER DOWNLOADING
###

Example:
scp video-server:'download_videos_using_links/*.{mkv,mp4}' .
video-server is the alias and all .mkv and .mp4 extensions are being downloaded to the current directory