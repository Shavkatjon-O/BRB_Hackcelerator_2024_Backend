from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User


class TaskStatusChoices(models.TextChoices):
    TO_DO = "to_do", "To Do"
    IN_PROGRESS = "in_progress", "In Progress"
    IN_REVIEW = "in_review", "In Review"
    APPROVAL_NEEDED = "approval_needed", "Approval Needed"
    COMPLETED = "completed", "Completed"
    CANCELED = "canceled", "Canceled"
    ARCHIVED = "archived", "Archived"
    ON_HOLD = "on_hold", "On Hold"


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=TaskStatusChoices.choices,
        default=TaskStatusChoices.TO_DO,
    )

    due_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_tasks"
    )

    def __str__(self):
        return self.title
