from flask import Flask, render_template, request
import os 
from model import TranscripterModel

app = Flask(__name__, template_folder="mvc")

FOLDER_UPLOAD = "uploads"
os.makedirs(FOLDER_UPLOAD, exist_ok=True)
app.config["UPLOAD_FOLDER"] = FOLDER_UPLOAD

AI_model = TranscripterModel()

@app.route("/", methods=["GET", "POST"])
def index():
    text_transcription = None

    if request.method == "POST":
        if "audio_file" not in request.files:
            return "ERROR: No se encontró el archivo de audio en la solicitud"

        audio_file = request.files["audio_file"]

        if audio_file.filename == "":
            return "ERROR: No se seleccionó ningún archivo de audio"

        if audio_file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_file.filename)
            audio_file.save(file_path)

            text_transcription = AI_model.process_audio(file_path)

        os.remove(file_path)
    return render_template("index.html", text_transcription=text_transcription)

if __name__ == "__main__":
    app.run(debug=True)