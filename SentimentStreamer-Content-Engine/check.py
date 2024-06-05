import requests

def check_links(links):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    working_links = []
    non_working_links = []
    
    for link in links:
        try:
            response = requests.get(link, headers=headers)
            if response.status_code == 200:
                working_links.append(link)
            else:
                non_working_links.append(link)
        except requests.exceptions.RequestException as e:
            non_working_links.append(link)
    
    return working_links, non_working_links

all_links = [
   "https://open.spotify.com/track/4l2WzFLrGNHLuvd7Uo0kn1",  # "Creep" - Radiohead
        "https://open.spotify.com/track/2takcwOaAZWiXQijPHIx7B",  # "Toxic" - Britney Spears
        "https://open.spotify.com/track/1JLi6I09H4eVPC6eQNeA7c",  # "Sick and Tired" - Anastacia
        "https://open.spotify.com/track/7e89621JPkKaeDSTQ3avtg",  # "Sadda Haq" - Rockstar (Hindi)
        "https://open.spotify.com/track/4tX2TplrkIP4v05BNC903e",  # "Hate That I Love You" - Rihanna ft. Ne-Yo
        "https://open.spotify.com/track/1zR5wWcEjPjgoWhjuqXIGz",  # "Love The Way You Lie" - Eminem ft. Rihanna
        "https://open.spotify.com/track/1MSbgVtEnWk4roAnTgBeD6",  # "You're Beautiful" - James Blunt
        "https://open.spotify.com/track/1y8NXRk8YiHxxIodSmuJrH",  # "Gives You Hell" - The All-American Rejects
        "https://open.spotify.com/track/4EZz8Y0Il70ulNk1lP0LoZ",  # "Rolling in the Deep" - Adele
        "https://open.spotify.com/track/6brl7bwOHmGFkNw3MBqssT",  # "I Don't Care" - Ed Sheeran & Justin Bieber
        "https://open.spotify.com/track/2d8JP84HNLKhmd6IYOoupQ",  # "Somebody's Watching Me" - Rockwell
        "https://open.spotify.com/track/0LOJjYmHp8b2K73C0fvLgA",  # "Bad Guy" - Billie Eilish
        "https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR",  # "Shape of You" - Ed Sheeran
        "https://open.spotify.com/track/0pd24Y7HLPykA3xs3e2ReF",  # "Dark Horse" - Katy Perry
        "https://open.spotify.com/track/4SZko61aMnmgvNhfhgTuD3",  # "Uptown Funk" - Mark Ronson ft. Bruno Mars
        "https://open.spotify.com/track/3zTLaA6KtyAwwk0Pl8ViJP",  # "Somebody That I Used To Know" - Gotye
        "https://open.spotify.com/track/7qn6mFhI60CWf9AqFqUVHk",  # "Don't Let Me Down" - The Chainsmokers
        "https://open.spotify.com/track/5oE5z39G8MqltMZB8W8ZJb",  # "I Hate U I Love U" - gnash
        "https://open.spotify.com/track/5yY9lUy8nbvjM1Uyo1Uqoc",  # "Lucid Dreams" - Juice WRLD
        "https://open.spotify.com/track/4VqPOruhp5EdPBeR92t6lQ"  # "Shallow" - Lady Gaga & Bradley Cooper
   
]



working_links, non_working_links = check_links(all_links)

print("Working links:")
for link in working_links:
    print(link)

print("\nNon-working links:")
for link in non_working_links:
    print(link)



