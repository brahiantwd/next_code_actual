import os

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv():
        return False

try:
    from pymongo import MongoClient
except ImportError:
    MongoClient = None


load_dotenv()

URI = os.getenv("MONGODB_URI")


class _ColeccionBarberosLocal:
    """Colección local vacía: permite que las vistas funcionen sin MongoDB."""

    def find(self, *args, **kwargs):
        return []


if MongoClient is not None:
    try:
        cliente_mongo = MongoClient(
            URI or "mongodb://127.0.0.1:27017",
            serverSelectionTimeoutMS=1500,
        )
        db = cliente_mongo["barberiaNextCode"]
        barberos = db["barberos"]
        clientes = db["clientes"]
        servicios = db["servicios"]
        horarios = db["horarios"]
        citas = db["citas"]
        productos = db["productos"]
        notificaciones = db["notificaciones"]
    except Exception:
        barberos = _ColeccionBarberosLocal()
        clientes = servicios = horarios = citas = productos = notificaciones = _ColeccionBarberosLocal()
else:
    barberos = _ColeccionBarberosLocal()
    clientes = servicios = horarios = citas = productos = notificaciones = _ColeccionBarberosLocal()
