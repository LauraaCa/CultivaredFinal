import psycopg2
import os

# Configuración de conexión a la base de datos
DB_CONFIG = {
    "dbname": "cultivared",
    "user": "laura",
    "password": "12345",
    "host": "localhost",
    "port": "5432"
}

class Config:
    # Construimos la URL a partir del diccionario DB_CONFIG
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "clave_secreta_segura")


# Función para obtener conexión directa con psycopg2
def get_connection():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print("Error de conexión:", e)
        return None


# Probar conexión directa (opcional)
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print("✅ Conectado a:", db_version)
        conn.close()
