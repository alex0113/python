from reddit_interface import RedditInterface

MINIMUM_POST_SCORE = 100

def filter_post(post):
    if post.score < MINIMUM_POST_SCORE:
        return True
    return False
def main():
    print("Hello World!")
    reddit = RedditInterface()
    posts = reddit.fetchTodayPosts("wallstreetbets")

    posts_dict = {}
    count = 0
    for post in posts:
        print(post, post.title, post.score )
        count = count + 1

        if filter_post(post):
            continue

        posts_dict[post.id] = {post.selftext, post.score}

    print(f'Fetched {count} number of posts. Kept {len(posts_dict)} posts')

if __name__ == "__main__":
    main()