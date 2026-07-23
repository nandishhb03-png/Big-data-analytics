CREATE KEYSPACE IF NOT EXISTS sparkify
WITH REPLICATION = {
'class':'SimpleStrategy',
'replication_factor':1
};

USE sparkify;

CREATE TABLE song_info_by_session (
    artist TEXT,
    song TEXT,
    length DECIMAL,
    session_id INT,
    item_in_session INT,
    PRIMARY KEY (session_id, item_in_session)
);

CREATE TABLE song_playing_history_by_user (
    artist TEXT,
    song TEXT,
    first_name TEXT,
    last_name TEXT,
    session_id INT,
    item_in_session INT,
    user_id INT,
    PRIMARY KEY ((user_id, session_id), item_in_session)
) WITH CLUSTERING ORDER BY (item_in_session DESC);

CREATE TABLE who_listened_to_song (
    user_id INT,
    first_name TEXT,
    last_name TEXT,
    song TEXT,
    PRIMARY KEY (song, user_id)
);
