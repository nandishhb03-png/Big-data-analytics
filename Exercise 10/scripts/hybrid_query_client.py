#!/usr/bin/env python3

from cassandra.cluster import Cluster
from datetime import datetime, timedelta
import json

class HybridAnalyticsClient:

    def __init__(self):
        self.cluster = Cluster(['localhost'])
        self.session = self.cluster.connect('streaming_analytics')

    def get_realtime_stats(self):
        rows = self.session.execute("""
        SELECT * FROM hourly_stats
        LIMIT 24
        """)

        return [{
            'hour': r.hour,
            'total_plays': r.total_plays,
            'unique_users': r.unique_users
        } for r in rows]

    def get_batch_stats(self, date):
        rows = self.session.execute("""
        SELECT * FROM daily_aggregates
        WHERE date = %s
        """, (date,))

        return [{
            'date': r.date,
            'total_plays': r.total_plays,
            'top_song': r.top_song
        } for r in rows]

    def get_hybrid_insights(self):
        realtime = self.get_realtime_stats()

        yesterday = (
            datetime.now() - timedelta(days=1)
        ).strftime('%Y-%m-%d')

        batch = self.get_batch_stats(yesterday)

        return {
            'realtime': realtime,
            'batch': batch
        }

    def close(self):
        self.cluster.shutdown()


if __name__ == "__main__":
    client = HybridAnalyticsClient()

    try:
        insights = client.get_hybrid_insights()

        print("HYBRID ANALYTICS INSIGHTS")
        print("=" * 40)

        print(json.dumps(
            insights,
            indent=2,
            default=str
        ))

    finally:
        client.close()
