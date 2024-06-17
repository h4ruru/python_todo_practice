import json
import os

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def display_tasks(self):
        if not self.tasks:
            print("Todoリストは空です。")
        else:
            print("Todoリスト:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def add_task(self):
        task = input("追加するタスクを入力してください: ")
        self.tasks.append(task)
        self.save_tasks()
        print(f"タスク '{task}' を追加しました。")

    def delete_task(self):
        self.display_tasks()
        try:
            task_number = int(input("削除するタスクの番号を入力してください: "))
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"タスク '{removed_task}' を削除しました。")
            else:
                print("無効な番号です。")
        except ValueError:
            print("番号を入力してください。")
