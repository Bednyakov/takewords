from parsers import textparser, words_from_text, translator
from tools.dbmanager import ManagerDB
from tools.loggers import logger


def main(url, ip_addr):
    """Создает БД, вызывает парсеры и создает словарь."""

    session = creator(ip_addr)

    if url:
        logger.info(f'IP: {ip_addr} URL: {url}')

        text_file: str = textparser.parser(url)
        logger.info(f'Textparser ok!')

        words: set = words_from_text.search(text_file)
        logger.info(f'Words search ok!')

        data: list = translator.mediator(words, session)
        logger.info('Translator ok!')

        session.insert_data(data)
        logger.info('Translated words added to the database.')

        session.insert_requests(session.table, ip_addr, url)
        logger.info('Request added to the database.')


def creator(ip_addr: str):
    name_db: str = 'translation.db'
    table: str = 'user_' + str(ip_addr).replace('.', '')
    return ManagerDB(name_db, table)


if __name__ == '__main__':
    raise Exception('Hello, it is modul!')