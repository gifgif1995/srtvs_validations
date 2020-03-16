from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be a minimum of at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network needs to be at least 3 characters"
        if len(postData['description']) <10:
            errors["description"] = "Description needs to be at least 10 characters long"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=250)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = ShowManager()

    def __repr__(self):
        return f"Show ID: ({self.id}) | Title: {self.title} | Network: {self.network} | Release Date: {self.release_date} | Description: {self.description} ||"

