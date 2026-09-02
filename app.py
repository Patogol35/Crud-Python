import os
import sqlite3

from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

# Permitir conexiones desde React
CORS(app)

DATABASE = "database.db"


# ==========================================
# CONEXIÓN A SQLITE
# ==========================================

def conectar_db():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion


# ==========================================
# CREAR TABLA
# ==========================================

def crear_tabla():
    conexion = conectar_db()

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


crear_tabla()


# ==========================================
# RUTA PRINCIPAL
# ==========================================

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API CRUD funcionando correctamente"
    })


# ==========================================
# GET - LISTAR PRODUCTOS
# ==========================================

@app.route("/productos", methods=["GET"])
def obtener_productos():

    conexion = conectar_db()

    productos = conexion.execute(
        "SELECT * FROM productos ORDER BY id DESC"
    ).fetchall()

    conexion.close()

    return jsonify([dict(producto) for producto in productos])


# ==========================================
# GET - OBTENER UN PRODUCTO
# ==========================================

@app.route("/productos/<int:id>", methods=["GET"])
def obtener_producto(id):

    conexion = conectar_db()

    producto = conexion.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id,)
    ).fetchone()

    conexion.close()

    if producto is None:
        return jsonify({
            "error": "Producto no encontrado"
        }), 404

    return jsonify(dict(producto))


# ==========================================
# POST - CREAR PRODUCTO
# ==========================================

@app.route("/productos", methods=["POST"])
def crear_producto():

    datos = request.get_json()

    if not datos:
        return jsonify({
            "error": "No se enviaron datos"
        }), 400

    nombre = datos.get("nombre")
    descripcion = datos.get("descripcion")
    precio = datos.get("precio")
    categoria = datos.get("categoria")

    if not all([
        nombre,
        descripcion,
        precio is not None,
        categoria
    ]):
        return jsonify({
            "error": "Todos los campos son obligatorios"
        }), 400

    conexion = conectar_db()

    cursor = conexion.execute(
        """
        INSERT INTO productos
        (nombre, descripcion, precio, categoria)
        VALUES (?, ?, ?, ?)
        """,
        (
            nombre,
            descripcion,
            precio,
            categoria
        )
    )

    conexion.commit()

    nuevo_id = cursor.lastrowid

    conexion.close()

    return jsonify({
        "mensaje": "Producto creado correctamente",
        "id": nuevo_id
    }), 201


# ==========================================
# PUT - ACTUALIZAR PRODUCTO
# ==========================================

@app.route("/productos/<int:id>", methods=["PUT"])
def actualizar_producto(id):

    datos = request.get_json()

    if not datos:
        return jsonify({
            "error": "No se enviaron datos"
        }), 400

    nombre = datos.get("nombre")
    descripcion = datos.get("descripcion")
    precio = datos.get("precio")
    categoria = datos.get("categoria")

    if not all([
        nombre,
        descripcion,
        precio is not None,
        categoria
    ]):
        return jsonify({
            "error": "Todos los campos son obligatorios"
        }), 400

    conexion = conectar_db()

    producto = conexion.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id,)
    ).fetchone()

    if producto is None:
        conexion.close()

        return jsonify({
            "error": "Producto no encontrado"
        }), 404

    conexion.execute(
        """
        UPDATE productos
        SET nombre = ?,
            descripcion = ?,
            precio = ?,
            categoria = ?
        WHERE id = ?
        """,
        (
            nombre,
            descripcion,
            precio,
            categoria,
            id
        )
    )

    conexion.commit()
    conexion.close()

    return jsonify({
        "mensaje": "Producto actualizado correctamente"
    })


# ==========================================
# DELETE - ELIMINAR PRODUCTO
# ==========================================

@app.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):

    conexion = conectar_db()

    producto = conexion.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id,)
    ).fetchone()

    if producto is None:
        conexion.close()

        return jsonify({
            "error": "Producto no encontrado"
        }), 404

    conexion.execute(
        "DELETE FROM productos WHERE id = ?",
        (id,)
    )

    conexion.commit()
    conexion.close()

    return jsonify({
        "mensaje": "Producto eliminado correctamente"
    })


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
