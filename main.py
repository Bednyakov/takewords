import textparser, words_from_text, translator, wordsfilter

def main():

    textparser.parser()
    words_from_text.search()
    translator.en_ru_translator()
    wordsfilter.filter()

if __name__ == '__main__':
    main()

