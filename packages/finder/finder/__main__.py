from googletrans import Translator


def main(args):
    sentence = args.get("sentence")
    destination = args.get("language")
    translator = Translator()
    language = translator.detect(sentence, dest=destination)
    translated = translator.translate(sentence, dest=destination)
    body = "Language detected: {0} | Translation: {1}".format(language.lang, translated.text)
    return {"body":  body}
