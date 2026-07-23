USE streaming_analytics;

-- CURRENT TOP SONGS
SELECT * FROM current_top_songs
WHERE date = toDate(now());

-- HOURLY STATS
SELECT * FROM hourly_stats;

-- USER HISTORY
SELECT * FROM user_listening_history
WHERE user_id = 1001
LIMIT 5;

-- SESSION ANALYSIS
SELECT * FROM user_sessions
WHERE user_id = 1001;

-- DAILY AGGREGATES
SELECT * FROM daily_aggregates;

-- TOP SONGS
SELECT * FROM top_songs_daily;
