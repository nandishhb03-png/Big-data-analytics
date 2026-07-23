# Exercise 8 - Cassandra Database using Docker

## Objective

To install and run Apache Cassandra using Docker on Ubuntu WSL and perform database operations using Cassandra Query Language (CQL).

## Files Included

* `docker-compose.yml` - Docker configuration file for Cassandra container.
* `setup_exercise.cql` - CQL script containing keyspace creation, table creation, data insertion, and queries.

## Keyspace Created

* `sparkify`

## Tables Created

1. `song_info_by_session`
2. `song_playing_history_by_user`
3. `who_listened_to_song`

## Operations Performed

* Created keyspace and tables.
* Inserted sample records.
* Retrieved songs played in a session.
* Retrieved songs played by a user in a session.
* Retrieved users who listened to a specific song.

## Technologies Used

* Ubuntu WSL
* Docker
* Apache Cassandra
* CQL
* Git and GitHub
