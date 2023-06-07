from django.contrib.auth import get_user_model

from diplom import settings
from diplom.celery import app
from events.models import Event

User = get_user_model()


@app.task
def soon_event_email(user_id: int, event_id: int):
    from django.core.mail import send_mail

    user = User.objects.get(id=user_id)
    event = Event.objects.get(id=event_id)

    send_mail(
        f"Скорое мероприятие {event.title}",
        f"Не пропустите в {event.time}",
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )
