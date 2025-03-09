import psycopg2

# ✅ Define PostgreSQL Connection
DB_CONFIG = {
    "dbname": "Robot",
    "user": "postgres",       # Change this
    "password": "Kaikuzu1@",  # Change this
    "host": "localhost"
}

def test_postgres_connection():
    """Test PostgreSQL connection and fetch data"""
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT * from newrobotlogs limit 5")
        tables = cursor.fetchall()
        print("\n✅ Connected to PostgreSQL!")
        print("📌 Available Tables:", tables)
        cursor.close()
        connection.close()
    except Exception as e:
        print("\n❌ PostgreSQL Connection Failed:", str(e))

# ✅ Run Connection Test
test_postgres_connection()
