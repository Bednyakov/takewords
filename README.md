# takewords
Takewords - программа для сбора (парсинга) иностранных слов из веб-страниц, с автоматическим составлением словаря и переводом на русский язык.
Первоначальная идея программы- начальное изучение иностранного языка с помощью технической документации для начинающих специалистов, которым необходим второй язык в профессиональной деятельности.
____________________________________________________________
Не активируется виртуальная среда в python (pycharm) venv? 
____________________________________________________________
При ошибке "Невозможно загрузить файл ..., так как выполнение сценариев отключено в этой системе" делаем следующее:
1. Пуск -> PowerShell (от имени администратора)
2. Прописываем команду: Set-ExecutionPolicy RemoteSigned
3. На вопрос отвечаем: А
_____________________________________________________________
### Необходимые пакеты:
- requests
- bs4
- re
- googletrans 3.1.0a0 (pip install googletrans==3.1.0a0)
_________________________
### Наполнение

- [x] Модуль парсинга веб-страницы в HTML и TXT
- [x] Модуль создания файла со словами из текста
- [x] Модуль создания словаря с переводом слов и отсевом повторов
- [ ] Основная программа для изучения слов
- [ ] GUI (графический интерфейс)

