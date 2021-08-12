import datetime

from django.db import models
from django.contrib.auth.models import User


class Dayset(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'user')

    @classmethod
    def get_by_user(cls, user):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return cls.objects.filter(user=user, date=today).first()

    def __str__(self) -> str:
        return f"{self.date}({self.user})"


class Task(models.Model):
    class State(models.TextChoices):
        ACTIVE = 'a', ('Active')
        COMPLETED = 'c', ('Completed')

    title = models.CharField(max_length=256) 
    details = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=1, choices=State.choices, default=State.ACTIVE)
    dayset = models.ForeignKey(Dayset, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
