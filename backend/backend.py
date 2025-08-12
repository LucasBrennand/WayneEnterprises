from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="sistema_login"
    )

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify({"success": True, "message": "Login válido"})
    else:
        return jsonify({"success": False, "message": "Usuário ou senha incorretos"}), 401

if __name__ == "__main__":
    app.run(debug=True)
