from app import celery
from main import main, creator


@celery.task
def get_words_task(url, ip_addr):
    main(url, ip_addr)
    session = creator(ip_addr)
    wordlist = session.get_data()
    result = {item.split()[0]: item.split()[1] for item in wordlist if len(item.split()) >= 2}
    return result