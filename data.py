def write_file():
    try:
        with open('data.txt', 'w') as file:
            file.write("Chocolate's embrace\n")
            file.write("Soft caramel dream at hand,\n")
            file.write("Snickers in my grip.")
    except IOError:
        print('Ошибка ввода-вывода')

def read_file():
    try:
        with open('data.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        print("Нет прав доступа к файлу.")

def append_file():
    try:
        with open('data.txt', 'a') as file:
            file.write('\nIt was delicious for everyone')
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        print("Нет прав доступа к файлу.")

def read_line():
    try:
        with open('data.txt', 'r') as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        print("Нет прав доступа к файлу.")

def copy_file():
    try:
        with open('data.txt', 'rb') as source_file:
            with open('data_copy.txt', 'wb') as copy_file:
                copy_file.write(source_file.read())
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        print("Нет прав доступа к файлу.")


write_file()
read_file()
append_file()
read_line()
copy_file()