from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy
from django.db import models

class Category(MPTTModel):
    name = models.CharField(
        max_length = 100
    )
    slug = models.SlugField(
        max_length = 150, 
        unique = True
    )
    is_active = models.BooleanField(
        default = False
    )
    parent = TreeForeignKey(
        "self",
        on_delete = models.PROTECT,
        related_name = "children",
        null = True,
        blank = True,
    )
    
    class MTTMeta:
        order_insertion_by = ['name']
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("categories")
    
    def __str__(self):
        return self.name


class Product(models.Model):
    web_id = models.CharField(
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        max_length=255
    )
    name = models.CharField(
        max_length=255
    )
    description = models.TextField(
        blank = True
    )
    Category = models.ForeignKey(
        Category,
        related_name = "product",
        default = 1,
        on_delete=models.SET_DEFAULT,
        null = True,
        blank = True
    )
    is_active = models.BooleanField(
        default = False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return self.name