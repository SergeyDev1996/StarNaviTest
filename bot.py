import os
import django
import random
import string
import json

from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StarNaviTest2.settings")
django.setup()
from post.models import Post, Like

User = get_user_model()


def generate_random_string(length):
    """Generate a random string of given length."""
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def create_users(number_of_users):
    """Create the specified number of user."""
    users = []
    for _ in range(number_of_users):
        username = generate_random_string(10)
        email = f"{username}@example.com"
        password = generate_random_string(10)
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        users.append(user)
    return users


def create_posts(users, max_posts_per_user):
    """Create random posts for each user."""
    posts = []
    for user in users:
        num_posts = random.randint(1, max_posts_per_user)
        for _ in range(num_posts):
            text = generate_random_string(10)
            post = Post.objects.create(
                user=user, text=text
            )
            posts.append(post)
    return posts


def like_posts(users, posts, max_likes_per_user):
    """Like random posts for each user."""
    for user in users:
        num_likes = random.randint(1, max_likes_per_user)
        liked_posts = random.sample(posts, num_likes)
        for post in liked_posts:
            Like.objects.create(user=user, post=post)


if __name__ == "__main__":
    # Read the configuration from a file (e.g., JSON)
    config_file = "bot_config.json"
    with open(config_file, "r") as f:
        config = json.load(f)

    number_of_users_config = config["number_of_users"]
    max_posts_per_user_config = config["max_posts_per_user"]
    max_likes_per_user_config = config["max_likes_per_user"]

    # Create user
    created_users = create_users(number_of_users_config)

    # Create posts
    created_posts = create_posts(created_users, max_posts_per_user_config)

    # Like posts
    like_posts(created_users, created_posts, max_likes_per_user_config)
    print("The bot finished it's job.")
