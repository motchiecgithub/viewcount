from TikTokApi import TikTokApi
import re
import pandas as pd
import time
start_time = time.time()
api = TikTokApi()
df = pd.read_excel("input.xlsx")

# create time 
create_time = []

# commentCount
comment = []
# diggCount
like = []
# playCount
view = []
# shareCount
share = []

urls = df['url']
length = len(urls)
count = 1
for url in urls:
    print("there are " + str(length - count) + " urls remaining")
    count += 1
    try:    
        source = api.video(url= url)
        stats = source.stats
        create_time.append(source.create_time)
        comment.append(stats['commentCount'])
        like.append(stats['diggCount'])
        view.append(stats['playCount'])
        share.append(stats['shareCount'])
    except Exception:
        create_time.append("N/A")
        comment.append("N/A")
        like.append("N/A")
        view.append("N/A")
        share.append("N/A")

# view
view_series = pd.Series(view)
view_series.index = urls
# like
like_series = pd.Series(like)
like_series.index = urls

# comment
comment_series = pd.Series(comment)
comment_series.index = urls
# share
share_series = pd.Series(share)
share_series.index = urls

# create time 
create_time_series = pd.Series(create_time)
create_time_series.index = urls
result_df = pd.DataFrame({  'create_time': create_time_series,
                            'view': view_series,
                            'like': like_series,
                            'comment': comment_series,
                            'share': share_series})

result_df.to_excel("output.xlsx")
print('this program has run successfully in ' + str (time.time() - start_time))