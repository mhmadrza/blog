from unicodedata import category
from django.contrib import admin
# for add Article in the admin page / آدرس قرار گیری مقالات
from .models import Article, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('positioning', 'title', 'slug', 'status')          
    list_filter = (['status'])                             
    search_fields = ('title', 'slug')                      
    prepopulated_fields = {'slug': ('title',)}                      

admin.site.register(Category, CategoryAdmin)

# for set a new option on the article panel  / اضافه کردن انتخاب های جدید در صفحه مقالات در ادمین پنل
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'status', 'Category_to_str')            #در این بخش به کمک این می توانید در لیست مقالات از اطلاعات دیگر با خبر شوید
    list_filter = ('published', 'status')                             # برای فیلتر کردن اطلاعات
    search_fields = ('title', 'description')                         #برای فیلد سرچ در بالا 
    prepopulated_fields = {'slug': ('title',)}                      #پر شدن فیلد سمعل به صورت خودکار 
    ordering = ['-status', 'published']                            #ترتیب قرار گیری در لیست مقالات 

    def Category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])   
    Category_to_str.short_description = 'دسته بندی'


# for register and put article in admin site / برای قرار دادن صفحه مقالات در ادمین
admin.site.register(Article, ArticleAdmin)