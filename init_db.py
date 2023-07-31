from weblog import app, db
from weblog import User, Post, Tag, pst_tag
from faker import Faker
import random

fake = Faker()
with app.app_context():
    db.drop_all()
    db.create_all()

roles = ['Author', 'Admin', 'Editor']
tags_name = ['Sports', 'Political', 'AI', 'Technology', 'Finance', 'Entertainment']

users = []
tags = []
posts = []
post_tags1 = []

for _ in range(10):
    user = User(name=fake.name(), username=fake.name(), password=fake.password(), role=random.choice(roles))
    users.append(user)
    tag = Tag(name=random.choice(tags_name))
    tags.append(tag)

for _ in range(30):
    post = Post(title=fake.word(), content=fake.sentence(), author=random.choice(users)
    )
    posts.append(post)

for pst in posts:
    current_tags = random.sample(tags, 2)
    post.labels = current_tags
    

with app.app_context():
    db.session.add_all(users)
    db.session.add_all(tags)
    db.session.add_all(posts)
    db.session.add_all(post_tags1)
    db.session.commit()