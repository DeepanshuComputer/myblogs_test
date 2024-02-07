from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog_Category(models.Model):
    blog_cat = models.CharField(max_length=60, unique=True)
    blog_img = models.ImageField(upload_to='images/')
    blog_description=models.CharField(max_length=1000)
    
    def __str__(self):
            return self.blog_cat
    
class contact_info(models.Model):
    u_email = models.EmailField()
    u_message = models.CharField(max_length=200 )
    def __str__(self):
        return self.u_email


class blog_posts(models.Model):
    blog_name =models.CharField(max_length=100)
    cover_img=models.ImageField(upload_to='images/')
    blog_description=RichTextField()
    blog_cat=models.ForeignKey(Blog_Category,on_delete=models.CASCADE)
    like_count=models.IntegerField(default=0, null=True)
    views_count=models.IntegerField(default=0, null=True)

    blog_cat=models.ForeignKey(Blog_Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.blog_name
    

class comment(models.Model):
    comment_email = models.EmailField(max_length=100)
    comment_info = models.CharField(max_length=100)
    comment_id = models.ForeignKey(blog_posts,null=True, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_email