# AI Voice Agent

A Python-based voice assistant that listens to user commands, performs system tasks, and uses a LangChain tool-calling agent for intelligent responses.

---

## Features

- Voice input using microphone
- Text-to-speech response
- Open websites by voice
- Open Windows applications
- Tell current time
- AI responses using OpenAI via LangChain
- Tool calling support (search, wiki, save)

---

## How It Works

1. User speaks through microphone
2. Speech is converted to text
3. System checks for:
   - Website commands
   - System commands
4. If no system command is found:
   - Query is sent to LangChain agent
5. Agent processes the query using tools
6. Response is spoken back to the user

---

## Project Structure
AI-Voice-Agent/
│
├── main.py # Main voice assistant
├── sources.py # Custom tools (search, wiki, save)
├── requirements.txt
├── .env.example
├── README.md


---

## Installation

### 1. Clone Repository
git clone https://github.com/Eamon2009/AI-Agent-plus.git

cd AI-Voice-Agent


### 2. Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate


---

### 3. Install Dependencies


pip install -r requirements.txt


---

### 4. Add API Key

Rename `cofig.env` to `.env`

Add your OpenAI API key:


OPENAI_API_KEY=your_api_key


Get your API key from:
https://platform.openai.com/api-keys

---

## Usage

Run the assistant:


python main.py


Say commands like:

- "Open YouTube"
- "Open Google"
- "What is the time"
- "Open calculator"
- "Explain Python loops"
- "Stop"

---

## Supported Commands

### Websites
- YouTube
- Google
- Wikipedia
- GitHub
- Stack Overflow

### Windows Apps
- Calculator
- Notepad
- Camera

### AI Mode
Any other query is handled by the LangChain agent.

---

## Tools Used

- OpenAI GPT-3.5 via LangChain
- SpeechRecognition
- pyttsx3 (offline speech)
- Custom tools:
  - search_tool
  - wiki_tool
  - save_mth

---

## Notes

- Microphone is required
- Works best on Windows (uses SAPI5)
- Ensure internet connection for AI responses

---

## Future Improvements

- Memory support
- GUI interface
- Wake word detection
- Cross-platform support

---

## License

MIT License
