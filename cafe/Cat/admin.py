from django.contrib import admin
from .models import Table, Reservation, Recipe


admin.site.register(Table)
admin.site.register(Reservation)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_ingredients', 'description', 'photo')
    readonly_fields = ('display_ingredients',)

    def display_ingredients(self, obj):
        ingredients_list = obj.get_ingredients_list()
        if ingredients_list:
            return '<ul>{}</ul>'.format(''.join('<li>{}</li>'.format(ingredient) for ingredient in ingredients_list))
        else:
            return ''

    display_ingredients.allow_tags = True
    display_ingredients.short_description = 'Ingredients'

admin.site.register(Recipe, RecipeAdmin)