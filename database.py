import sqlite3
import json
import os

db_path = os.path.join(os.path.dirname(__file__), "claracare.db")

def get_db():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT DEFAULT 'NJ',
            zip_code TEXT NOT NULL,
            lat REAL NOT NULL,
            lng REAL NOT NULL,
            phone TEXT,
            website TEXT,
            services TEXT,
            languages TEXT,
            hours TEXT,
            appointment_required INTEGER DEFAULT 0,
            sliding_scale INTEGER DEFAULT 0,
            notes TEXT
        )
    """)

    conn.commit()
    conn.close()