def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула {result}")
        return result

    return wrapper

def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None

        return wrapper

    return decorator

@logger
def add(a, b):
    return a + b

@logger
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


@logger
def greet(name):
    return f"Привет, {name}!"

@require_role(['admin'])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "Успешно удалено"


@require_role(['admin', 'manager'])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки сохранены"


@require_role(['user', 'admin', 'manager'])
def view_data(user):
    print(f"Данные просмотрены пользователем {user['name']}")
    return "Данные показаны"

if __name__ == "__main__":
    print("ТЕСТИРОВАНИЕ ДЕКОРАТОРА ЛОГИРОВАНИЯ")
    add(5, 3)
    print()
    divide(10, 2)
    print()
    divide(10, 0)
    print()
    greet("Анна")

    print("ТЕСТИРОВАНИЕ ДЕКОРАТОРА ДОСТУПА")
    users = [
        {'name': 'Алексей', 'role': 'admin'},
        {'name': 'Мария', 'role': 'manager'},
        {'name': 'Александр', 'role': 'user'},
        {'name': 'Ольга', 'role': 'guest'}
    ]

    for user in users:
        print(f"\nПользователь: {user['name']} (роль: {user['role']})")
        print("Удаление базы данных:", end=" ")
        delete_database(user)
        print("Изменение настроек:", end=" ")
        edit_settings(user)
        print("Просмотр данных:", end=" ")
        view_data(user)