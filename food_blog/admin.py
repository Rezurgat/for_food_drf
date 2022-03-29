from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models

#добавление возможности написания рецепта сразу при создании поста
class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1 #кол-во объявляемых рецептов



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'post_author', 'when_create', 'id']
    inlines = [RecipeInline]
    save_as = True #чтобы кнопка сохранения была и вверху ...
    save_on_top = True #.. и внизу

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cooking_time', 'post']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'website', 'id', 'when_create']

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)

