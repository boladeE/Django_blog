import json

from django.contrib.auth.models import User

from blog_app.models import Post

users = User.objects.all()
with open("posts.json") as file:
    posts = json.load(file)

for post in posts:
    post = Post(title=post["title"], content=post["content"], user_id=users[0].id)
    post.save()
