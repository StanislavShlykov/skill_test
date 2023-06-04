from new_blog.models import *


user1 = User.objects.create_user('Boris')
user2 = User.objects.create_user('Ivan')
user3 = User.objects.create_user('Sasha')

auth1 = Author.objects.create(user=user1)
auth2 = Author.objects.create(user=user2)

cat1 = Category.objects.create(cat_name='образование')
cat2 = Category.objects.create(cat_name='спорт')
cat3 = Category.objects.create(cat_name='история')
cat4 = Category.objects.create(cat_name='политика')

post1 = Post.objects.create(author=auth1, post_name='название', post_rating=10)
post2 = Post.objects.create(author=auth2, post_name='название', post_rating=15)
post3 = Post.objects.create(author = auth2,type = True, post_name = 'название', post_rating=1)

post1.category.add(cat1)
post1.category.add(cat2)
post2.category.add(cat2)
post2.category.add(cat3)
post3.category.add(cat3)
post3.category.add(cat4)

com1 = Comment.objects.create(post=post1, user=user1, text='плохой коммент', com_rating = 5)
com2 = Comment.objects.create(post=post2, user=user2, text='плохой коммент', com_rating = 4)
com3 = Comment.objects.create(post=post3, user=user3, text='плохой коммент', com_rating = 2)
com4 = Comment.objects.create(post=post2, user=user1, text='плохой коммент', com_rating = 10)

com1.like()
com1.like()
com2.like()
com3.dislike()

post1.dislike()
post2.like()
post3.like()
post3.like()

auth1.update_rating()
auth2.update_rating()

best_auth= Author.objects.order_by('-rating')[0]
User.objects.get(id=best_auth.user_id).username
best_auth.rating

best_post= Post.objects.order_by('-post_rating')[0]
best_post.time_in
User.objects.get(id=best_post.author.user_id).username
best_post.post_rating
best_post.post_name
best_post.preview()

# комменты к статье

best_post.comment_set.all().values('com_date', 'user_id', 'com_rating', 'text')


