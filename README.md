# download_videos_using_links
Scraped all video id's from a specific channel using youtube-dl, Youtube Data API, a cloud server, and python. 

The purpose of downloading the videos from this channel was to make sure the channel would not be taken down given that the account was given warning that it was going to be no longer accessible. The purpose of usage of the cloud server was to be able to download all videos without receiving the 429 HTTP error from Youtube's servers by using the youtube-dl command tool. 

Transfered files on the cloud via scp and ssh to run the script, used python3.8, used screen to ensure script process could easily be checked.

The exclude.txt file was later added due to space limitations on the cloud server.

###
INSTALLATION
###

pip3 install termcolor