import praw

# Replace with your Reddit app credentials
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="trendscout by /u/YOUR_USERNAME"
)

def scrape_reddit_posts(query, limit=20):
    subreddit = reddit.subreddit("all")
    results = subreddit.search(query, limit=limit)
    for post in results:
        print(f"Title: {post.title}\nUpvotes: {post.score}\nURL: {post.url}\n")

if __name__ == "__main__":
    scrape_reddit_posts("your business idea")
