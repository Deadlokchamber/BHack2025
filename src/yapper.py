import os
from pyneuphonic import Neuphonic, TTSConfig
from pyneuphonic.player import AudioPlayer
import threading
class yapper:
    # Load the API key from the environment
    def __init__(self):
        self.client = Neuphonic(api_key=os.environ.get('NEUPHONIC_API_KEY'))

        self.sse = self.client.tts.SSEClient()

        # TTSConfig is a pydantic model so check out the source code for all valid options
        self.tts_config = TTSConfig(
            speed=1,
            lang_code='en', # replace the lang_code with the desired language code.
            voice_id='b19687fd-c5c9-4bda-9d52-756c3b10c88e'  # use client.voices.list() to view all available voices
        )
    

    # Create an audio player with `pyaudio`
    def startYapThread(self,text):
        threading.Thread(target=self.yap,args=(text,),daemon=True).start()


    def yap(self,text):
        with AudioPlayer() as player:
            response = self.sse.send(text, tts_config=self.tts_config)
            player.play(response)
            
