from googletrans import Translator


def api_translator(text: str) -> str:
    """
    Возвращает переведенную на русский строку.
    """
    try:
        translator = Translator()
        translation = translator.translate(text, dest='ru')
        return translation.text

    except Exception as e:
        return {'sorry': ['no', 'data', e]}
