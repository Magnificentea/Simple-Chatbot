Markdown
# Python Gemini AI Chatbot

Ein interaktiver Terminal-Chatbot auf Basis der **Google Gemini API**, entwickelt in Python. Das Projekt demonstriert die Integration von modernen Large Language Models (LLMs), Gesprächsverlaufs-Management (Chat Sessions) und die sichere Handhabung von API-Schlüsseln.

---

## 💡 Funktionen

* **Kontextbezogener Chat:** Hält über `client.chats.create()` den Verlauf der Unterhaltung aufrecht, sodass die KI auf vorherige Nachrichten Bezug nehmen kann.
* **Sichere Konfiguration:** Verwendet `.env`-Umgebungsvariablen zur Kapselung des API-Schlüssels, um versehentliches Veröffentlichen von Credentials zu verhindern.
* **Fehlerfreie Modellanbindung:** Verwendet das aktuelle `gemini-3.6-flash`-Modell von Google.

---

## 🛠️ Technologien

* **Sprache:** Python 3.12+
* **SDK:** `google-genai`
* **Umgebungsvariablen:** `python-dotenv`
* **IDE:** JetBrains PyCharm

---

## 🚀 Installation & Einrichtung

### 1. Repository klonen
```bash
git clone [https://github.com/DEIN-GITHUB-BENUTZERNAME/Simple-Chatbot.git](https://github.com/DEIN-GITHUB-BENUTZERNAME/Simple-Chatbot.git)
cd Simple-Chatbot
2. Virtuelle Umgebung erstellen und aktivieren
Bash
python -m venv .venv

# Unter Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# Unter Linux/macOS:
source .venv/bin/activate
3. Abhängigkeiten installieren
Bash
pip install -r requirements.txt
4. API-Schlüssel konfigurieren
Erstelle im Projektverzeichnis eine Datei namens .env und trage deinen Google Gemini API-Schlüssel ein:

Code-Snippet
GEMINI_API_KEY=dein_gemini_api_key_hier
💻 Nutzung
Starte das Skript über das Terminal:

Bash
python "Simple Chatbot.py"
Gib deine Nachrichten ein und drücke Enter.

Tippe tschüss, exit oder verlassen, um das Programm zu beenden.

🛡️ Sicherheit
Dieses Repository nutzt eine .gitignore-Datei. Sensible Daten wie die .env-Datei und das .venv/-Verzeichnis werden nicht in die Versionsverwaltung übernommen.


---

### Was du noch anpassen kannst:
1. Ersetze `DEIN-GITHUB-BENUTZERNAME` durch deinen echten GitHub-Namen.
2. Speichere diesen Text direkt in der `README.md`-Datei im Ordner `Simple`.