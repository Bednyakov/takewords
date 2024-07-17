from googletrans import Translator
from tools.loggers import logger


def api_translator(text: str, ip_addr: str) -> str:
    """
    Возвращает переведенную на русский строку.
    """
    logger.info(f'IP: {ip_addr} - запрос на перевод текста.')
    try:
        if len(text.split()) < 300:
            translator = Translator()
            translation = translator.translate(text, dest='ru')
            
            logger.info(f'Translated text: {translation.text}')
            return translation.text
        
        logger.info('Слишком длинный текст.')
        return {'sorry': 'Слишком длинный текст.'}

    except Exception as e:
        logger.info('Ошибка перевода.')
        return {'sorry': ['no', 'data', e]}
