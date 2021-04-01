import pickle
import wave
from typing import Any

import pyaudio


class Film:
    def __init__(self, name: str, format: int, bw_color: bool, iso: int, grain: str, info: str):
        self.name: str = name
        self.format: int = format
        self.bw_color: bool = bw_color
        slef.process:str = process
        self.iso: int = iso
        self.grain: str = grain
        self.info: str = info

class Chem:
    def __init__(self
        self.name

def print_hi(name):
    return f'Hi, {name}'


def save_config(data: Any, file_name: str):
    try:
        with open(file_name, 'xb') as file:
            pickle.dump(data, file)

    except FileExistsError as e:
        print(f'File error: {e}')
    except OSError as e:
        print(f'System error: {e}')
    else:
        print('File saved successfully')


def load_config(file_name: str):
    try:
        with open(file_name, 'rb') as file:
            data = pickle.load(file)
    except OSError as e:
        print(f'System error: {e}')
    else:
        print('file read successfully')
    return data

def play_alert_sound():
    t = Thread(target=generate_audio)
    t.start()


def generate_audio():
    with wave.open('alert.wav', "rb") as f:
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # define stream chunk
        chunk = 1024
        data = f.readframes(chunk)
        # play audio stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()
def play_alert_sound():
    with wave.open('alert.wav', "rb") as f:
        generate_audio(f)

if __name__ == '__main__':
    play_alert_sound()
    play_alert_sound()
