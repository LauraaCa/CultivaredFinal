import psycopg2
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env (solo útil localmente)
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    if not SQLALCHEMY_DATABASE_URI:
        print("⚠️ No se encontró DATABASE_URL — usa tu .env o variable de entorno.")
    elif "sslmode" not in SQLALCHEMY_DATABASE_URI:
        # Render requiere SSL en PostgreSQL
        SQLALCHEMY_DATABASE_URI += "?sslmode=require"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "clave_secreta_segura")


def get_connection():
    try:
        db_url = os.getenv("DATABASE_URL")
        if db_url:
            return psycopg2.connect(db_url, sslmode="require")
        else:
            print("❌ No se encontró DATABASE_URL.")
    except Exception as e:
        print("❌ Error de conexión:", e)
        return None


# --- Prueba manual (solo local) ---
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            print("✅ Conectado a:", cur.fetchone())
        conn.close()
