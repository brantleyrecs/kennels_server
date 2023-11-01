import sqlite3
# import json
from models import (Location, Animal, Employee)

def get_all_locations():
    """get all locations"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
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
            l.id,
            l.name,
            l.address,
            e.name,
            e.address,
            e.location_id,
            a.name,
            a.status,
            a.breed,
            a.customer_id,
            a.location_id
        FROM location l
        JOIN employee e
            ON e.location_id = l.id
        JOIN animal a
            ON a.location_id = l.id
        WHERE l.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        location = Location(data['id'], data['name'], data['address'])

        employee = Employee(data['id'], data['name'],
                                data['address'], data['location_id'])

        location.employee = employee.__dict__

        animal = Animal(data['id'], data['name'],
                            data['status'], data['breed'],
                            data['customer_id'], data['location_id'])
        location.animal = animal.__dict__
    return location.__dict__

def delete_location(id):
    """delete location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))

