from flask import Flask
from config import Config
from models import db

try:
    from routes import autenticacion, admin, vendedor, comprador, gestor
except ImportError:
    print("⚠️ No se pudieron importar todas las rutas. Verifica la carpeta 'routes'.")

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)

with app.app_context():
    from models import Usuarios, Producto, Transaccion, Carrito, ItemsCarrito, Pedido, ItemPedido
    db.create_all()
    print("✅ Tablas creadas o actualizadas en la base de datos.")


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 - Página no encontrada</h1>", 404

try:
    app.register_blueprint(autenticacion.main, url_prefix='/CULTIVARED')
    app.register_blueprint(admin.main, url_prefix='/ADMINISTRADOR')
    app.register_blueprint(vendedor.main, url_prefix='/VENDEDOR')
    app.register_blueprint(comprador.main, url_prefix='/COMPRADOR')
    app.register_blueprint(gestor.main, url_prefix='/GESTOR')
    print("✅ Blueprints registrados correctamente.")
except Exception as e:
    print("⚠️ Error al registrar blueprints:", e)


if __name__ == '__main__': 
    app.run(host="0.0.0.0"  , debug=True)
