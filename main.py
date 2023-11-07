class Task:
    def __init__(self, description, status):
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks):
                print(f"Task {i+1}:")
                print(f"Description: {task.description}")
                print(f"Status: {task.status}")
                print("")
        else:
            print("No tasks found.")

    def update_task_status(self, task_num, new_status):
        if task_num > 0 and task_num <= len(self.tasks):
            self.tasks[task_num-1].status = new_status
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_num):
        if task_num > 0 and task_num <= len(self.tasks):
            deleted_task = self.tasks.pop(task_num-1)
            print(f"Task '{deleted_task.description}' deleted.")
        else:
            print("Invalid task number.")

# Sample usage
todo_list = ToDoList()

# Add tasks
task1 = Task("Complete coding assignment", "Incomplete")
todo_list.add_task(task1)

task2 = Task("Finish reading a book", "Incomplete")
todo_list.add_task(task2)

# View all tasks
todo_list.view_tasks()

# Update task status
todo_list.update_task_status(1, "Complete")

# Delete task
todo_list.delete_task(2)