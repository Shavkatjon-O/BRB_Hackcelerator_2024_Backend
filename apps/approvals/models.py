from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel

User = get_user_model()


class RequestTypeChoices(models.TextChoices):
    LEAVE = "LEAVE", "Leave"
    EXPENSE = "EXPENSE", "Expense"
    TRAVEL = "TRAVEL", "Travel"
    ABSENCE = "ABSENCE", "Absence"
    MEETING_ROOM_BOOKING = "MEETING_ROOM_BOOKING", "Meeting Room Booking"
    PROJECT_EXTENSION = "PROJECT_EXTENSION", "Project Extension"
    OVERTIME = "OVERTIME", "Overtime"
    WORK_FROM_HOME = "WORK_FROM_HOME", "Work From Home"
    TRAINING = "TRAINING", "Training"
    SHIFT_CHANGE = "SHIFT_CHANGE", "Shift Change"
    EQUIPMENT = "EQUIPMENT", "Equipment"
    SICK_LEAVE = "SICK_LEAVE", "Sick Leave"


class RequestStatusChoices(models.TextChoices):
    PENDING = "PENDING", "Pending"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"


class Request(BaseModel):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    request_type = models.CharField(
        max_length=50,
        choices=RequestTypeChoices.choices,
        default=RequestTypeChoices.LEAVE,
    )
    status = models.CharField(
        max_length=50,
        choices=RequestStatusChoices.choices,
        default=RequestStatusChoices.PENDING,
    )

    description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.request_type} request by {self.user} for {self.start_date} - {self.end_date}"
