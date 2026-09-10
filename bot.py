import os
import requests
import time

TOKEN = os.environ.get("8750412059:AAHLIoUxvz0aEQSyMMCeØM
tnPIsCTjR679A")

if not TOKEN:
    raise Exception("8750412059:AAHLIoUxvz0aEQSyMMCeØM
tnPIsCTjR679A")

URL = f"https://api.telegram.org/bot{TOKEN}"

offset = None

print("Bot iniciado")

while True:
    try:
        params = {"timeout": 20}
        if offset is not None:
            params["offset"] = offset

        response = requests.get(
            f"{URL}/getUpdates",
            params=params,
            timeout=30
        )

        data = response.json()

        for update in data.get("result", []):
            offset = update["update_id"] + 1

            message = update.get("message")
            if not message:
                continue

            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            if text == "/start":
                requests.post(
                    f"{URL}/sendMessage",
                    data={
                        "chat_id": chat_id,
                        "text": "🤖 Bot Surebet conectado correctamente.\n\nCuando conectemos OddsPapi voy a buscar oportunidades entre Betano y Bet365."
                    }
                )

            elif text == "/id":
                requests.post(
                    f"{URL}/sendMessage",
                    data={
                        "chat_id": chat_id,
                        "text": f"Tu Chat ID es: {chat_id}"
                    }
                )

        time.sleep(1)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
