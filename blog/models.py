from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProfileDate(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    body = models.TextField()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title


