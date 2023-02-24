import pafy 
import pandas as pd 

df = pd.read_excel('input.xlsx')
urls = df['url']
len = len(urls)
line = 1
err = 0
result_lst = []
for url in urls:
    try:
        yvideo = pafy.new(url)  
        yvalue = yvideo.viewcount
        result_lst.append(yvalue)
        print(str(len - line) + " remaining")
        line += 1 
    except Exception:
        print(str(len - line) + " remaining")
        line += 1 
        result_lst.append("N/A")

result_series = pd.Series(result_lst)
result_series.index = urls
result_df = pd.DataFrame({"view": result_series})
result_df.to_excel("output.xlsx")
print(result_df)