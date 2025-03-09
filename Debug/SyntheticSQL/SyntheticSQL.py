import random
import pandas as pd

# Define SQL file name
sql_filename = "new_robot_data.sql"

# Generate synthetic robot log data
data = []
for _ in range(1000):  # Ensure exactly 1000 entries are generated
    serial_number = f"X2000-{random.randint(1000, 9999)}"
    operation_mode = random.choice(["Idle", "Active", "Maintenance", "Error"])
    task_completed = random.choice(["Patrol", "Surveillance", "Assembly", "Inspection", "Transport", "Charging"])
    battery_level = random.randint(0, 100)
    temperature = round(random.uniform(20.0, 75.0), 2)  # °C
    error_code = random.choice(["ERR-101", "ERR-202", "ERR-303", None, None, None])  # Some NULL values
    last_maintenance = pd.Timestamp("2024-01-01") + pd.to_timedelta(random.randint(0, 180), unit="D")
    location = random.choice(["Factory A", "Warehouse B", "HQ Lab", "Production Line", "Testing Zone"])
    log_timestamp = pd.Timestamp("2025-01-01") + pd.to_timedelta(random.randint(0, 30), unit="D")

    data.append((serial_number, operation_mode, task_completed, battery_level, temperature, error_code, 
                 last_maintenance.strftime("%Y-%m-%d"), location, log_timestamp.strftime("%Y-%m-%d %H:%M:%S")))

print(f"Generated {len(data)} rows.")  # Debugging line to confirm 1000 rows generated

# Generate SQL file content
with open(sql_filename, "w", encoding="utf-8") as file:
    file.write("DROP DATABASE IF EXISTS NewSyntheticDB;\n")  # Ensures fresh start
    file.write("CREATE DATABASE IF NOT EXISTS NewSyntheticDB;\n")
    file.write("USE NewSyntheticDB;\n\n")

    file.write("""
    CREATE TABLE IF NOT EXISTS NewRobotLogs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        serial_number VARCHAR(20),
        operation_mode ENUM('Idle', 'Active', 'Maintenance', 'Error'),
        task_completed VARCHAR(100),
        battery_level INT,
        temperature DECIMAL(5,2),
        error_code VARCHAR(10) NULL,
        last_maintenance DATE,
        location VARCHAR(50),
        log_timestamp DATETIME
    );\n\n
    """)

    file.write("INSERT INTO NewRobotLogs (serial_number, operation_mode, task_completed, battery_level, temperature, error_code, last_maintenance, location, log_timestamp) VALUES\n")

    for i, row in enumerate(data):
        error_value = "NULL" if row[5] is None else f"'{row[5]}'"
        line = f"('{row[0]}', '{row[1]}', '{row[2]}', {row[3]}, {row[4]}, {error_value}, '{row[6]}', '{row[7]}', '{row[8]}')"
        
        if i < len(data) - 1:
            file.write(line + ",\n")  # Add comma for all except the last row
        else:
            file.write(line + ";\n")  # Last row ends with a semicolon

    file.flush()  # Ensure all data is written before closing

print(f"✅ SQL file '{sql_filename}' has been created with {len(data)} rows!")
