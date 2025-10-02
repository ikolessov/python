def convert_to_int(value):
    try:
        result = int(value)
        print(f"Преобразование прошло успешно: {result}")
        return result
    except ValueError:
        print(f"Ошибка: невозможно преобразовать '{value}' в целое число.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Попытка преобразования завершена.\n")

if __name__ == "__main__":
    # Корректная строка
    convert_to_int("123")

    # Некорректная строка
    convert_to_int("abc")

    # Другой тип данных
    convert_to_int([1, 2, 3])
