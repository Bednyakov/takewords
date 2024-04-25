from googletrans import Translator


def api_translator(text: str) -> str:
    """
    Возвращает переведенную на русский строку.
    """
    try:
        if len(text.split()) < 300:
            translator = Translator()
            translation = translator.translate(text, dest='ru')
            return translation.text
        return {'sorry': 'Слишком длинный текст.'}

    except Exception as e:
        return {'sorry': ['no', 'data', e]}
