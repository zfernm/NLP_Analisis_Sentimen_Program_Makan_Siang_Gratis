import tweepy
from textblob import TextBlob
import pandas as pd
import re
import time

bearer_token = "UPLOAD_BEARER_TOKEN_ANDA"

client = tweepy.Client(bearer_token=bearer_token)

def clean_tweet(tweet):
    tweet = re.sub(r"http\S+", "", tweet) 
    tweet = re.sub(r"@\S+", "", tweet)    
    tweet = re.sub(r"#", "", tweet)     
    tweet = re.sub(r"RT\s+", "", tweet)  
    tweet = re.sub(r"\s+", " ", tweet)   
    return tweet.strip().capitalize()

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

def scrape_tweets_v2(query, max_results=50):
    try:
        tweets_data = []
        next_token = None

        while len(tweets_data) < max_results:
            response = client.search_recent_tweets(
                query=query,
                max_results=10,  
                next_token=next_token,  
                tweet_fields=["text"]  
            )
            tweets = response.data
            meta = response.meta

            if tweets:
                for tweet in tweets:
                    clean_text = clean_tweet(tweet.text)
                    sentiment = analyze_sentiment(clean_text)
                    tweets_data.append({
                        "Tweet": clean_text,
                        "Sentiment": sentiment
                    })

                next_token = meta.get("next_token", None)
                if not next_token:
                    break  
            else:
                break  

            time.sleep(2)  

        return pd.DataFrame(tweets_data)

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    keyword = "Program Makan Siang Gratis"  
    max_tweets = 9  

    print("Fetching tweets...")
    tweets_df = scrape_tweets_v2(keyword, max_tweets)

    if tweets_df is not None:
        print("Tweets fetched successfully!")
        print(tweets_df.head())

        tweets_df.to_csv("program_makan_siang_gratis_1.csv", index=False)
        print("Saved to 'program_makan_siang_gratis_1.csv'")
    else:
        print("No tweets fetched.")
