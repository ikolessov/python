class UserAlreadyExistsError(Exception):
    """Ошибка: пользователь с таким именем уже существует."""
    def __init__(self, username):
        self.username = username
        super().__init__(f"Пользователь '{username}' уже существует.")


class UserNotFoundError(Exception):
    """Ошибка: пользователь с таким именем не найден."""
    def __init__(self, username):
        self.username = username
        super().__init__(f"Пользователь '{username}' не найден.")


class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"User(username={self.username}, email={self.email}, age={self.age})"


class UserManager:
    def __init__(self):
        self.users = {}  # словарь: username -> User

    def add_user(self, user: User):
        if user.username in self.users:
            raise UserAlreadyExistsError(user.username)
        self.users[user.username] = user
        print(f"[INFO] Пользователь {user.username} добавлен.")

    def remove_user(self, username: str):
        if username not in self.users:
            raise UserNotFoundError(username)
        del self.users[username]
        print(f"[INFO] Пользователь {username} удалён.")

    def find_user(self, username: str) -> User:
        if username not in self.users:
            raise UserNotFoundError(username)
        return self.users[username]


def main():
    manager = UserManager()

    # 1. Добавление пользователей
    try:
        user1 = User("alice", "alice@example.com", 25)
        manager.add_user(user1)

        user2 = User("bob", "bob@example.com", 30)
        manager.add_user(user2)

        # Попытка добавить пользователя с уже существующим именем
        duplicate_user = User("alice", "alice_new@example.com", 26)
        manager.add_user(duplicate_user)
    except UserAlreadyExistsError as e:
        print(f"[ERROR] {e}")

    print()

    # 2. Удаление пользователя
    try:
        manager.remove_user("charlie")  # такого пользователя нет
    except UserNotFoundError as e:
        print(f"[ERROR] {e}")

    print()

    # 3. Поиск пользователя
    try:
        found_user = manager.find_user("bob")
        print(f"[INFO] Найден пользователь: {found_user}")

        manager.find_user("david")  # такого пользователя нет
    except UserNotFoundError as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()
