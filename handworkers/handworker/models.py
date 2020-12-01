from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=200)
    ar_title = models.CharField(max_length=200)
    desc = models.TextField()
    ar_desc = models.TextField()
    image_base = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    """Home"""
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)
    image_base = models.CharField(max_length=200)
    desc = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    """Category"""
    def __str__(self):
        return self.name


class Governorate(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    """Governorate"""
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    governorate = models.ForeignKey('Governorate', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    """City"""
    def __str__(self):
        return self.name


class Workers(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    governorate = models.ForeignKey('Governorate', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    desc = models.TextField()
    rate = models.IntegerField(default=0)
    total_rate = models.IntegerField(default=0)
    work_time = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    """Workers"""
    def __str__(self):
        return self.name


class RateWorkers(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    text = models.TextField()
    rate = models.IntegerField()
    worker = models.ForeignKey('Workers', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    """City"""
    def __str__(self):
        return self.name


class Phone(models.Model):
    number = models.CharField(max_length=200)
    worker = models.ForeignKey('Workers', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    """City"""
    def __str__(self):
        return self.name


