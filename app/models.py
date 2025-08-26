import sqlite3
from datetime import datetime

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Create devices table
    c.execute('''CREATE TABLE IF NOT EXISTS devices
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 device_type TEXT NOT NULL,
                 topic TEXT NOT NULL UNIQUE,
                 state TEXT DEFAULT 'off',
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Create automation tasks table
    c.execute('''CREATE TABLE IF NOT EXISTS automations
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 device_id INTEGER,
                 action TEXT NOT NULL,
                 schedule_type TEXT NOT NULL,
                 time_value TEXT,
                 days TEXT,
                 active BOOLEAN DEFAULT TRUE,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 FOREIGN KEY (device_id) REFERENCES devices (id))''')
    
    # Check if devices table is empty
    c.execute('SELECT COUNT(*) FROM devices')
    count = c.fetchone()[0]
    
    # Insert some sample devices only if table is empty
    if count == 0:
        sample_devices = [
            ('Living Room Light', 'light', 'home/livingroom/light'),
            ('Kitchen Light', 'light', 'home/kitchen/light'),
            ('Bedroom Light', 'light', 'home/bedroom/light'),
            ('Thermostat', 'thermostat', 'home/thermostat'),
        ]
        
        c.executemany('INSERT INTO devices (name, device_type, topic) VALUES (?, ?, ?)', sample_devices)
        print("Sample devices added to database.")
    
    conn.commit()
    conn.close()

def get_db_connection(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn