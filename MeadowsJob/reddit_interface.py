import praw

class RedditInterface:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id="COPr4q4mxzW6YA",
            client_secret="CAVBQILSMs4FZhsC4cuB-9Mk7wNcdA",
            password="hug0nam1",
            user_agent="alex0113",
            username="alex0113",
        )
        print(f'Logged in using user: {self.reddit.user.me()}')

    def fetchTodayPosts(self, subreddit):
        subreddit = self.reddit.subreddit(subreddit)
        return subreddit.top("day", limit = None)



    