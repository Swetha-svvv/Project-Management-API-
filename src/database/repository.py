from sqlalchemy.orm import Session

from src.database.models import User, Project, Task


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, hashed_password: str):

        user = User(
            email=email,
            hashed_password=hashed_password,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def get_by_email(self, email: str):

        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_by_id(self, user_id: int):

        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )


class ProjectRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        name: str,
        description: str,
        owner_id: int,
    ):

        project = Project(
            name=name,
            description=description,
            owner_id=owner_id,
        )

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def get_all_by_owner(
        self,
        owner_id: int,
    ):

        return (
            self.db.query(Project)
            .filter(Project.owner_id == owner_id)
            .all()
        )

    def get_by_id(
        self,
        project_id: int,
    ):

        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def delete(
        self,
        project: Project,
    ):

        self.db.delete(project)
        self.db.commit()


class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        title,
        description,
        status,
        due_date,
        project_id,
    ):

        task = Task(
            title=title,
            description=description,
            status=status,
            due_date=due_date,
            project_id=project_id,
        )

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task

    def get_by_id(
        self,
        task_id,
    ):

        return (
            self.db.query(Task)
            .filter(Task.id == task_id)
            .first()
        )

    def get_by_project(
        self,
        project_id,
    ):

        return (
            self.db.query(Task)
            .filter(Task.project_id == project_id)
            .all()
        )

    def delete(
        self,
        task: Task,
    ):

        self.db.delete(task)
        self.db.commit()