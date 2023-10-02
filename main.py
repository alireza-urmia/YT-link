from pytube import Playlist

playlist = Playlist('')

print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video_url in playlist.video_urls:
    print(video_url)