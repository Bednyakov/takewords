from googletrans import Translator
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def progress(func):
    '''Декоратор, сигнализирующий, что функция не зависла.'''
    def inner(arg):
        result = func(arg)
        logger.info(f'Функция {func.__name__} обработала {arg}.')
        return result
    return inner

@progress
def en_ru_translator(word: str) -> str:
    '''Функция переводит переданную строку.'''
    translator = Translator()
    translation = translator.translate(word, dest='ru')
    return f'{word} {translation.text}'

if __name__ == '__main__':
    raise Exception('Запущен модуль!')