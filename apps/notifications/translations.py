from modeltranslation.translator import TranslationOptions, register
from apps.notifications.models import Notification


@register(Notification)
class NotificationTranslationOptions(TranslationOptions):
    fields = ("message",)
