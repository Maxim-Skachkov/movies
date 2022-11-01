from django.contrib import admin

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}

from .models import *
admin.site.register(Category, MovieAdmin)
admin.site.register(Person, MovieAdmin)
admin.site.register(Genre, MovieAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots, MovieAdmin)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Review)
