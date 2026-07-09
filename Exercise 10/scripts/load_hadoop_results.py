from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('streaming_analytics')

# Load daily aggregates
print("Loading daily aggregates...")

with open('output/daily_aggregates/part-00000') as f:
    for line in f:
        if not line.strip():
            continue

        parts = line.strip().split('\t')

        if len(parts) >= 6:
            date, total_plays, unique_users, avg_duration, top_song, top_artist = parts

            session.execute("""
            INSERT INTO daily_aggregates
            (date, total_plays, unique_users, avg_duration, top_song, top_artist)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                date,
                int(total_plays),
                int(unique_users),
                float(avg_duration),
                top_song,
                top_artist
            ))

# Load top songs
print("Loading top songs...")

with open('output/top_songs/part-00000') as f:
    for line in f:
        if not line.strip():
            continue

        parts = line.strip().split('\t')

        if len(parts) >= 5:
            date, rank, song, artist, count = parts

            session.execute("""
            INSERT INTO top_songs_daily
            (date, rank, song, artist, play_count)
            VALUES (%s, %s, %s, %s, %s)
            """, (
                date,
                int(rank),
                song,
                artist,
                int(count)
            ))

print("Results loaded into Cassandra!")

cluster.shutdown()
