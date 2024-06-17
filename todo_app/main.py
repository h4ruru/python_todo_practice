from tasks.task_manager import TaskManager
import os

def display_menu():
    print("\nTodoリストメニュー:")
    print("0. リストメニューを表示する")
    print("1. タスクを表示する")
    print("2. タスクを追加する")
    print("3. タスクを削除する")
    print("4. 終了する")

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'data/tasks.json')
    task_manager = TaskManager(file_path)

    display_menu()  # 初回表示
    
    while True:
        print("\n0. リストメニューを表示する")
        choice = input("選択してください (0-4): ")

        if choice == '0':
            display_menu()
        elif choice == '1':
            task_manager.display_tasks()
        elif choice == '2':
            task_manager.add_task()
        elif choice == '3':
            task_manager.delete_task()
        elif choice == '4':
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度選択してください。")

if __name__ == "__main__":
    main()
