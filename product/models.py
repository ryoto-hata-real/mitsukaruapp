from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from mainapp.models import User

SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]
class Product(models.Model):
    picture = models.ImageField(default='images/no_image.png',blank=True,upload_to='images')
    ad_image = models.TextField(default="",max_length=1500,blank=True)
    title = models.CharField(max_length=100)
    producer = models.CharField(default="",max_length=50)
    contents = models.TextField(default="", max_length=1000, blank=True)
    language_tags = models.TextField(default="",max_length=500, blank=True)
    level_tags = models.TextField(default="",max_length=500, blank=True)
    content_tags = models.TextField(default="",max_length=500, blank=True)
    urls = models.TextField(max_length=1000,default="",blank=True)
    price = models.IntegerField(default=0,blank=False)
    score = models.FloatField(default=0.0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title



class LevelTagMaster(models.Model):
    level_tag_name = models.CharField(max_length=15)
    def __str__(self):
        return self.level_tag_name

class LanguageTagMaster(models.Model):
    language_tag_name = models.CharField(max_length=15)
    def __str__(self):
        return self.language_tag_name

class ContentTagMaster(models.Model):
    content_tag_name = models.CharField(max_length=15)
    def __str__(self):
        return self.content_tag_name


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='review')
    review = models.TextField(max_length=500)
    score = models.PositiveSmallIntegerField(verbose_name='レビュースコア', choices=SCORE_CHOICES, default='3')
    user_id = models.ForeignKey(User,default="", on_delete=models.CASCADE, verbose_name='投稿ユーザ')
    created_at = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.review
