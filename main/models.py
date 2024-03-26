from django.db import models

# Create your models here.

class Contact(models.Model):
    FirstName = models.CharField(max_length=122)
    LastName = models.CharField(max_length=122)
    Email = models.EmailField(max_length=122)
    Message = models.CharField(max_length=112)


    def __str__(self):
        self.name = self.FirstName + " " + self.LastName
        return self.name
    


class Blogs(models.Model):
    BlogTitle = models.CharField(max_length=122)
    BlogContent = models.TextField()
    BlogPublishDate = models.DateField()

    def __str__(self):
        self.name = self.BlogTitle
        return self.name
    
