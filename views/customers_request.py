import sqlite3
# import json
from models import Customer

def get_all_customers():
    """get all customers"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            customer = Customer(row['id'], row['name'], row['address'])

            customers.append(customer.__dict__)

    return customers

def get_single_customer(id):
    """get single customer"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'])

    return customer.__dict__

def get_customer_by_email(email):
    """getting customer by email"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
        c.id,
        c.name,
        c.address,
        c.email,
        c.password
    FROM customer c
    WHERE c.email = ?
    """, ( email, ))

    customers = []
    dataset = db_cursor.fetchall()

    for row in dataset:
        customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
        customers.append(customer.__dict__)

    return customers
