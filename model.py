import whisper
import os

class TranscripterModel: 
    def __init__(self):
        self.model = whisper.load_model("base")

    def process_audio(self, ruta_archivo): 
        if not os.path.exists(ruta_archivo):
            return "ERROR: Archivo de audio no encontrado/existe"

        resultado = self.model.transcribe(ruta_archivo)
        return resultado.get("text", " ")