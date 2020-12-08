import json, os, re, sys
from termcolor import colored

def fix_characters(title):
  """
  Fixes title so that youtube-dl can output a
  passable filename. Does not support 
  non numeric or non a-Z characters. 
  """
  return re.sub('[^0-9a-zA-Z]+', ' ', title)

def append_videos(videos_info):
  """
  Used in load_video data to help extract the 
  correct info needed to download the video, 
  which is the videoId and title. 
  """
  videos = []
  for video in videos_info:
    if 'videoId' in video['id']:
      videos.append([str(video['id']['videoId']), fix_characters(video['snippet']['title'])])
  return videos

def load_video_data(fpath):
  """
  Reads yt data api json files to extract important 
  downloading data.
  """
  videos = []
  with open(fpath) as f:
    d1 = json.load(f)['items']
    videos += append_videos(d1)
  return videos

def get_excluded_videos():
  """
  Returns the set of videos that should be excluded from
  the download. Consists of filenames that have already
  been downloaded. 
  """
  excluded_list = open('exclude.txt', 'r')
  return set([line.strip() for line in excluded_list.readlines()])

def check_excluded_list(excluded_vids, title):
  """
  A check downloading the video to see if the video 
  belongs in the excluded list. 
  """
  if title + ".mkv" in excluded_vids or title + ".mp4" in excluded_vids or title + ".webm" in excluded_vids:
    return True
  return False

def download_videos(download_limit=6):
  """
  Downloads 6 videos at a time and outputs into the videos/ directory. 
  """
  videos = []
  for fname in os.listdir('yt_api_data'):
    videos += load_video_data(fname)
  vids_downloaded = 0
  excluded_vids = get_excluded_videos()
  for video_id, title in videos:
    if download_limit != 'all' and vids_downloaded == download_limit:
      break
    title = title.replace(' ', '_')
    mkv_path = "videos/" + title + ".mkv"
    mp4_path = "videos/" + title + ".mp4"
    download_fpath = "videos/" + title
    if not check_excluded_list(excluded_vids, title) and not os.path.isfile(mkv_path) and not os.path.isfile(mp4_path):
      print(colored(str(vids_downloaded + 1) + ": ", "yellow") + colored(video_id + " downloading: " + download_fpath, "green"))
      command_prefix = "youtube-dl -o " + download_fpath
      if video_id[0] == '-': 
        os.system(command_prefix + " -- " + video_id)
      else:
        os.system(command_prefix + " " + video_id)
      vids_downloaded += 1
    else:
      print(colored("skipping download: " + title + "with youtube_id: " + video_id, "yellow"))

def helper_text():
  print(colored("This program accepts 0-1 arguments, if 0 arguments are provided, then 6 videos will be downloaded. If 1 argument is provided, its value can be numeric, or the string all. Below there are 3 examples where the first downloads all, the second downloads 2, the third downloads 6", "yellow"))
  print(colored("    Example: python3 script.py all"))
  print(colored("    Example: python3 script.py 2"))
  print(colored("    Example: python3 script.py"))

if __name__ == "__main__":
  if len(sys.argv) == 1:
    download_videos(6)
    sys.exit()
  elif len(sys.argv) == 2:
    if sys.argv[1] == 'all':
      download_videos('all')
      sys.exit()
    elif sys.argv[1].isnumeric():
      download_videos(int(sys.argv[1]))
      sys.exit()
  helper_text()
  

