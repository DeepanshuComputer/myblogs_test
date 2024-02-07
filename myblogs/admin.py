from django.contrib import admin
from.models import Blog_Category , contact_info , blog_posts, comment

# Register your models here.
admin.site.register(Blog_Category)
admin.site.register(contact_info)
admin.site.register(blog_posts)         #now
admin.site.register(comment)