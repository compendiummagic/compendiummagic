from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

def book_cover_upload_path(instance, filename):
    return '/'.join(['books', str(instance.id), filename])
def misc_cover_upload_path(instance, filename):
    return '/'.join(['misc', str(instance.id), filename])
def apparel_cover_upload_path(instance, filename):
    return '/'.join(['apparel', str(instance.id), filename])

class ApparelType(models.Model):
    type = models.CharField(max_length=200)
    def __unicode__(self):
        return "%s" % (self.type)

class ApparelSize(models.Model):
    size = models.CharField(max_length=200)
    def __unicode__(self):
        return "%s" % (self.size)

class MiscType(models.Model):
    type = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % (self.type)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    quantity = models.IntegerField(default = 0)
    cover_image = models.ImageField(upload_to=book_cover_upload_path, default='books/image_not_available.jpg')

class Misc(models.Model):
    title = models.CharField(max_length=200)
    designer = models.CharField(max_length=200)
    type = models.ForeignKey(MiscType)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    quantity = models.IntegerField(default = 0)
    cover_image = models.ImageField(upload_to=misc_cover_upload_path, default='misc/image_not_available.jpg')

class Apparel(models.Model):
    title = models.CharField(max_length=200)
    designer = models.CharField(max_length=200)
    type = models.ForeignKey(ApparelType)
    size = models.ForeignKey(ApparelSize)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    quantity = models.IntegerField(default = 0)
    cover_image = models.ImageField(upload_to=apparel_cover_upload_path, default='apparel/image_not_available.jpg')

class ReviewBook(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()

class ReviewMisc(models.Model):
    misc = models.ForeignKey(Misc)
    user = models.ForeignKey(User)
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()

class ReviewApparel(models.Model):
    apparel = models.ForeignKey(Apparel)
    user = models.ForeignKey(User)
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()
