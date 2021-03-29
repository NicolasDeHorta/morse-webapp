import json

def morse_decoder(translation_type, code):
    if translation_type == "text":
        text = code
        with open("static/morse-code.json") as file:
            text_to_morse_dic = json.load(file)
        translation = ""

        for letter in text:
            if letter != " ":
                translation += text_to_morse_dic[letter.lower()]
                translation += " | "
            else:
                translation += " | "
                
        return translation

    if translation_type == "morse":

        with open("static/morse-to-text.json") as file:
            morse_to_text_dic = json.load(file)
        morse = code
        morse = morse.split(" ")
        translation = ""

        for letter in morse:
            if letter == "|":
                translation += " "
            elif letter in [key for (key, value) in morse_to_text_dic.items()]:
                translation += morse_to_text_dic[letter]
            else:
                pass

        return translation
