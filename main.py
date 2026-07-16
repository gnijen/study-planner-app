from planner import Planner
from storage import save_tasks, load_tasks


def show_menu():
    print("1. Add task")
    print("2. View all tasks")
    print("3. View prioritized tasks")
    print("4. Mark task complete")
    print("5. Remove task")
    print("6. Export report")
    print("7. Quit")
    

def main():
    planner = Planner()
    planner.tasks = load_tasks()   # manually wire up existing data
    
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "7":
            print("Goodbye!")
            break

        save_tasks(planner.get_all_tasks())

if __name__ == "__main__":
    main()