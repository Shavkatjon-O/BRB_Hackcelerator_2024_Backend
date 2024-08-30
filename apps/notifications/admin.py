from django.contrib import admin
from apps.notifications.models import Notification
from core.mixins import TabbedTranslationAdmin


@admin.register(Notification)
class NotificationAdmin(TabbedTranslationAdmin):
    pass
