from flask import Flask, render_template, request
import jinja2
from morse_decoder import morse_decoder









app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def morsecode():

    text_to_morse = request.form.get("textinput")
    morse_to_text = request.form.get("morseinput")
    translation = ""
    if request.method == "POST":
        try:
            if text_to_morse:
                translation_type = text_to_morse
            elif morse_to_text:
                translation_type = morse_to_text
            else:
                pass
            
            code = request.form.get("morse-code")
            translation = morse_decoder(translation_type, code)
        except:
            pass

    return render_template("morse.html", translation=translation)

while __name__ == "__main__":
    app.run(debug=True)