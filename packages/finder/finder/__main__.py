from googletrans import Translator


def main(args):
    sentence = args.get("sentence", "Whatever")
    print(sentence)
    destination = args.get("language", "English")
    print(destination)


    translator = Translator()
    language = translator.detect(sentence, dest=destination)
    translated = translator.translate(sentence, dest=destination)
    body = "Language detected: {0} | Translation: {1}".format(language.lang, translated.text)
    print(body)

    return {
        'body': {
            'response_type': 'in_channel',
            'text': body
        }
    }

