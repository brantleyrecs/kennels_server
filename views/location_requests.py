import sqlite3
# import json
from models import Location

def get_all_locations():
    """get all locations"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            location = Location(row['id'], row["name"], row["address"])
            locations.append(location.__dict__)

    return locations

def get_single_location(id):
    """get single location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        location = Location(data['id'], data['name'], data['address'])

    return location.__dict__
