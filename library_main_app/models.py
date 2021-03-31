from django.db import models

# Create your models here.

class Books(models.Model):

    ISBN_NUM = models.CharField(max_length=50)
    BOOKS_NAME= models.CharField(max_length=100)
    AUTHORS = models.TextField()
    AVAILABLE_COPIES= models.IntegerField()
    
    def __str__(self):
        return self.BOOKS_NAME


class Readers(models.Model):
    READERS_NAME = models.CharField(max_length=30)
    READERS_ID = models.CharField(max_length=30)
    Book = models.ForeignKey(Books,on_delete=models.CASCADE,related_name="ReadBy")
    BORROW_DATE = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.READERS_NAME