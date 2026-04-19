import pyaudio
import numpy as np
import wave
import time
import STT
import os

class audioTrigger:

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    SOGLIA_SQUELCH = 500  # Regola questo valore in base al volume della radio
    SILENZIO_POST_TRASM = 2 # Secondi di silenzio prima di chiudere il file
    
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.buffer = [] # Qui accumuliamo i chunk durante la trasmissione
        self.is_recording = False
        self.silence_start_time = None
        self.id_trasmissione = self._get_next_id() # ID iniziale

    def setChunk(self, chunks):
        try:
            if chunks in [512, 1024, 2048, 4096]:
                self.CHUNK==chunks
                self._start_stream() # Necessario riavviare
        except:
            print("Usa una potenza di 2 standard (512, 1024, 2048)")        
    
    def setRate(self, rate):
        """Imposta il Sample Rate (8000, 16000, 44100, 48000)"""
        standard_rates = [8000, 16000, 32000, 44100, 48000]
        if rate in standard_rates:
            self.RATE = rate
            self._start_stream()
            print(f"Sample Rate impostato a {rate}Hz")
        else:
            print(f"Rate non standard. Scegli tra: {standard_rates}")
    
    def setSquelch(self, valore):
        """Imposta la sensibilità del volume per far scattare la registrazione"""
        try:
            v = float(valore)
            if v >= 0:
                self.SOGLIA_SQUELCH = v
                print(f"Soglia Squelch impostata a {v}")
        except ValueError:
            print("Inserisci un numero non negativo per lo Squelch")

    def setSilenzioPostTrasm(self, secondi):
        """Imposta quanti secondi attendere prima di chiudere la registrazione"""
        try:
            s = float(secondi)
            if s > 0:
                self.SILENZIO_POST_TRASM = s
                print(f"Silenzio post-trasmissione: {s}s")
        except ValueError:
            print("Inserisci un numero di secondi non negativo")

    def stopRecord(self):
        stream=self.p.close()
        print("Trigger stopped")

    def startRecord(self):
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        print("trigger started")
        data=stream.read(self.CHUNK)    # Read the microphone input

