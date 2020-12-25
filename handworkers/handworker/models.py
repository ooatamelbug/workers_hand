from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=200, blank=False)
    ar_title = models.CharField(max_length=200, blank=False)
    desc = models.TextField(blank=True)
    ar_desc = models.TextField(blank=True)
    image_base = models.ImageField(default='default.png', blank=False)
    views = models.IntegerField(blank=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    """Home"""
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)
    image_base = models.ImageField(max_length=200, blank=False)
    desc = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    """Category"""
    def __str__(self):
        return self.name


class Governorate(models.Model):
    name = models.CharField(max_length=200, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    """Governorate"""
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200, blank=False)
    governorate = models.ForeignKey('Governorate', on_delete=models.CASCADE, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    """City"""
    def __str__(self):
        return self.name


class Workers(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=250, blank=False)
    governorate = models.ForeignKey('Governorate', on_delete=models.CASCADE, blank=False)
    city = models.ForeignKey('City', on_delete=models.CASCADE, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=False)
    desc = models.TextField(blank=True)
    rate = models.IntegerField(default=0, blank=True)
    total_rate = models.IntegerField(default=0, blank=True)
    work_time = models.TextField(blank=False)
    is_aviable = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    """Workers"""
    def __str__(self):
        return self.name


class RateWorkers(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    status = models.BooleanField(default=False, blank=False)
    text = models.TextField(blank=False)
    rate = models.IntegerField(blank=False)
    worker = models.ForeignKey('Workers', on_delete=models.CASCADE, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    """City"""
    def __str__(self):
        return self.name


class Phone(models.Model):
    number = models.CharField(max_length=11, blank=False)
    worker = models.ForeignKey('Workers', on_delete=models.CASCADE, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    """City"""
    def __str__(self):
        return self.number


