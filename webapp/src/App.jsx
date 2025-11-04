import React, { useEffect, useState } from "react";
import WebApp from "@twa-dev/sdk";
import { motion } from "framer-motion";

export default function App() {
  const [user, setUser] = useState(null);
  const tg = window.Telegram.WebApp;
  const user = tg.initDataUnsafe?.user;

  useEffect(() => {
    WebApp.ready();
    const tgUser = WebApp.initDataUnsafe?.user;
    if (tgUser) {
      setUser(tgUser);
    }
  }, []);

  return (
    <div
      className="min-h-screen flex flex-col items-center justify-center text-white"
      style={{
        background: "linear-gradient(to bottom, #3b0a45, #14001e)",
        fontFamily: "sans-serif",
      }}
    >
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="text-center"
      >
        <h1 className="text-4xl font-bold mb-4">🕹️ CARD BATTLE</h1>
        <p className="text-lg mb-6">Собери героев и сразись в битве!</p>

        {user ? (
          <p className="text-xl mb-6">👤 Привет, {user.first_name}!</p>
        ) : (
          <p className="text-gray-400 mb-6">Загрузка профиля...</p>
        )}

        <div className="flex flex-col gap-3">
          <button
            onClick={() => alert("Игра ещё не началась!")}
            className="bg-green-600 hover:bg-green-700 px-6 py-3 rounded-xl text-lg font-semibold"
          >
            ▶ Начать игру
          </button>
          <button
            onClick={() => alert("Раздел героев скоро будет!")}
            className="bg-purple-600 hover:bg-purple-700 px-6 py-3 rounded-xl text-lg font-semibold"
          >
            💎 Мои герои
          </button>
        </div>
      </motion.div>
    </div>
  );
}
