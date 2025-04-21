from task_manager import TaskManager

def first_test():
    task_manager = TaskManager()
    task_manager.add_task('Первая задача')
    task_id = 1
    task_manager.complete_task(task_id)

    task = task_manager.tasks[0]

    status = 'выполнена' if task['completed'] else 'не выполнена'
    print(f"В первом тесте создана задача: '{task['description']}'. Статус: '{status}'.")

def second_test():
    task_manager = TaskManager()
    task_manager.add_task('Задача для удаления')
    task_manager.remove_task(1)

    if not task_manager.tasks:
        print("Во втором тесте задача успешно удалена, список задач пуст.")
    else:
        task = task_manager.tasks[0]
        print(f"Во втором тесте удалена задача: '{task['description']}' (но список задач не пуст)")

def third_test():
    task_manager = TaskManager()
    task_manager.add_task('Задача для сохранения')
    task_manager.save_to_json('Тестовый файл')
    task_manager.load_from_json('Тестовый файл')

first_test()
second_test()
third_test()