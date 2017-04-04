from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

# Create your models here.

def book_cover_upload_path(instance, filename):
    return '/'.join(['books', str(instance.id), filename])
def misc_cover_upload_path(instance, filename):
    return '/'.join(['misc', str(instance.id), filename])
def apparel_cover_upload_path(instance, filename):
    return '/'.join(['apparel', str(instance.id), filename])
def trick_cover_upload_path(instance, filename):
    return '/'.join(['trick', str(instance.id), filename])
def act_cover_upload_path(instance, filename):
    return '/'.join(['act', str(instance.id), filename])


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

class TrickType(models.Model):
    type = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % (self.type)

class ActStyle(models.Model):
    style = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % (self.style)

class Difficulty(models.Model):
    rating = models.TextField(max_length=200)

    def __unicode__(self):
        return "%s" % (self.rating)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    quantity = models.IntegerField(default = 0)
    cover_image = models.ImageField(upload_to=book_cover_upload_path, default='image_not_available.jpg')

class Item(models.Model):
    title = models.CharField(max_length=200, default='Website')

class Misc(models.Model):
    title = models.CharField(max_length=200)
    designer = models.CharField(max_length=200)
    type = models.ForeignKey(MiscType)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    quantity = models.IntegerField(default = 0)
    cover_image = models.ImageField(upload_to=misc_cover_upload_path, default='image_not_available.jpg')

class Apparel(models.Model):
    title = models.CharField(max_length=200)
    designer = models.CharField(max_length=200)
    type = models.ForeignKey(ApparelType)
    size = models.ForeignKey(ApparelSize)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    quantity = models.IntegerField(default = 0)
    cover_image = models.ImageField(upload_to=apparel_cover_upload_path, default='image_not_available.jpg')

class Trick(models.Model):
    title = models.CharField(max_length=200)
    designer = models.CharField(max_length=200)
    type = models.ForeignKey(TrickType)
    difficulty = models.ForeignKey(Difficulty)
    video = EmbedVideoField()
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    quantity = models.IntegerField(default = 0)
    cover_image = models.ImageField(upload_to=trick_cover_upload_path, default='image_not_available.jpg')

class Act(models.Model):
    name = models.CharField(max_length=200)
    style = models.ForeignKey(ActStyle)
    restaurant = models.BooleanField(default=False)
    stage = models.BooleanField(default=False)
    close_up = models.BooleanField(default=False)
    bio = models.TextField()
    speciality = models.CharField(max_length=200, default='All-Rounder')
    image = models.ImageField(upload_to=act_cover_upload_path, default='image_not_available.jpg')
    website = models.CharField(max_length=200, default='http://localhost:8000/compendiummagic/')

class Review(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()

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

class ReviewTrick(models.Model):
    trick = models.ForeignKey(Trick)
    user = models.ForeignKey(User)
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()

class Cart(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

    def add_to_cart(self, item_id, item_classifier):
        if item_classifier == 1:
            item = Book.objects.get(pk=item_id)
            try:
                preexisting_order = BookOrder.objects.get(item=item, cart=self)
                preexisting_order.quantity += 1
                preexisting_order.save()

            except BookOrder.DoesNotExist:
                new_order = BookOrder.objects.create(
                    item=item,
                    cart=self,
                    quantity=1
                )
                new_order.save()

        elif item_classifier == 2:
            item = Misc.objects.get(pk=item_id)
            try:
                preexisting_order = MiscOrder.objects.get(item=item, cart=self)
                preexisting_order.quantity += 1
                preexisting_order.save()

            except MiscOrder.DoesNotExist:
                new_order = MiscOrder.objects.create(
                    item=item,
                    cart=self,
                    quantity=1
                )
                new_order.save()

        elif item_classifier == 3:
            item = Apparel.objects.get(pk=item_id)
            try:
                preexisting_order = ApparelOrder.objects.get(item=item, cart=self)
                preexisting_order.quantity += 1
                preexisting_order.save()

            except ApparelOrder.DoesNotExist:
                new_order = ApparelOrder.objects.create(
                    item=item,
                    cart=self,
                    quantity=1
                )
                new_order.save()

        elif item_classifier == 4:
            item = Trick.objects.get(pk=item_id)
            try:
                preexisting_order = TrickOrder.objects.get(item=item, cart=self)
                preexisting_order.quantity += 1
                preexisting_order.save()

            except TrickOrder.DoesNotExist:
                new_order = TrickOrder.objects.create(
                    item=item,
                    cart=self,
                    quantity=1
                )
                new_order.save()

    def remove_from_cart(self, item_id, item_classifier):
        if item_classifier == 1:
            item = Book.objects.get(pk=item_id)
            try:
                preexisting_order = BookOrder.objects.get(item=item, cart=self)
                if preexisting_order.quantity > 1:
                    preexisting_order.quantity -= 1
                    preexisting_order.save()
                else:
                    preexisting_order.delete()
            except BookOrder.DoesNotExist:
                pass

        elif item_classifier == 2:
            item = Misc.objects.get(pk=item_id)
            try:
                preexisting_order = MiscOrder.objects.get(item=item, cart=self)
                if preexisting_order.quantity > 1:
                    preexisting_order.quantity -= 1
                    preexisting_order.save()
                else:
                    preexisting_order.delete()
            except MiscOrder.DoesNotExist:
                pass

        elif item_classifier == 3:
            item = Apparel.objects.get(pk=item_id)
            try:
                preexisting_order = ApparelOrder.objects.get(item=item, cart=self)
                if preexisting_order.quantity > 1:
                    preexisting_order.quantity -= 1
                    preexisting_order.save()
                else:
                    preexisting_order.delete()
            except ApparelOrder.DoesNotExist:
                pass

        elif item_classifier == 4:
            item = Trick.objects.get(pk=item_id)
            try:
                preexisting_order = TrickOrder.objects.get(item=item, cart=self)
                if preexisting_order.quantity > 1:
                    preexisting_order.quantity -= 1
                    preexisting_order.save()
                else:
                    preexisting_order.delete()
            except TrickOrder.DoesNotExist:
                pass


class BookOrder(models.Model):
    item = models.ForeignKey(Book)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()


class MiscOrder(models.Model):
    item = models.ForeignKey(Misc)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()


class ApparelOrder(models.Model):
    item = models.ForeignKey(Apparel)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()

class TrickOrder(models.Model):
    item = models.ForeignKey(Trick)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()