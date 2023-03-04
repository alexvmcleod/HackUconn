import praw
import requests
import time
import os

reddit = praw.Reddit(client_id='rcfAWEQk1GwMhzrNMdIhAQ',
                     client_secret='_vx-2JowOVa5-E22LR0h8bYmVerMNA',
                     username='alexmcleoduconn',
                     password='HackUConn1',
                     user_agent='HackUConn')

def download_post(post_id,subreddit="otherstuff"):
    post = reddit.submission(id=post_id)
    
    
    print('downloading!')
    # Download the first image from the post's media
    image_url = post.url
    print(image_url)
    
    #thing = str(image_url)
    if str(image_url)[-4:] == '.jpg' or str(image_url)[-4:] == '.png':
        image_response = requests.get(image_url)
        with open(f'images/{subreddit}/{post_id}.png', 'wb') as f:
            f.write(image_response.content)
        return 0
    else:
        print(f"Post '{post_id}' is not a suitable image!")
        return 1
    # with open(f'images/{subreddit}/{post_id}.png', 'wb') as f:
    #          f.write(image_response.content)
    # return 0


def scrapesubreddit(subredditname,imagelen=100):
    #creates folder for images if none exists
    folder_path = os.path.join('images',subredditname)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    image_count = 0
    subreddit = reddit.subreddit(subredditname)
    for submission in subreddit.hot(limit=imagelen):
        if download_post(submission.id,subredditname) == 0: image_count += 1
    print(f"{image_count} images downloaded!")

def add_metadata(image,upvotes,subreddit):
    pass

# start = time.time()
# for i in range(100):
#     download_post('11hm8ez',i)
# end = time.time()

# print(end-start)


start = time.time()
scrapesubreddit('aiArt',100)
end = time.time()
print(end-start)
