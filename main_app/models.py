from django.db import models

# Create your models here.
from django.db import models

# możliwe kategorie ogłoszeń

list_of_categories = ((0, 'inne'),
                      (1, 'odzież'),
                      (2, 'motoryzacja'),
                      (3, 'usługi'),
                      (4, 'żywność'),
                      (5, 'sport'),)


class User(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.IntegerField(null=True)
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.surname


# tabela ogłoszeń
class Ad(models.Model):
    title = models.CharField(max_length=64, null=True)
    content = models.TextField(null=True)
    active = models.BooleanField(default=True)
    category = models.IntegerField(choices=list_of_categories, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
