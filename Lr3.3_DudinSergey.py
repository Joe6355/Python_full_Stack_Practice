
#созд класса ошибок
class PhoneError(Exception):
    pass


#error пустого номера
class EmptyPhoneError(PhoneError):
    pass


#error начала номера
class PrefixPhoneError(PhoneError):
    pass


#error скобок
class BracketsPhoneError(PhoneError):
    pass


#error дефисов
class HyphenPhoneError(PhoneError):
    pass


#error недопустимых символов
class SymbolsPhoneError(PhoneError):
    pass


#error количества цифр
class LengthPhoneError(PhoneError):
    pass


#функция проверки номера
def check_phone_DSV(number):

    #проверяем тип данных
    if not isinstance(number, str):
        raise TypeError("Номер должен быть строкой!")

    #убираем все пробелы
    number = "".join(
        symbol for symbol in number if not symbol.isspace()
    )

    #проверяем что номер не пустой
    if not number:
        raise EmptyPhoneError(
            "Номер телефона не может быть пустым!"
        )

    #проверяем допустимые символы
    for symbol in number:
        if symbol not in "0123456789+-()":
            raise SymbolsPhoneError(
                "Номер содержит недопустимые символы!"
            )

    #проверка дефисов
    if (number.startswith("-") or
            number.endswith("-") or
            "--" in number):
        raise HyphenPhoneError(
            "Дефис не может стоять в начале, "
            "в конце или два раза подряд!"
        )

    #считаем открывающие и закрывающие скобки
    open_bracket = number.count("(")
    close_bracket = number.count(")")

    #проверяем количество пар скобок
    if (open_bracket, close_bracket) not in ((0, 0), (1, 1)):
        raise BracketsPhoneError(
            "Допускается только одна пара скобок!"
        )

    #проверяем порядок скобок
    if open_bracket == 1:
        if number.index("(") > number.index(")"):
            raise BracketsPhoneError(
                "Скобки расположены неправильно!"
            )

    #убираем скобки и дефисы
    number = number.replace("(", "")
    number = number.replace(")", "")
    number = number.replace("-", "")

    #проверяем начало номера +7 или 8
    if not (number.startswith("+7") or number.startswith("8")):
        raise PrefixPhoneError(
            "Номер должен начинаться с +7 или 8!"
        )

    #убираем плюс перед проверкой цифр
    if number.startswith("+7"):
        digits = number[1:]
    else:
        digits = number

    #проверяем что остались только цифры
    if any(symbol not in "0123456789" for symbol in digits):
        raise SymbolsPhoneError(
            "Знак + допускается только перед цифрой 7!"
        )

    #проверяем количество цифр
    if len(digits) != 11:
        raise LengthPhoneError(
            "В номере должно быть 11 цифр! "
            f"Сейчас: {len(digits)}"
        )

    #заменяем первую 8 на +7 или возвращаем +7
    result = "+7" + digits[1:]

    #возвращаем правильный номер
    return result


#запуск программы
if __name__ == "__main__":

    try:
        #ввод номера пользователем
        phone = input("Введите номер телефона: ")

        #проверка и преобразование номера
        result = check_phone_DSV(phone)

        #вывод результата
        print("Номер телефона корректный!")
        print("Результат:", result)

    #обработка пользовательских ошибок
    except (
        EmptyPhoneError,
        PrefixPhoneError,
        BracketsPhoneError,
        HyphenPhoneError,
        SymbolsPhoneError,
        LengthPhoneError
    ) as error:
        print("Ошибка:", error)

    #обработка стандартной ошибки типа данных
    except TypeError as error:
        print("Ошибка типа данных:", error)

    #обработка прерывания ввода
    except (EOFError, KeyboardInterrupt):
        print("\nВвод номера был прерван!")
