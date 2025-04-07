#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import db, Author, Post

fake = Faker()

with app.app_context():
    
    Post.query.delete()
    Author.query.delete()

    authors = []
    for n in range(25):
        author = Author(
            name=fake.unique.name(),
            phone_number=fake.numerify('##########')
        )
        authors.append(author)

    db.session.add_all(authors)

    
    posts = []
    clickbait_phrases = ["Won't Believe", "Secret", "Top", "Guess"]
    categories = ['Fiction', 'Non-Fiction']
    
    for n in range(25):
        post = Post(
            title=f"{rc(clickbait_phrases)} {fake.sentence()}",
            content=fake.text(max_nb_chars=2000),  
            category=rc(categories),
            summary=fake.text(max_nb_chars=250)
        )
        posts.append(post)

    db.session.add_all(posts)
    db.session.commit()