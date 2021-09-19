from django.db import models

# tabela ogłoszeniodawców

class User(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.IntegerField(null=True)
    email = models.CharField(max_length=64, unique=True)


# tabela kategorii usług

list_of_categories = ((1, 'odzież'),
                      (2, 'motoryzacja'),
                      (3, 'usługi'),
                      (4, 'żywność'))

class Category(models.Model):
    name = models.IntegerField(choices=list_of_categories)

# tabela ogłoszeń

class Ad(models.Model):
    title = models.CharField(max_length=64, null=True)
    content = models.TextField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
