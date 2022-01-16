from django.db import models

# Create your models here.
class State(models.Model):
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return self.state_name

class Course(models.Model):
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return self.course_name


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    enrolled = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

