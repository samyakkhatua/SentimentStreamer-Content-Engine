from fastapi import FastAPI
from enum import Enum
import random
from pydantic import BaseModel 
from typing import List, Dict

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],  
)
class AvailableOptions(str, Enum):
    happy = "happy"
    sad = "sad"
    neutral = "neutral"
    excited = "excited"
    surprised = "surprised"
    angry = "angry"
    fear = "fear"
    

class MoodResponse(BaseModel):
    mood: AvailableOptions
    # movie:List[str]
    playlists: List[str]
    videos: List[str]
    articles:List[str]
    suggestions:List[str]
    

videos = {
   


'angry ': [
    "https://www.imdb.com/title/tt1392190/",
    "https://www.imdb.com/title/tt0137523/",
    "https://www.imdb.com/title/tt0172495/",
    "https://www.imdb.com/title/tt2911666/",
    "https://www.imdb.com/title/tt1853728/",
    "https://www.imdb.com/title/tt0468569/",
    "https://www.imdb.com/title/tt0110912/",
    "https://www.imdb.com/title/tt0133093/",
    "https://www.imdb.com/title/tt0361748/",
    "https://www.imdb.com/title/tt0266697/",
    # Add more movies here
],

'disgust' : [
    "https://www.imdb.com/title/tt1467304/",
    "https://www.imdb.com/title/tt0180093/",
    "https://www.imdb.com/title/tt0066921/",
    "https://www.imdb.com/title/tt0387564/",
    "https://www.imdb.com/title/tt0450278/",
    "https://www.imdb.com/title/tt0870984/",
    "https://www.imdb.com/title/tt0091064/",
    "https://www.imdb.com/title/tt0069089/",
    "https://www.imdb.com/title/tt0073650/",
    "https://www.imdb.com/title/tt0290673/",
    # Add more movies here
],

'fear' : [
    "https://www.imdb.com/title/tt1457767/",
    "https://www.imdb.com/title/tt7784604/",
    "https://www.imdb.com/title/tt0087800/",
    "https://www.imdb.com/title/tt0070047/",
    "https://www.imdb.com/title/tt0081505/",
    "https://www.imdb.com/title/tt5052448/",
    "https://www.imdb.com/title/tt3235888/",
    "https://www.imdb.com/title/tt1179904/",
    "https://www.imdb.com/title/tt2321549/",
    "https://www.imdb.com/title/tt0298130/",
    # Add more movies here
],

'happy': [
    "https://www.imdb.com/title/tt0109830/",
    "https://www.imdb.com/title/tt1675434/",
    "https://www.imdb.com/title/tt0211915/",
    "https://www.imdb.com/title/tt3783958/",
    "https://www.imdb.com/title/tt2278388/",
    "https://www.imdb.com/title/tt0449059/",
    "https://www.imdb.com/title/tt0454921/",
    "https://www.imdb.com/title/tt1045658/",
    "https://www.imdb.com/title/tt1049413/",
    "https://www.imdb.com/title/tt2096673/",
    # Add more movies here
],

'neutral' : [
    "https://www.imdb.com/title/tt0111161/",
    "https://www.imdb.com/title/tt0068646/",
    "https://www.imdb.com/title/tt0108052/",
    "https://www.imdb.com/title/tt0167260/",
    "https://www.imdb.com/title/tt0060196/",
    "https://www.imdb.com/title/tt1375666/",
    "https://www.imdb.com/title/tt0109830/",
    "https://www.imdb.com/title/tt0137523/",
    "https://www.imdb.com/title/tt0133093/",
    "https://www.imdb.com/title/tt0099685/",
    # Add more movies here
],

'sad' : [
    "https://www.imdb.com/title/tt0108052/",
    "https://www.imdb.com/title/tt0095327/",
    "https://www.imdb.com/title/tt0120689/",
    "https://www.imdb.com/title/tt0180093/",
    "https://www.imdb.com/title/tt0783233/",
    "https://www.imdb.com/title/tt0253474/",
    "https://www.imdb.com/title/tt4034228/",
    "https://www.imdb.com/title/tt2024544/",
    "https://www.imdb.com/title/tt1120985/",
    "https://www.imdb.com/title/tt0388795/",
    # Add more movies here
],

'surprise' : [
    "https://www.imdb.com/title/tt0167404/",
    "https://www.imdb.com/title/tt0137523/",
    "https://www.imdb.com/title/tt0114814/",
    "https://www.imdb.com/title/tt2267998/",
    "https://www.imdb.com/title/tt0209144/",
    "https://www.imdb.com/title/tt0364569/",
    "https://www.imdb.com/title/tt0482571/",
    "https://www.imdb.com/title/tt1130884/",
    "https://www.imdb.com/title/tt0114369/",
    "https://www.imdb.com/title/tt0117381/",
    # Add more movies here
],
}




playlists = {
    'angry': [
       "https://open.spotify.com/track/1dGr1c8CrMLDpV6mPbImSI",
        "https://open.spotify.com/track/2MuWTIM3b0YEAskbeeFE1i",
        "https://open.spotify.com/track/0NWPxcsf5vdjdiFUI8NgkP",
        "https://open.spotify.com/track/3xXBsjrbG1xQIm1xv1cKOt",
        "https://open.spotify.com/track/5fVZC9GiM4e8vu99W0Xf6J",
        "https://open.spotify.com/track/5sICkBXVmaCQk5aISGR3x1",
        "https://open.spotify.com/track/5sICkBXVmaCQk5aISGR3x1",
        "https://open.spotify.com/track/3ZffCQKLFLUvYM59XKLbVm",
        "https://open.spotify.com/track/4VqPOruhp5EdPBeR92t6lQ",
        "https://open.spotify.com/track/7Ie9W94M7OjPoZVV216Xus",
        "https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9",
        "https://open.spotify.com/track/6QgjcU0zLnzq5OrUoSZ3OK",
        "https://open.spotify.com/track/2nLtzopw4rPReszdYBJU6h",
        "https://open.spotify.com/track/7w87IxuO7BDcJ3YUqCyMTT",
        "https://open.spotify.com/track/4Ce37cRWvM1vIGGynKcs22",
        "https://open.spotify.com/track/3S7HNKPakdwNEBFIVTL6dZ",
        "https://open.spotify.com/track/1rgnBhdG2JDFTbYkYRZAku",
        "https://open.spotify.com/track/3jjujdWJ72nww5eGnfs2E7",
        "https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m",
        "https://open.spotify.com/track/3ZFTkvIE7kyPt6Nu3PEa7V",
        "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC"
    ],
    'disgust': [
        "https://open.spotify.com/track/3e9HZxeyfWwjeyPAMmWSSQ",
    "https://open.spotify.com/track/5b88tNINg4Q4nrRbrCXUmg",
    "https://open.spotify.com/track/3z8h0TU7ReDPLIbEnYhWZb",
    "https://open.spotify.com/track/7w87IxuO7BDcJ3YUqCyMTT",
    "https://open.spotify.com/track/1rgnBhdG2JDFTbYkYRZAku",
    "https://open.spotify.com/track/3e9HZxeyfWwjeyPAMmWSSQ",
    "https://open.spotify.com/track/2d7LPtieXdIYzf7yHPooWd",
    "https://open.spotify.com/track/4aWmUDTfIPGksMNLV2rQP2",
    "https://open.spotify.com/track/4umIPjkehX1r7uhmGvXiSV",
    "https://open.spotify.com/track/2takcwOaAZWiXQijPHIx7B",
    "https://open.spotify.com/track/7e89621JPkKaeDSTQ3avtg",
    "https://open.spotify.com/track/6brl7bwOHmGFkNw3MBqssT",
    "https://open.spotify.com/track/2d8JP84HNLKhmd6IYOoupQ",
    "https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR",
    "https://open.spotify.com/track/5yY9lUy8nbvjM1Uyo1Uqoc",
    "https://open.spotify.com/track/4VqPOruhp5EdPBeR92t6lQ"
    ],
    'fear': [
        "https://open.spotify.com/track/3d9DChrdc6BOeFsbrZ3Is0",
    "https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9",
    "https://open.spotify.com/track/2iuZJX9X9P0GKaE93xcPjk",
    "https://open.spotify.com/track/3U21A07gAloCc4P7J8rxcn",
    "https://open.spotify.com/track/1dGr1c8CrMLDpV6mPbImSI",
    "https://open.spotify.com/track/463CkQjx2Zk1yXoBuierM9",
    "https://open.spotify.com/track/3z8h0TU7ReDPLIbEnYhWZb",
    "https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b",
    "https://open.spotify.com/track/40riOy7x9W7GXjyGp4pjAv",
    "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3",
    "https://open.spotify.com/track/3AszgPDZd9q0DpDFt4HFBy",
    "https://open.spotify.com/track/2d8JP84HNLKhmd6IYOoupQ",
    "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",
    "https://open.spotify.com/track/0Oe49j06Bjrxs8PltuVeaW",
    "https://open.spotify.com/track/7FIWs0pqAYbP91WWM0vlTQ",
    "https://open.spotify.com/track/4eWQlBRaTjPPUlzacqEeoQ"
    ],
    'happy': [
       "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",
    "https://open.spotify.com/track/6QgjcU0zLnzq5OrUoSZ3OK",
    "https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR",
    "https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9",
    "https://open.spotify.com/track/4iJyoBOLtHqaGxP12qzhQI",
    "https://open.spotify.com/track/6Qs4SXO9dwPj5GKvVOv8Ki",
    "https://open.spotify.com/track/2DEZmgHKAvm41k4J3R2E9Y",
    "https://open.spotify.com/track/5T8EDUDqKcs6OSOwEsfqG7",
    "https://open.spotify.com/track/4RVwu0g32PAqgUiJoXsdF8",
    "https://open.spotify.com/track/7szuecWAPwGoV1e5vGu8tl",
    "https://open.spotify.com/track/6I3mqTwhRpn34SLVafSH7G",
    "https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf",
    "https://open.spotify.com/track/2takcwOaAZWiXQijPHIx7B",
    "https://open.spotify.com/track/7yq4Qj7cqayVTp3FF9CWbm",
    "https://open.spotify.com/track/1Je1IMUlBXcx1Fz0WE7oPT",
    "https://open.spotify.com/track/6xtcFXSo8H9BZN637BMVKS",
    "https://open.spotify.com/track/6DCZcSspjsKoFjzjrWoCdn",
    "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3",
    "https://open.spotify.com/track/5oO3drDxtziYU2H1X23ZIp" 
    ],
    'neutral': [
          "https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR",
    "https://open.spotify.com/track/0k664IuFwVP557Gnx7RhIl",
    "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3",
    "https://open.spotify.com/track/3ZFTkvIE7kyPt6Nu3PEa7V",
    "https://open.spotify.com/track/6LsAAHotRLMOHfCsSfYCsz",
    "https://open.spotify.com/track/1zHlj4dQ8ZAtrayhuDDmkY",
    "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",
    "https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v",
    "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",
    "https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v",
    "https://open.spotify.com/track/6LsAAHotRLMOHfCsSfYCsz",
    "https://open.spotify.com/track/5HCyWlXZPP0y6Gqq8TgA20",
    "https://open.spotify.com/track/2dpaYNEQHiRxtZbfNsse99",
    "https://open.spotify.com/track/4iJyoBOLtHqaGxP12qzhQI",
    "https://open.spotify.com/track/0hNduWmlWmEmuwEFcYvRu1",
    "https://open.spotify.com/track/0ofHAoxe9vBkTCp2UQIavz"
    ],
    'sad': [
         "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7a",
    "https://open.spotify.com/track/0k664IuFwVP557Gnx7RhIl",
    "https://open.spotify.com/track/5hc71nKsUgtwQ3z52KEKQk",
    "https://open.spotify.com/track/4E6cwWJWZw2zWf7VFbH7wf",
    "https://open.spotify.com/track/5yY9lUy8nbvjM1Uyo1Uqoc",
    "https://open.spotify.com/track/7mWFF4gPADjTQjC97CgFVt",
    "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7a",
    "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp",
    "https://open.spotify.com/track/1i1fxkWeaMmKEB4T7zqbzK",
    "https://open.spotify.com/track/6b8Be6ljOzmkOmFslEb23P",
    "https://open.spotify.com/track/7fBv7CLKzipRk6EC6TWHOB",
    "https://open.spotify.com/track/0TK2YIli7K1leLovkQiNik",
    "https://open.spotify.com/track/6I9VzXrHxO9rA9A5euc8Ak",
    "https://open.spotify.com/track/0r7CVbZTWZgbTCYdfa2P31",
    "https://open.spotify.com/track/7aiClxsDWFRQ0Kzk5KI5ku",
    "https://open.spotify.com/track/2takcwOaAZWiXQijPHIx7B",
    "https://open.spotify.com/track/6jG2YzhxptolDzLHTGLt7S",
    "https://open.spotify.com/track/0ofHAoxe9vBkTCp2UQIavz"
    ],
    'surprised': [
        "https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9",
    "https://open.spotify.com/track/6RUKPb4LETWmmr3iAEQktW",
    "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",
    "https://open.spotify.com/track/5OCJzvD7sykQEKHH7qAC3C",
    "https://open.spotify.com/track/0k664IuFwVP557Gnx7RhIl",
    "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7a",
    "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT",
    "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC",
    "https://open.spotify.com/track/6RRNNciQGZEXnqk8SQ9yv5",
    "https://open.spotify.com/track/0r7CVbZTWZgbTCYdfa2P31",
    "https://open.spotify.com/track/3U21A07gAloCc4P7J8rxcn",
    "https://open.spotify.com/track/0e7ipj03S05BNilyu5bRzt",
    "https://open.spotify.com/track/3eekarcy7kvN4yt5ZFzltW",
    "https://open.spotify.com/track/4RVtBlHFKj51Ipvpfv5ER4",
    "https://open.spotify.com/track/7aiClxsDWFRQ0Kzk5KI5ku",
    "https://open.spotify.com/track/3RiPr603aXAoi4GHyXx0uy",
    "https://open.spotify.com/track/4iV5W9uYEdYUVa79Axb7Rh",
    "https://open.spotify.com/track/5yY9lUy8nbvjM1Uyo1Uqoc"
    ],
}

articles= {
  'angry' : [
    "https://www.psychologytoday.com/us/basics/anger",
    "https://www.verywellmind.com/anger-management-4157185",
    "https://www.healthline.com/health/why-am-i-always-angry",
    "https://www.nami.org/Blogs/NAMI-Blog/January-2020/The-Role-of-Anger-in-Mental-Health",
    "https://www.verywellmind.com/anger-management-strategies-4178871",
    "https://www.psychologytoday.com/us/blog/prescriptions-life/202103/overcoming-fear",
    "https://www.verywellmind.com/understanding-sadness-4799491",
    "https://www.psychologytoday.com/us/basics/sadness",
    "https://www.helpguide.org/articles/grief/coping-with-grief-and-loss.htm",
   
 ],
 'disgust' : [
    "https://www.psychologytoday.com/us/basics/disgust",
    "https://www.verywellmind.com/what-is-disgust-2794971",
    "https://www.verywellmind.com/the-psychology-of-disgust-2671614",
    "https://www.sciencedaily.com/releases/2017/06/170620141215.htm",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3712191/",
    "https://www.psychologytoday.com/us/basics/fear",
    "https://www.verywellmind.com/what-is-fear-2795237",
    "https://www.health.harvard.edu/staying-healthy/the-biology-of-fear",
    "https://www.webmd.com/anxiety-panic/guide/mental-health-fear",
    "https://adaa.org/understanding-anxiety/facts-statistics"
 ],
 'fear' : [
    "https://www.psychologytoday.com/us/basics/fear",
    "https://www.verywellmind.com/what-is-fear-2795237",
    "https://www.health.harvard.edu/staying-healthy/the-biology-of-fear",
    "https://www.webmd.com/anxiety-panic/guide/mental-health-fear",
    "https://adaa.org/understanding-anxiety/facts-statistics",
    "https://www.psychologytoday.com/us/basics/happiness",
    "https://www.verywellmind.com/what-is-happiness-4869767",
    "https://www.helpguide.org/articles/mental-health/the-pursuit-of-happiness.htm",
    "https://www.healthline.com/health/positive-thinking",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6258755/"
 ],
 'happy' : [
    "https://www.psychologytoday.com/us/basics/happiness",
    "https://www.verywellmind.com/what-is-happiness-4869767",
    "https://www.helpguide.org/articles/mental-health/the-pursuit-of-happiness.htm",
    "https://www.healthline.com/health/positive-thinking",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6258755/",
    "https://www.psychologytoday.com/us/basics/emotional-neutrality",
    "https://www.verywellmind.com/emotional-neutrality-4772841",
    "https://www.lifehack.org/289585/8-ways-stay-neutral-your-emotions",
    "https://www.betterhelp.com/advice/general/why-being-neutral-can-be-beneficial-finding-balance-in-your-emotions/",
    "https://www.psychologytoday.com/us/blog/emotional-nourishment/201801/the-art-emotional-neutrality"
 ],
 'sad' : [
    "https://www.psychologytoday.com/us/basics/happiness",
    "https://www.verywellmind.com/what-is-happiness-4869767",
    "https://www.helpguide.org/articles/mental-health/the-pursuit-of-happiness.htm",
    "https://www.healthline.com/health/positive-thinking",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6258755/",
    "https://www.psychologytoday.com/us/basics/emotional-neutrality",
    "https://www.verywellmind.com/emotional-neutrality-4772841",
    "https://www.lifehack.org/289585/8-ways-stay-neutral-your-emotions",
    "https://www.betterhelp.com/advice/general/why-being-neutral-can-be-beneficial-finding-balance-in-your-emotions/",
    "https://www.psychologytoday.com/us/blog/emotional-nourishment/201801/the-art-emotional-neutrality"
 ],
 'neutral' :[
    "https://www.psychologytoday.com/us/basics/emotional-neutrality",
    "https://www.verywellmind.com/emotional-neutrality-4772841",
    "https://www.lifehack.org/289585/8-ways-stay-neutral-your-emotions",
    "https://www.betterhelp.com/advice/general/why-being-neutral-can-be-beneficial-finding-balance-in-your-emotions/",
    "https://www.psychologytoday.com/us/blog/emotional-nourishment/201801/the-art-emotional-neutrality",
    "https://www.verywellmind.com/understanding-surprise-2795097",
    "https://www.psychologytoday.com/us/basics/surprise",
    "https://www.sciencedaily.com/releases/2011/04/110406161651.htm",
    "https://www.fastcompany.com/3033692/the-power-of-surprise-how-surprise-can-lead-to-creativity-and-innovation"
   
   ],
}

mood_suggestions = {
    'angry': [
        "Encourage physical activity like going for a walk or hitting the gym to release pent-up energy.",
        "Suggest journaling to express and process feelings in a constructive way.",
        "Practice mindfulness or meditation to regain composure and perspective.",
        "Recommend seeking anger management therapy or classes for long-term management.",
        "Explore creative outlets like painting, writing, or music to channel intense emotions positively.",
        "Stay calm and avoid escalating the situation.",
        "Listen actively to understand their perspective.",
        "Validate their feelings without necessarily agreeing with their actions.",
        "Offer to take a break from the conversation if it's getting too heated.",
        "Suggest deep breathing or other relaxation techniques."
    ],
    'disgust': [
        "Offer to help find solutions to the source of their disgust.",
        "Encourage them to focus on what they can control rather than what disgusts them.",
        "Suggest relaxation techniques like progressive muscle relaxation or aromatherapy.",
        "Share stories or examples of overcoming similar feelings of disgust.",
        "Recommend seeking professional help if disgust leads to significant distress or impairment.",
        "Respect their boundaries and personal space.",
        "Avoid engaging in behaviors or discussions that trigger their disgust.",
        "Redirect the conversation to a more neutral or positive topic.",
        "Offer support if they're dealing with something particularly unpleasant.",
        "Avoid judgment and try to empathize with their perspective."
    ],
    'fear': [
        "Help them create a plan to gradually confront their fears through exposure therapy.",
        "Encourage physical activity or exercise to reduce the physiological symptoms of fear.",
        "Suggest reading books or watching movies that address overcoming fear.",
        "Offer to accompany them to appointments or situations that provoke fear.",
        "Practice grounding techniques like naming objects in the environment to reduce anxiety.",
        "Offer reassurance and support.",
        "Encourage them to express their fears and concerns openly.",
        "Help them identify specific steps they can take to address their fears.",
        "Offer to accompany them if they need to confront something they're afraid of.",
        "Suggest relaxation techniques like deep breathing or mindfulness exercises."
    ],
    'happy': [
        "Capture the moment with a photo or video to cherish later.",
        "Plan a surprise or spontaneous adventure to amplify their happiness.",
        "Express gratitude for their positive energy and its impact on those around them.",
        "Share stories or memories that reinforce their happiness.",
        "Encourage them to spread their joy by doing something kind for others.",
        "Share in their happiness and celebrate their achievements.",
        "Offer congratulations or compliments.",
        "Listen attentively as they share their good news or positive experiences.",
        "Plan a small celebration or outing to further enhance their mood.",
        "Express gratitude for their positive energy and presence."
    ],
    'neutral': [
        "Share something exciting or unexpected to elicit a reaction.",
        "Ask open-ended questions to prompt deeper conversation and engagement.",
        "Offer to do something out of the ordinary together to break the neutral state.",
        "Recommend trying new experiences or hobbies to add excitement to their life.",
        "Express genuine interest and curiosity in their thoughts and feelings.",
        "Engage them in conversation to see if there's something on their mind.",
        "Suggest activities or topics that might spark their interest.",
        "Share something interesting or exciting to see if it elicits a response.",
        "Respect their desire for space if they seem content with their current state.",
        "Offer support if they seem neutral due to underlying concerns or stress."
    ],
    'sad': [
        "Provide comfort through physical touch like a hug or holding their hand.",
        "Suggest volunteering or helping others as a way to find purpose and fulfillment.",
        "Encourage them to seek professional help if sadness persists or interferes with daily life.",
        "Share uplifting stories, quotes, or videos to inspire hope and optimism.",
        "Offer practical help with tasks or responsibilities to lighten their load.",
        "Offer a listening ear and emotional support.",
        "Avoid dismissing or minimizing their feelings.",
        "Encourage them to express their emotions openly.",
        "Suggest activities or hobbies that might lift their spirits.",
        "Offer to spend time together doing something they enjoy."
    ],
    'surprised': [
        "Reflect on the surprise together and discuss its implications or significance.",
        "Encourage them to embrace the unexpected and see it as an opportunity for growth.",
        "Share personal stories of past surprises and how they were handled.",
        "Explore ways to turn the surprise into a positive outcome or learning experience.",
        "Offer support and reassurance as they navigate the unfamiliar territory.",
        "Acknowledge their surprise and ask if they're okay.",
        "Offer support or assistance if their surprise is related to a problem or unexpected event.",
        "Share in their excitement if their surprise is positive.",
        "Use humor to lighten the mood if appropriate.",
        "Offer to help them process their surprise or adjust to the new information."
    ]
}




#FastApi IMPLEMENTATION
@app.get("/mood/{mood}", response_model=MoodResponse)
async def get_mood_content(mood: AvailableOptions):
   # random.sample(list,k)
   # random.sample(happy,4)
    selected_videos = random.sample(videos[mood.value], min(6, len(videos[mood.value])))
    selected_suggestions = random.sample(mood_suggestions[mood.value], min(2, len(mood_suggestions[mood.value])))
    selected_playlists = random.sample(playlists[mood.value], min(6, len(playlists[mood.value])))
    selected_articles = random.sample(articles[mood.value], min(2, len(articles[mood.value])))

    return MoodResponse(
        mood=mood,
        videos=selected_videos,
        playlists=selected_playlists,
        suggestions=selected_suggestions,
        articles=selected_articles
    )
