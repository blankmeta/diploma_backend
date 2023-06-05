from django.contrib.auth import get_user_model

from diplom import settings
from diplom.celery import app

User = get_user_model()


@app.task
def soon_event_email(user_id: int, event_id: int):
    from django.core.mail import send_mail

    user = User.objects.get(id=user_id)

    send_mail(
        f"Скорое мероприятие {event_id}",
        "Не пропустите, а то получите по ебалу",
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )
