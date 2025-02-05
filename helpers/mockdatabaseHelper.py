import sqlite3
import json
import os

class MockDatabaseHelper:
    def __init__(self, mock_data_file: str = "mock_data/mock_patients.json"):
        """Initialize an in-memory SQLite database and load mock patient data."""
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        if os.path.exists(mock_data_file):
            self.load_mock_data(mock_data_file)

    def execute_query(self, query, params=None):
        """Execute an SQL query with optional parameters."""
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except sqlite3.Error as err:
            print(f"SQLite Error: {err}")
            self.connection.rollback()

    def fetch_all(self, query, params=None):
        """Fetch all results from a query."""
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        """Fetch a single row from a query."""
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def load_mock_data(self, mock_data_file):
        """Load mock patient data from a JSON file."""
        with open(mock_data_file, "r") as file:
            data = json.load(file)

        self.execute_query("""
            CREATE TABLE IF NOT EXISTS patients (
                id TEXT PRIMARY KEY,
                name TEXT,
                nhs_number TEXT,
                dob TEXT,
                address TEXT
            )
        """)

        for patient in data["patients"]:
            self.execute_query("""
                INSERT INTO patients (id, name, nhs_number, dob, address)
                VALUES (?, ?, ?, ?, ?)
            """, (patient["id"], patient["name"], patient["nhs_number"], patient["dob"], patient["address"]))

    def close_connection(self):
        """Close the SQLite connection."""
        self.cursor.close()
        self.connection.close()
