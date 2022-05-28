from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter

# make new database in model with this code and then use makemigration for make
# migration file and save the data and the migrate
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name = "عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "آدرس دسته بندی")
    status = models.BooleanField(default=True,verbose_name="آیا نمایش داده شود؟")
    positioning = models.IntegerField(verbose_name="پوزیشن")
   
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندیها"   
        ordering = ["positioning"] 

    def __str__(self):
        return self.title       



class Article(models.Model):
    STATUS_CHOICES = (
        ("d", 'پیش نویس'),
        ("p", 'منتشر شده'),
    )
    title = models.CharField(max_length=200, verbose_name = "عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندیها", related_name="articles")
    description = models.TextField(verbose_name = "محتوا")
    thumbnail = models.ImageField(upload_to='images', verbose_name = "تصویر مقاله")
    published = models.DateField(default=timezone.now, verbose_name = "زمان انتشار")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name = "وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-published"] 

    def __str__(self):
        return self.title        # we use this for make the title in admin just like title/ برای نشان دادن سر مقاله برای اسم مقاله

    def jpublish(self):
        return jalali_converter(self.published)    