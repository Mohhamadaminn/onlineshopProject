from django.db import models

from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
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


class ActiveCustomManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCustomManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_POINTS = [
        ('1', _('Very Bad!')),
        ('2', _('Bad')),
        ('3', _('Not Bad')),
        ('4', _('Good')),
        ('5', _('Perfect!')),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_('Comment Text'))
    points = models.CharField(max_length=10,
                               choices=PRODUCT_POINTS,
                               verbose_name=_('what is your score?'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCustomManager()

    class Meta:
        ordering = ['date_modified']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.product.id})
    
    