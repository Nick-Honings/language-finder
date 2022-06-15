from googletrans import Translator


def main(args):
    sentence = args.get("sentence")
    destination = args.get("language")
    translator = Translator()
    language = translator.detect(sentence, dest=destination)
    translated = translator.translate(sentence, dest=destination)

    return {"body": {language.lang: translated.text}}
