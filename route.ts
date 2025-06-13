// import { redditRequest } from 'reddit';
// Replace the above line with the correct import path or implement redditRequest below if missing

// Example implementation (replace with actual logic or correct import as needed)
async function redditRequest(subreddit: string, limit: number) {
    // Placeholder: Replace with actual Reddit API call logic
    return {
        data: {
            posts: [
                // Example data
                { title: "Example post", subreddit, limit }
            ]
        }
    };
}
export async function redditRoute(req, res) {
    try {
        let { subreddit, limit } = req.query;

        if (!subreddit) {
            return res.status(400).json({ error: 'Subreddit is required' });
        }

        if (!limit) {
            limit = 10; // Default limit if not provided
        }

        const response = await redditRequest(subreddit, limit);
        return res.status(200).json(response.data);
    } catch (error) {
        console.error('Error fetching data from reddit:', error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
}