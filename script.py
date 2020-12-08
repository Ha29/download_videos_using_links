import json, os, re
from termcolor import colored

def fix_characters(title):
  return re.sub('[^0-9a-zA-Z]+', ' ', title)

def append_videos(videos_info):
  videos = []
  for video in videos_info:
    if 'videoId' in video['id']:
      videos.append([str(video['id']['videoId']), fix_characters(video['snippet']['title'])])
  return videos

def load_video_data(fpath):
  videos = []
  with open(fpath) as f:
    d1 = json.load(f)['items']
    videos += append_videos(d1)
  return videos

def in_excluded_list(title):
  excluded_list = open('exclude.txt', 'r')
  vids = [line.strip() for line in excluded_list.readlines()]
  if title + ".mkv" in vids or title + ".mp4" in vids:
    return True
  return False

def download_videos():
  videos = []
  videos += load_video_data("videos1.json") + load_video_data("videos2.json")
  vids_downloaded = 0
  for video_id, title in videos:
    if vids_downloaded > 5:
        break
    title = title.replace(' ', '_')
    mkv_path = "videos/" + title + ".mkv"
    mp4_path = "videos/" + title + ".mp4"
    download_fpath = "videos/" + title
    if not in_excluded_list(title) and not os.path.isfile(mkv_path) and not os.path.isfile(mp4_path):
      print(colored(video_id + " downloading: " + download_fpath, "green"))
      command_prefix = "youtube-dl -o " + download_fpath
      if video_id[0] == '-': 
        os.system(command_prefix + " -- " + video_id)
      else:
        os.system(command_prefix + " " + video_id)
      vids_downloaded += 1
    else:
      print(colored("skipping download: " + title + "with youtube_id: " + video_id, "yellow"))

if __name__ == "__main__":
  download_videos()

