import os
from google import genai

# Ersetze DEIN_GEMINI_API_KEY durch deinen echten Key
client = genai.Client(api_key="AQ.Ab8RN6LB1U2gYXQBj0Dk8-0F6KO4_PrP3-MVqJKw5G0HorJWEw")

# Erstelle ein Chat-Objekt (merkt sich den Gesprächsverlauf)
chat = client.chats.create(model="gemini-3.6-flash")

if __name__ == "__main__":
    print("Chatbot gestartet! Tippe 'tschüss' zum Beenden.\n")

    while True:
        user_input = input("Du: ")

        if user_input.lower() in ["verlassen", "auf wiedersehen", "tschüss", "exit"]:
            print("Buraks Chatbot: Auf Wiedersehen!")
            break

        if not user_input.strip():
            continue

        # Nachricht über den Chat senden
        response = chat.send_message(user_input)
        print(f"Buraks Chatbot: {response.text}\n")