from django.db import models

from django.shortcuts import reverse

from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_created = models.TimeField(auto_now_add=True)
    datetime_modified = models.TimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])



class Comment(models.Model):
    PRODUCT_POINTS = [
        ('1', 'Very Bad!'),
        ('2', 'Bad'),
        ('3', 'Not Bad'),
        ('4', 'Good'),
        ('5', 'Perfect!'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    points = models.CharField(max_length=10, choices=PRODUCT_POINTS)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_modified']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
    