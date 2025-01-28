# Siri - The Virtual Assistant

This is a Python-based virtual assistant named **Siri**. It interacts with the user through voice commands and performs tasks such as searching Wikipedia, opening websites, playing music, telling jokes, and more.

## Features

- **Voice Interaction**: The assistant listens to and responds to user commands using speech recognition.
- **Task Execution**: Perform various tasks such as:
  - Search Wikipedia for information
  - Open YouTube or Google with specific search queries
  - Play music from your computer
  - Tell the current time
  - Open Visual Studio Code
  - Open your photo gallery
  - Tell jokes using `pyjokes`
  - Exit the application gracefully
- **Customizable**: The assistant can be extended with more commands to suit user requirements.

## Requirements

Before running the script, ensure you have the following Python packages installed:

- `pyttsx3` (For text-to-speech functionality)
- `speechRecognition` (For speech recognition)
- `wikipedia` (For searching Wikipedia)
- `webbrowser` (For opening websites)
- `os` (For interacting with the operating system)
- `pyjokes` (For generating jokes)

You can install the required packages using the following pip command:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyjokes
```

## Setup and Usage

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd siri-virtual-assistant
   ```

2. Update the paths in the script to match your system for:
   - Music directory
   - Visual Studio Code executable path
   - Gallery folder

3. Run the Python script:
   ```bash
   python siri.py
   ```

4. The assistant will greet you and listen for voice commands. Use phrases like:
   - **"Search Wikipedia for Python programming"**
   - **"Open YouTube and search for travel videos"**
   - **"Play music"**
   - **"Tell me a joke"**
   - **"What's the time?"**
   - **"Exit"** to stop the assistant.

## Example Commands

- **Wikipedia Search**: "Search Wikipedia for machine learning"
- **YouTube Search**: "Open YouTube" (Followed by the search query)
- **Google Search**: "Open Google" (Followed by the search query)
- **Play Music**: "Play music"
- **Tell a Joke**: "Tell me a joke"
- **Time Check**: "What's the time?"
- **Exit Application**: "Exit"

## Enhancements Made

- Integrated **pyjokes** to add the ability to tell jokes.
- Enhanced YouTube and Google functionalities to accept search queries.
- Removed email-sending functionality for simplicity.
- Optimized user interaction with better speech feedback and error handling.

## Notes

- Ensure your microphone is working correctly for voice recognition.
- The script currently works with the English language (en-in).


