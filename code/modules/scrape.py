#imports
import requests
import time

import pandas as pd

#function to scrape a subreddit
def scrape_reddit(subreddit, kind, iterations, epoch = int(time.time()), file = None):
    """
    subreddit : subreddit to scrape

    kind : scrape "submission"(posts) OR "comment"(comments)

    iterations : number of times to scrape
                 100 posts scraped per iteration

    epoch : begin scraping before this epoch. defaults to epoch of time at import
    """
    #cnt flag iterations at while loop, status code set to 200 to initiate while loop
    cnt = 0
    status_code = 200
    
    #url for api call to pushshift and parameters passed to api
    url_requested = "https://api.pushshift.io/reddit/search/" + kind
    params = {
        "subreddit" : subreddit,
        "size"      : 100,
        "before"    : epoch
    }
    
    #If no file is provided creates a new DF, else file is provided adds posts to file
    #prior to the timestamp of the last observation
    if file == None:
        subreddit_df = pd.DataFrame()
    else:
        subreddit_df = pd.read_csv(file)
        params["before"] = subreddit_df["created_utc"].iloc[-1] - 1

    while status_code == 200 and cnt < iterations:
        #wait 2 + 1 seconds throughout loop
        time.sleep(2)

        #make http request to pushshift
        res = requests.get(url_requested, params)
        status_code = res.status_code
        if status_code != 200:
            raise ValueError(f"status code: {status_code}. After {cnt} iterations.")
        
        #100 entries returned and extracted
        data = res.json()
        posts = data["data"]

        #data to pandas df
        #timestamp of last entry set as time to scrape before for next iter
        posts_df = pd.DataFrame(posts)
        params["before"] = posts_df["created_utc"].iloc[-1] - 1

        #add 1 iteration of observation to DF
        subreddit_df = pd.concat([subreddit_df, posts_df], ignore_index=True)
        subreddit_df.to_csv("../data/r_" + subreddit + "_data/raw_" + subreddit + "_data.csv", index=False)
        
        #print count and number of rows
        if cnt % 10 == 0:
            print(f"{cnt + 1} iterations complete {subreddit}_data.csv has {subreddit_df.shape[0]} rows") 
        cnt += 1
        
        #wait +1 second
        time.sleep(1)

    return subreddit_df
