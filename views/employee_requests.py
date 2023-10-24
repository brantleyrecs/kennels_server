import sqlite3
# import json
from models import Employee

def get_all_employees():
    """get all employees"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
            a.location_id
        FROM employee a
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return employees

def get_single_employee(id):
    """get single employee"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

    return employee.__dict__

def get_employee_by_location(location_id):
    """getting employee by location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    db_cursor.execute("""
        SELECT
           a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.location_id = ?
        """, ( location_id, ))

    employees = []
    dataset = db_cursor.fetchall()

    for row in dataset:
        employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
        employees.append(employee.__dict__)

    return employees
