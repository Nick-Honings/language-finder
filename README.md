# language-finder - FAAS POC

## Description
Don't know what language your message is and need translation? Language Finder can help you.

Language Finder takes two parameters:
1. sentence = What sentence you want to translate.
2. language = What language you want to translate to.

Fire it to this url:
https://faas-ams3-2a2df116.doserverless.co/api/v1/web/fn-b5d07a52-a7ca-4ec8-b211-b1e460afb55e/finder/finder

And you should get a response like this:

{\
    "response_type": "in_channel",\
    "text": "Language detected: de | Translation: heaven" \
}


## Files
1. __main__.py
Entry point of the application
2. build.sh
First file that DigitalOcean executes
3. requirements.txt
Requirements of the application