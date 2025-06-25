from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='password',
            database='testdb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages")
        rows = cursor.fetchall()
        output = "<h1>Messages from MySQL:</h1>"
        for row in rows:
            output += f"<p>{row[0]}</p>"
        return output
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
