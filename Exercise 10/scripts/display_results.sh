#!/bin/bash

echo "========================================="
echo "HADOOP + CASSANDRA ANALYTICS RESULTS"
echo "========================================="

echo ""
echo "REAL-TIME STATS"
echo "-----------------------------------------"

docker exec cassandra cqlsh -e "
USE streaming_analytics;
SELECT * FROM hourly_stats LIMIT 5;
"

echo ""
echo "TOP SONGS"
echo "-----------------------------------------"

docker exec cassandra cqlsh -e "
USE streaming_analytics;
SELECT * FROM top_songs_daily LIMIT 10;
"

echo ""
echo "HYBRID INSIGHTS"
echo "-----------------------------------------"

python3 scripts/hybrid_query_client.py
