from django.contrib import admin
from .models import Post, Author

admin.site.register(Post, Author)
