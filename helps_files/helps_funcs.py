import os
from helps_files.static_per import *


# Всякие собственные исключения для пароля


class LengthError(Exception):
    pass


class LetterError(LengthError):
    pass


class DigitError(LengthError):
    pass


# Функция для проверки пароля при регистрации
def check_password(password: str):
    digits = (False, False, False)
    if len(password) <= 5:
        raise LengthError
    for sym in password:
        if sym.isdigit() and not digits[0]:
            digits = (True, digits[1], digits[2])
        elif sym.isupper() and not digits[1]:
            digits = (digits[0], True, digits[2])
        elif sym.islower() and not digits[2]:
            digits = (digits[0], digits[1], True)
        if all(digits):
            break
    if not all(digits):
        if not digits[0]:
            raise DigitError
        raise LetterError
    if not digits:
        raise DigitError
    return True


# Проверка логина при регистрации
def check_login(login):
    return all([sym not in BAD_SYM for sym in login])


# Функция, которая возвращает количество карт при статистике
def get_num(line):
    return sum([1 if stro else 0 for stro in line.split(', ')])


# Возвращает html для отображения профиля в коллекциях
def html_get_to_profile(login):
    return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { " \
           "white-space: pre-wrap; }\n</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:8." \
           "25pt; font-weight:400; font-style:normal;\">\n<p align=\"right\" " \
           "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; " \
           "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Ваш профиль: " \
           f"<span style=\" font-size:11pt;  font-weight:600;\">{login}</span></p></body></html>"


# Возвращает html для количества карт в конце игры
def html_get_to_num_of_card(num_of_cards, num_of_correct_cards):
    return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" \
           "p, li { white-space: pre-wrap; }\n" \
           "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:8pt; font-weight:400; " \
           "font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; " \
           "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans Light\'; " \
           f"font-size:9pt;\">Количество правильных ответов: {num_of_correct_cards}</span></p>\n" \
           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; " \
           "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans Light\'; font-size:9pt;\">" \
           f"Всего карт было: {num_of_cards}</span></p></body></html>"


# Возвращает html для отображения рейтинга карты
def html_get_to_user_fun(text, color):
    return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" \
           "p, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:\'Open Sans Light\';" \
           " font-size:8pt; font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px;" \
           " margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" \
           f"<span style=\" font-size:9pt; color:{color};\">{text}</span></p></body></html>"


# Возвращает html для окна с удалением коллекции/карты
def html_get_to_delete_window(collection, card=''):
    if card:
        return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: " \
               "pre-wrap; }\n</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:10pt; " \
               "font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px; " \
               "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" \
               "<span style=\" font-family:\'MS Shell Dlg 2\';\">Удалить карту </span><span style=\" font-family:\'" \
               f"MS Shell Dlg 2\'; font-weight:600;\">&quot;{card}&quot;</span><span style=\" " \
               "font-family:\'MS Shell Dlg 2\';\"> из коллекции </span><span style=\" font-family:\'MS Shell Dlg 2\'" \
               f"; font-weight:600;\">&quot;{collection}&quot;</span><span style=\" font-family:" \
               "\'MS Shell Dlg 2\';\">?</span></p></body></html>"
    else:
        return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: " \
               "pre-wrap; }\n</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:10pt; " \
               "font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px; " \
               "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" \
               "<span style=\" font-family:\'MS Shell Dlg 2\';\">Удалить коллекцию </span><span style=\" " \
               "font-family:\'" \
               f"MS Shell Dlg 2\'; font-weight:600;\">&quot;{collection}&quot;</span><span style=\" font-family:" \
               "\'MS Shell Dlg 2\';\">?</span></p></body></html>"


# Возвращает html для игры (отображение карт, если там текст)
def html_get_to_card_game_text(text):
    return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li " \
           "{ white-space: pre-wrap; }\n</style></head><body style=\" font-family:\'Open Sans Light\'; " \
           "font-size:8.25pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; " \
           "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" " \
           f"font-size:11pt;\">{text}</span></p></body></html>"


# Возвращает html для окна со статистикой
def html_get_to_statistics(collec_n, true_c, false_c, date_time, num_g, coeff):
    if not true_c:
        true_c = 'таких карт нет..'
    if not false_c:
        false_c = 'таких карт нет...'
    return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { " \
           "white-space: pre-wrap;}\n</style></head><body style=\" font-family:\'Open Sans Light\'; " \
           "font-size:10pt; font-weight:400; " \
           "font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; " \
           "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> " \
           f"Игра номер <span style=\" font-weight:600;\">{num_g}</span></p>\n<p style=\" " \
           "margin-top:0px; margin-bottom:0px; " \
           "margin-left:0px; margin-right:0px; -qt-block-indent:0; " \
           f"text-indent:0px;\">Коллекция: {collec_n}" \
           "</p>\n<p style=\" margin-top:0px; margin-bottom:0px; " \
           "margin-left:0px; margin-right:0px; -qt-block-indent:0; " \
           f"text-indent:0px;\">Правильные карты: {true_c}</p>\n<p style=\" " \
           "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; " \
           f"-qt-block-indent:0; text-indent:0px;\">Неправильные карты: {false_c}</p>\n<p style=\" margin-top:0px; " \
           "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; " \
           f"text-indent:0px;\">Процент правильных ответов: {coeff}</p>\n<p style=\" margin-top:0px; " \
           "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" \
           f"{date_time}</p>\n<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; " \
           "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n<p style=\"" \
           "-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; " \
           "-qt-block-indent:0; text-indent:0px;\"><br /></p>\n<p style=\"-qt-paragraph-type:empty; " \
           "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; " \
           "text-indent:0px;\"><br /></p></body></html>"


# Проверяет есть ли фотка в папке БД фоток
def check_path(file_name):
    return os.path.exists(f'databases/users_photos/{file_name}')


# Удаляет фотки из папки БД фоток
def delete_photos(photos):
    for photo in photos:
        if check_path(photo):
            os.remove(f'databases/users_photos/{photo}')
