from django.db import models

# Create your models here.
from django.db import models

# możliwe kategorie ogłoszeń

list_of_categories = ((0, 'inne'),
                      (1, 'odzież'),
                      (2, 'motoryzacja'),
                      (3, 'usługi'),
                      (4, 'żywność'),
                      (5, 'sport'),
                      (6, 'nauka'),)


# tabela ogłoszeń
class Ad(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(null=True)
    category = models.IntegerField(choices=list_of_categories, default=0)
    contact = models.TextField()
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.title
