from reddit_interface import RedditInterface
from finance_utils import TickerProcessor 
import timeit

MINIMUM_POST_SCORE = 10

def filter_post(post):
    if post.score < MINIMUM_POST_SCORE:
        return True
    return False

def main():
    start = timeit.timeit()

    print("Hello World!")
    reddit = RedditInterface()
    ticketProcessor = TickerProcessor()
    posts = reddit.fetchTodayPosts("wallstreetbets")

    posts_dict = {}
    count = 0
    for post in posts:
        print(post, post.title, post.selftext, post.score )
        count = count + 1

        if filter_post(post):
            continue

        posts_dict[post.id] = {post.selftext, post.score}
        ticketProcessor.parseTickers(post.title)
        ticketProcessor.parseTickers(post.selftext)

        ticketProcessor.dump()
    ticketProcessor.dump()


    print(f'Fetched {count} number of posts. Kept {len(posts_dict)} posts')

    end = timeit.timeit()
    print(end - start)

if __name__ == "__main__":
    main()