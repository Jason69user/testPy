import json


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.index = 1

    def add_task(self, description: str):
        if any(description == task['description'] for task in self.tasks):
            print('Такая задача уже есть')
            return

        self.tasks.append({'id': self.index, 'description': description, 'completed': False})
        print(f'Задача №{self.index} "{description}" добавлена.')
        self.index += 1

    def complete_task(self, index: int):
        for task in self.tasks:
            if task['id'] == index:
                task['completed'] = True
                print(f"Задача {index} '{task['description']}' выполнена.")
                return
        print('Задача не найдена.')


    def remove_task(self, index: int):
        for i, task in enumerate(self.tasks):
            if task['id'] == index:
                removed_task = self.tasks.pop(i)
                print(f"Задача {index} '{removed_task['description']}' удалена.")
                for new_id, task in enumerate(self.tasks, start=1):
                    task['id'] = new_id

                self.index = len(self.tasks) + 1
                return

    def save_to_json(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)
        print(f'Задачи сохранены в файл {filename}')

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                loaded_tasks = json.load(file)
                for task in loaded_tasks:
                    if not any(existing_task['description'] == task['description'] for existing_task in self.tasks):
                        self.tasks.append(
                            {'description': task['description'], 'completed': task.get('completed', False)})

                self.index = 1
                for task in self.tasks:
                    task['id'] = self.index
                    self.index += 1

                print(f'Файл с задачами {filename} выгружен')
        except FileNotFoundError:
            print('Файл не найден.')
        except json.JSONDecodeError:
            print('Ошибка декодирования JSON.')

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return
        for task in self.tasks:
            status = "✓" if task['completed'] else "✗"
            print(f"[{status}] Задача №{task['id']}: {task['description']}")



def task_manager():
    task_manager = TaskManager()
    while True:
        enter = input('\nВыбирите действие из списка ниже:'
                      '\n1 - Просмотреть список задач'
                      '\n2 - Добавить задачу'
                      '\n3 - Пометить задачу выполенной'
                      '\n4 - Удалить задачу'
                      '\n5 - Сохранить список задач как...'
                      '\n6 - Загрузить список задачи из файла'
                      '\n7 - Выйти'
                      '\n Нажмите на цифру пункта меню: ')

        if enter == '1':
            task_manager.show_tasks()
        elif enter == '2':
            task = input('Введите описание задачи: ')
            task_manager.add_task(task)
        elif enter == '3':
            index = input('Введите номер задачи: ')
            task_manager.complete_task(index)
        elif enter == '4':
            index = input('Введите номер задачи: ')
            task_manager.remove_task(index)
        elif enter == '5':
            filename = input('Назовите файл: ')
            task_manager.save_to_json(filename)
        elif enter == '6':
            filename = input('Назовите файл: ')
            task_manager.load_from_json(filename)
        elif enter == '7':
            print('Выход из программы.')
            break
        else:
            print('Неверный ввод, попробуйте снова')


task_manager()