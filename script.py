import json, os, re


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

def download_videos():
  videos = []
  videos += load_video_data("videos1.json") + load_video_data("videos2.json")
  for video_id, title in videos:
    print("youtube-dl -o " + title.replace(' ', '_').replace('(', '') + " " + video_id)
    mkv_path = "videos/" + title + ".mkv"
    mp4_path = "videos/" + title + ".mp4"
    download_fpath = "videos/" + title.replace(' ', '_')
    if not os.path.isfile(mkv_path) and not os.path.isfile(mp4_path):
      print(video_id + " downloading: " + download_fpath)
      os.system("youtube-dl -o " + download_fpath + " " + video_id)
    else:
      print("skipping download: " + title + "with youtube_id: " + video_id)

if __name__ == "__main__":
  download_videos()

