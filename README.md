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
- pip install -r requirements.txt
3. **FFmpeg Setup:**
- Download and extract FFmpeg.
- Update the `ffmpeg_path` variable in the script with your FFmpeg bin directory path.

3. **OpenAI API Key:**
- Set your OpenAI API key in the script.

4. **Running the Script:**
- Python app.py

The script will automatically record, transcribe, and respond to audio input.

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with your suggestions.

