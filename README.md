# Siri - The Virtual Assistant

This is a Python-based virtual assistant named **Siri**. It can interact with the user through voice commands, execute tasks such as searching Wikipedia, sending emails, opening websites, playing music, and more.

## Features

- **Voice Interaction**: The assistant listens and responds to user commands.
- **Task Execution**: Perform various tasks such as:
  - Search Wikipedia
  - Open YouTube or Google
  - Play music from your computer
  - Tell the current time
  - Open Visual Studio Code
  - Access your photo gallery
  - Send emails (Gmail integration)
- **Customizable**: The assistant can be extended with more commands to suit your needs.

## Requirements

Before running the script, ensure you have the following Python packages installed:

- `pyttsx3` (For text-to-speech functionality)
- `speechRecognition` (For speech recognition)
- `wikipedia` (For searching Wikipedia)
- `webbrowser` (For opening websites)
- `os` (For interacting with the operating system)
- `smtplib` (For sending emails via Gmail)

You can install the required packages using the following pip command:

```bash
pip install pyttsx3 SpeechRecognition wikipedia
