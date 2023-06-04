from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

name = [
    (False, 'Статья'),
    (True, 'Новость')
]

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        rating1 = 0
        rating2 = 0
        rating3 = 0
        au_us_id = self.user_id
        posts_ex = Post.objects.exclude(author_id=self.id)
        for i in self.post_set.all().values():
            rating1 += i['post_rating']*3
        for i in self.post_set.all():
            for j in i.comment_set.all().values():
                rating2 += j['com_rating']
        for i in posts_ex:
            for m in i.comment_set.all().filter(user_id = au_us_id).values():
                rating3 += m['com_rating']
        self.rating = rating1+rating2+rating3
        self.save()


class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.BooleanField(default=False, choices=name)  # False = статья, можно переделать, если будет больше вариантов
    time_in = models.TimeField(auto_now_add=True)
    post_name = models.CharField(max_length=100)
    post_text = models.TextField(default="Тут должен быть контент, а будет абракадабра, для проверки задания: ываываываф ыафыаываывфа ываф ываф ывп фывп фвап фвп выа фывп фыва выа ыфвп выа фыв афвыа ывф.")
    post_rating = models.IntegerField(default=0)

    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        if self.post_rating > 0:
            self.post_rating -= 1
            self.save()

    def preview(self):
        return self.post_text[:123] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    com_date = models.DateTimeField(auto_now_add=True)
    com_rating = models.IntegerField(default=0)

    def like(self):
        self.com_rating += 1
        self.save()

    def dislike(self):
        if self.com_rating > 0:
            self.com_rating -= 1
            self.save()