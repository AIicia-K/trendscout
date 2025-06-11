import praw
reddit = praw.reddit(
    client_id = sjII952alCaHVwQ0eOXm0g
client_secret = 	d7GJcpAMI1K4zioQUjz8ajT4IX6QAw
user_agent = "trendscout by /u/Intrepid_Letterhead5"
)
def scrape_reddit_posts(query, limit=20):
    subreddit = reddit.subreddit(all)
    results = subreddit.search(query, limiit=limit)
    for post in results:
        print("Title: "+ post.title + "\nUpvotes: " + str(post.score) + "\nURL: " + post.url + "\n")

        if __name__ == "__main__":
            scrape_reddit_posts("AI tutors", limit=20)
            import praw
            
