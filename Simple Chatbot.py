import os
import sys
import traceback
from pathlib import Path
from dotenv import load_dotenv
from google import genai

if hasattr(sys, 'frozen'):
    base_dir = Path(sys.executable).parent
elif '__file__' in globals() and __file__:
    base_dir = Path(__file__).resolve().parent
else:
    base_dir = Path.cwd()

env_path = base_dir / ".env"

# Lädt die .env aus dem Ordner
load_dotenv(dotenv_path=env_path)

try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            f"KEIN API-KEY GEFUNDEN!\nGesuchter Pfad: {env_path}\nBitte prüfe, ob die .env-Datei dort liegt und 'GEMINI_API_KEY=DeinKey' enthält."
        )

    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-3.6-flash")

    print("Chatbot gestartet! Tippe 'tschüss' zum Beenden.\n")

    while True:
        user_input = input("Du: ")

        if user_input.lower() in ["verlassen", "auf wiedersehen", "tschüss", "exit"]:
            print("")
            print("Buraks Chatbot: Auf Wiedersehen!")
            break

        if not user_input.strip():
            continue

        response = chat.send_message(user_input)
        print("")
        print(f"Buraks Chatbot: {response.text}\n")

except Exception as e:
    print(f"\nEs ist ein Fehler aufgetreten:\n{e}")
    traceback.print_exc()

finally:
    input("\nDrücke Enter, um das Fenster zu schließen...")