import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import os
from openai import OpenAI
from playsound import playsound
from pathlib import Path

# Set the path to the FFmpeg bin directory
ffmpeg_path = r"C:\Users\aghazouani\Downloads\ffmpeg-2023-11-05-git-44a0148fad-essentials_build\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

# Record the audio
def record_audio(duration=10, sample_rate=44100, filename='output.wav'):
    print("Recording...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()  # Wait until recording is finished
    write(filename, sample_rate, recording)  # Save as WAV file
    print("Recording finished.")

# Transcribe the audio
def transcribe_audio(filename='output.wav'):
    print("Transcribing...")
    model = whisper.load_model("base")
    audio = whisper.load_audio(filename)
    result = model.transcribe(audio)
    print("Transcription:", result['text'])
    return result['text']

# Instantiate the OpenAI client with your API key
Client = OpenAI(api_key="Your OpenAI Key")

# Function to convert text to speech and play it
def text_to_speech_and_play(text, speech_file_path='response.mp3'):
    # Get GPT-3 response
    gpt_response = Client.completions.create(prompt=text,model="text-davinci-003",max_tokens=150)
    response_text = gpt_response.choices[0].text.strip()
    print("GPT-3 Response:", response_text)
    
    # Generate speech from the GPT-3 response
    response = Client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=response_text
    )
    
    # Save the TTS response as an audio file
    with open(speech_file_path, 'wb') as f:
        f.write(response.content)
    
    # Play the audio response
    playsound(str(speech_file_path))

# Full process
record_audio(duration=5)  # Record for 5 seconds
transcribed_text = transcribe_audio()  # Transcribe the recorded audio
text_to_speech_and_play(transcribed_text)  # Convert GPT-3 text response to speech and play it
