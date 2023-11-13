# Audio Interaction Script

This repository contains a Python script that integrates various technologies to create an interactive audio processing application. It records audio, transcribes it, sends the transcription to GPT-3, and plays back a spoken response.

## Features

- **Audio Recording:** Captures audio input and saves it as a WAV file.
- **Audio Transcription:** Uses OpenAI's Whisper model to transcribe the recorded audio.
- **Text Processing and Response:** The transcribed text is processed by OpenAI's GPT-3, generating a contextual response.
- **Text-to-Speech:** Converts the GPT-3 generated text into speech and plays it back.
- **FFmpeg Integration:** Uses FFmpeg for audio processing tasks.

## Requirements

- Python 3
- sounddevice
- scipy
- whisper
- openai
- playsound
- FFmpeg

## Setup and Usage

1. **Install Dependencies:**
