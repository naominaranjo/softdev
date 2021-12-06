# CircleTable - Christopher Liu, Yusuf Elsharawy, Naomi Naranjo
# SoftDev
# K16 -- All About Database
# 2021-10-20

import csv
import sqlite3  # Enable control of an sqlite database

DB_FILE = "discobandit.db"


def read_data(filename: str) -> list:
    """Reads data from a given CSV file and returns a list of dicts for
    each row."""

    table_data = []
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table_data.append(row)

    return table_data


def main():
    """Imports data from courses.csv and students.csv and puts the data into
    SQL tables."""
    db = sqlite3.connect(DB_FILE)  # Open if file exists, otherwise create
    c = db.cursor()  # Facilitate db ops -- use cursor to trigger db events

    # ==========================================================

    # Read data from courses.csv and students.csv
    courses = read_data("courses.csv")
    students = read_data("students.csv")

    # Remove existing tables if exists
    c.execute("DROP TABLE IF EXISTS courses")
    c.execute("DROP TABLE IF EXISTS students")

    # Create new SQL tables
    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
    c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)")

    # Populate SQL tables
    c.executemany("INSERT INTO courses VALUES (:code, :mark, :id)", courses)
    c.executemany("INSERT INTO students VALUES (:name, :age, :id)", students)

    # ==========================================================

    db.commit()  # Save changes
    db.close()  # Close database


if __name__ == "__main__":
    main()
