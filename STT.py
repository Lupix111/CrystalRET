from faster_whisper import WhisperModel


"""segments, info = model.transcribe("audio.mp3", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
"""
class STT():
    model_size = ""
    
    def STT():
        def __init__(self):
          self.model_size = "tiny"
          model = WhisperModel(self.model_size, device="cuda", compute_type="int8_float16")

    def setModel(self, modelSize):
        try:
            if modelSize in ["tiny","base","small","medium","large-v1","large-v2","large-v3","large-v3-turbo","distil-large-v2","distil-large-v3"]:
                self.model_size=modelSize
        except:
            print("The model does not exist.")

    #def startTranscibe(self, file_mp3):
