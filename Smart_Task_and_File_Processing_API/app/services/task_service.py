from exceptions.custom_exceptions import (
    TaskNotFoundException
)


class TaskService:

    def __init__(self):
        self.tasks = []
        self.task_counter = 1

    def create_task(
        self,
        task_data: dict
    ):
        """
        Create a new task.
        """

        task_data["id"] = self.task_counter

        self.tasks.append(task_data)

        self.task_counter += 1

        return task_data

    def get_all_tasks(self):
        """
        Return all tasks.
        """

        return self.tasks

    def get_task_by_id(
        self,
        task_id: int
    ):
        """
        Get task by ID.
        """

        for task in self.tasks:

            if task["id"] == task_id:
                return task

        raise TaskNotFoundException()

    def update_task(
        self,
        task_id: int,
        update_data: dict
    ):
        """
        Update task.
        """

        for task in self.tasks:

            if task["id"] == task_id:

                task.update(update_data)

                return task

        raise TaskNotFoundException()

    def delete_task(
        self,
        task_id: int
    ):
        """
        Delete task.
        """

        for task in self.tasks:

            if task["id"] == task_id:

                self.tasks.remove(task)

                return {
                    "message": "Task deleted successfully"
                }

        raise TaskNotFoundException()


task_service = TaskService()