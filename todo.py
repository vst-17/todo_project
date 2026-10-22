class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty")
        self.tasks.append({"title": task, "done": False})
        return len(self.tasks)

    def mark_done(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task not found")
        self.tasks[index]["done"] = True

    def get_tasks(self):
        return self.tasks

    def count_done(self):
        return sum(1 for t in self.tasks if t["done"])

    def delete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task not found")
        return self.tasks.pop(index)
    