import logging


def get_logger(name: str) -> logging.Logger:
    # Объявляем объект логгера и присваиваем имя
    logger = logging.getLogger(name)
    # Устанавливаем уровень логгера
    logger.setLevel(logging.DEBUG)

    # Обработчик
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Форматер для обработчика
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
