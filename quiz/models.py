from django.db import models

# Create your models here.
class Question(models.Model):
    que = models.CharField(max_length=200)
    ans = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.que}'

    class Meta:
        ordering = [ '-created']

class Quiz(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reward = models.IntegerField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


