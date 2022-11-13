from reddit_interface import RedditInterface
from finance_utils import TickerProcessor 
from mail_sender import EmailSender
from report_generator import genReport

import timeit

SKIP_WORDS_FILE = "SkipWords.txt"
MINIMUM_POST_SCORE = 20
TICKER_POPULARITY_THRESHOLD = 3

def filter_post(post):
    if post.score < MINIMUM_POST_SCORE:
        return True
    return False

def main():
    start = timeit.default_timer()



    print("Hello World!")

    f = open(SKIP_WORDS_FILE, "r")
    skipWords = f.read().split()

    reddit = RedditInterface()
    ticketProcessor = TickerProcessor(TICKER_POPULARITY_THRESHOLD, skipWords)
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
    rez = ticketProcessor.fetchEnrichedValidTickers()
    for ticket in rez:
        print(ticket)


    print(f'Fetched {count} number of posts. Kept {len(posts_dict)} posts')

    report = genReport(rez)
    emailSender = EmailSender()
    emailSender.sendEmail(report)


    end = timeit.default_timer()
    print(end - start)

if __name__ == "__main__":
    main()