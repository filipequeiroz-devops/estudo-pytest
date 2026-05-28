import requests
import pandas as pd


def main():
    url      = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data     = response.json()
    df       = pd.DataFrame(data)
    
    return df

if __name__ == "__main__":
    main()