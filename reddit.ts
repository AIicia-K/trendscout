export async function redditRequest(subreddit: string, limit: number) {
    // Placeholder implementation, replace with actual Reddit API call
    return {
        status: (code: number) => ({
            json: (data: any) => ({ code, data })
        }),
        data: { subreddit, limit }
    };
}