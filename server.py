from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DATA_FILE = "players.json"

# 📂 Загрузка/сохранение игроков
def load_players():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_players(players):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(players, f, indent=2, ensure_ascii=False)

# ⚡ Роут проверки
@app.route("/")
def home():
    return jsonify({"message": "Card Battle Server работает ✅"})

# 🧍‍♂️ Логин / создание игрока
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    player_id = str(data.get("id"))
    username = data.get("username", "Игрок")

    players = load_players()

    if player_id not in players:
        players[player_id] = {
            "username": username,
            "coins": 100,
            "heroes": [
                {"name": "Новобранец", "emoji": "🧙‍♂️", "skin": "default"}
            ]
        }
        save_players(players)
        return jsonify({"message": "🎁 Новый игрок создан!", "player": players[player_id]})
    else:
        return jsonify({"message": "✅ Добро пожаловать обратно!", "player": players[player_id]})

# 🧠 Получение данных игрока
@app.route("/api/player/<int:player_id>")
def get_player(player_id):
    players = load_players()
    if str(player_id) not in players:
        return jsonify({"error": "Игрок не найден"}), 404
    return jsonify(players[str(player_id)])

# 🚀 Запуск сервера
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
