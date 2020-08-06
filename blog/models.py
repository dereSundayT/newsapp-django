from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    cat_slug = models.SlugField(max_length=140, unique=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_image = models.ImageField(default='noimage.jpg', upload_to='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)
    view = models.IntegerField(default=0)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)
    contents = models.TextField()

    def __str__(self):
        return f"{ self.user.username } ' commented ' on this Post: {self.post.title}"
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
