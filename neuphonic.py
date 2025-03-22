import os
from pyneuphonic import Neuphonic, TTSConfig
from pyneuphonic.player import AudioPlayer

# Load the API key from the environment
client = Neuphonic(api_key=os.environ.get('NEUPHONIC_API_KEY'))

sse = client.tts.SSEClient()

# TTSConfig is a pydantic model so check out the source code for all valid options
tts_config = TTSConfig(
    speed=1.5,
    lang_code='en', # replace the lang_code with the desired language code.
    voice_id='e564ba7e-aa8d-46a2-96a8-8dffedade48f'  # use client.voices.list() to view all available voices
)

# Create an audio player with `pyaudio`
with AudioPlayer() as player:
    response = sse.send('Enemy at 78 degrees', tts_config=tts_config)
    player.play(response)
    response2 = sse.send('Enemy at 83 degrees', tts_config=tts_config)
    player.play(response2)
