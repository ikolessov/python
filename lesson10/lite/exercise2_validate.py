def validate_user_input(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Входные данные должны быть словарем.")
        if 'name' not in data or not isinstance(data['name'], str):
            raise ValueError("Ключ 'name' отсутствует или не является строкой.")
        if 'age' not in data or not (isinstance(data['age'], int) or isinstance(data['age'], float)) or data['age'] <= 0:
            raise ValueError("Ключ 'age' отсутствует или значение не является положительным числом.")
        print(f"Данные пользователя корректны: {data}")
        return True
    except Exception as e:
        raise e from None

if __name__ == "__main__":
    # Корректные данные
    validate_user_input({"name": "Alice", "age": 30})

    # Отсутствует ключ name
    try:
        validate_user_input({"age": 25})
    except Exception as e:
        print(e)

    # Некорректное значение age
    try:
        validate_user_input({"name": "Bob", "age": -5})
    except Exception as e:
        print(e)

    # Некорректный тип данных
    try:
        validate_user_input("invalid_data")
    except Exception as e:
        print(e)
