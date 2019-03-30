# YouTube-music-video-5M [BETA]

by Keunwoo Choi

This is a beta release, 02 Aug 2017.

## Statistics

  * 5,119,955 video ID's in youtube in 20 text files.
  * file name: `"youtube_video_ids_{:0d}_{}.txt".format(file_index, n_ids_this_file)`
  * Entries of the files are either
    - `"\n"`
    - `"# new artist:\t{}\t{}\n".format(artist_name, artist_spotify_id)`
    - `"{}\n".format(youtube_video_id)` 
  * E.g., the first 10 lines of `youtube_video_ids_00_206947.txt` is...
```

# new artist: Drake 3TVXtAsR1Inumwj472S9r4

3t195yz9xCc
VkXjvHfP3MM
7LnBvuzjpr4
1Ldzm7KGECI
HL1UzIK-flA
3XR5mhXtpXw
WsPfSXJaelk

```

  * Files and entries are sorted by some sort of artist popularity.
  * Each text file includee video ID's of 500 artists
  * Overall, they are from approximately 10K artists.

## Crawlling by how?
  * I used YouTube search API with the keywords of `"{} official music video".format(artist_name)`. Hopefully these are more of official music videos with a professional quality rather than amateur ones.

## Utilities
  * [pytube](https://github.com/nficano/pytube)
  * [Spotify API](https://developer.spotify.com/web-api/)

## Note
  * Due to the law, no further information/feature will be added either from Youtube or Spotify.
  * Some more stats will be added, e.g., the number of artist.

