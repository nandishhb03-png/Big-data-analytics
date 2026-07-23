#!/usr/bin/env python3

import sys
from collections import defaultdict

def process_date_songs(date_songs):
    """Process songs for a specific date and output top 100"""

    date = date_songs[0][0]

    songs_data = defaultdict(
        lambda: {'artist': '', 'count': 0}
    )

    for _, data in date_songs:
        song, artist_count = data.split(',', 1)
        artist, count = artist_count.split(',')

        count = int(count)

        if songs_data[song]['artist'] == '':
            songs_data[song]['artist'] = artist

        songs_data[song]['count'] += count

    sorted_songs = sorted(
        [
            (song,
             data['artist'],
             data['count'])
            for song, data in songs_data.items()
        ],
        key=lambda x: x[2],
        reverse=True
    )[:100]

    for rank, (song, artist, count) in enumerate(sorted_songs, 1):
        print(
            f"{date}\t"
            f"{rank}\t"
            f"{song}\t"
            f"{artist}\t"
            f"{count}"
        )


current_date = None
current_data = []

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, value = line.split('\t', 1)

        date_song = key
        artist_count = value

        date, song = date_song.split('_', 1)

        if current_date is None:
            current_date = date

        if date != current_date:
            process_date_songs(current_data)
            current_date = date
            current_data = []

        current_data.append(
            (
                date,
                f"{song},{artist_count}"
            )
        )

    except Exception:
        continue

if current_data:
    process_date_songs(current_data)
