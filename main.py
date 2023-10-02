from pytube import Playlist


# Add target playlist link between quotes
playlist = Playlist('https://youtube.com/playlist?list=PLLRM7ROnmA9H_8wqcxoKTMU5gZE6BOyhm&si=_VR1h4SER3JXhW47')


# Save episodes links of playlist to text file
with open('episodes_urls.txt', 'w') as f:
    f.write('number of videos exist on playlist: ' + str(len(playlist.video_urls)) + '\n' + '\n')
    for video_url in playlist.video_urls:
        f.write(video_url + '\n')