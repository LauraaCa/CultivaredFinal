import psycopg2
import os

LOCAL_DB_CONFIG = {
    "dbname": "cultivared",
    "user": "laura",
    "password": "12345",
    "host": "localhost",
    "port": "5432"
}

RENDER_INTERNAL_URL = "postgresql://laura:7amRTA1rXNjJEATgymzFyg2FEdY3IS91@dpg-d43t5rgdl3ps73a96iqg-a/cultivared_postgresql"

class Config:
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"postgresql://{LOCAL_DB_CONFIG['user']}:{LOCAL_DB_CONFIG['password']}@"
        f"{LOCAL_DB_CONFIG['host']}:{LOCAL_DB_CONFIG['port']}/{LOCAL_DB_CONFIG['dbname']}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "clave_secreta_segura")


# --- Función para obtener conexión manual con psycopg2 ---
def get_connection():
    try:
        # Usa DATABASE_URL si existe (Render), si no usa la local
        db_url = os.getenv("DATABASE_URL")
        if db_url:
            return psycopg2.connect(db_url)
        else:
            return psycopg2.connect(**LOCAL_DB_CONFIG)
    except Exception as e:
        print("❌ Error de conexión:", e)
        return None


