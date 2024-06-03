from fastapi import FastAPI
from enum import Enum
import random
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

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
    videos: List[str]
    playlists: List[str]
    articles:List[str]
    suggestions:List[str]
    

emotions = {
    'happy': [
        "Happy Upbeat Music: https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Feel Good Songs: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "Uplifting Pop Hits: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Joyful Dance Music: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Positive Energy Playlist: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Happy Acoustic Songs: https://www.youtube.com/watch?v=K0ibBPhiaG0",
        "Cheerful Indie Music: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Feel Good Music Mix: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Joyful Pop Songs: https://www.youtube.com/watch?v=fRh_vgS2dFE",
        "Happy Vibes Playlist: https://www.youtube.com/watch?v=QjoJMQs7Mmw",
        "Upbeat Songs for a Good Mood: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Positive Thinking Music: https://www.youtube.com/watch?v=k7s68X4AtpE",
        "Feel Good Dance Music: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "Joyful Acoustic Guitar: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Happy Pop Music: https://www.youtube.com/watch?v=fRh_vgS2dFE",
        "Cheerful Tunes Playlist: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Upbeat Indie Pop: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Positive Vibes Songs: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Feel Good Electro Music: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Joyful Songs Mix: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Happy Chill Music: https://www.youtube.com/watch?v=QjoJMQs7Mmw",
        "Uplifting Instrumental Music: https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Positive Mood Music: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "Feel Good Pop Hits: https://www.youtube.com/watch?v=fRh_vgS2dFE",
        "Joyful Background Music: https://www.youtube.com/watch?v=K0ibBPhiaG0",
        "Happy Indie Songs: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Upbeat Music for a Good Mood: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Positive Energy Music: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Feel Good Acoustic Music: https://www.youtube.com/watch?v=K0ibBPhiaG0",
        "Joyful Pop Hits: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Happy Songs Playlist: https://www.youtube.com/watch?v=QjoJMQs7Mmw",
        "Uplifting Acoustic Guitar: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Positive Vibes Music: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Feel Good Indie Music: https://www.youtube.com/watch?v=fRh_vgS2dFE",
        "Joyful Dance Hits: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Happy Pop Songs: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Upbeat Chill Music: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "Positive Thinking Songs: https://www.youtube.com/watch?v=k7s68X4AtpE",
        "Feel Good Playlist: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Joyful Electro Music: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Happy Indie Pop: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Upbeat Music Mix: https://www.youtube.com/watch?v=fRh_vgS2dFE",
        "Positive Vibes Playlist: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Feel Good Songs Playlist: https://www.youtube.com/watch?v=QjoJMQs7Mmw",
        "Joyful Acoustic Music: https://www.youtube.com/watch?v=K0ibBPhiaG0",
        "Happy Vibes Music: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Upbeat Pop Songs: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Positive Mood Playlist: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Feel Good Dance Songs: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Joyful Pop Music: https://www.youtube.com/watch?v=fRh_vgS2dFE",
    ],
    'sad': [
        "Sad Piano Music: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Melancholic Acoustic Songs: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Emotional Piano Music: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Sad Instrumental Music: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Sad Indie Songs: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Melancholic Classical Music: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Emotional Acoustic Music: https://www.youtube.com/watch?v=K0ibBPhiaG0",
        "Sad Jazz Music: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Sad Love Songs: https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Sad Guitar Music: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Emotional Classical Music: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Sad Ambient Music: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Sad Pop Songs: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Emotional Indie Music: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Melancholic Instrumental Music: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Sad Piano Playlist: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Emotional Guitar Music: https://www.youtube.com/watch?v=K0ibBPhiaG0",
        "Sad Classical Music Playlist: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Sad Jazz Playlist: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Melancholic Acoustic Playlist: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Emotional Piano Playlist: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Sad Instrumental Playlist: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Sad Indie Playlist: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Melancholic Classical Playlist: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Emotional Acoustic Playlist: https://www.youtube.com/watch?v=K0ibBPhiaG0",
        "Sad Jazz Mix: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Sad Love Songs Mix: https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Melancholic Guitar Playlist: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Sad Piano Instrumentals: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Emotional Classical Playlist: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Sad Ambient Playlist: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Sad Pop Playlist: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Melancholic Indie Music: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Emotional Instrumental Playlist: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Sad Piano Mix: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Melancholic Guitar Songs: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Emotional Classical Mix: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Sad Ambient Mix: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Sad Pop Songs Mix: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Melancholic Indie Playlist: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Emotional Instrumental Mix: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Sad Piano Songs Mix: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Melancholic Classical Mix: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Emotional Guitar Playlist: https://www.youtube.com/watch?v=K0ibBPhiaG0",
        "Sad Classical Music Mix: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Melancholic Jazz Music: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Sad Indie Music Mix: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Emotional Love Songs: https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Melancholic Acoustic Mix: https://www.youtube.com/watch?v=2gMIi7C2DdE",
    ],
    'surprised': [
        "https://www.youtube.com/watch"
    ],
    'excited': [
        "High Energy Music: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Workout Playlist: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "Energetic Dance Music: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Upbeat Pop Hits: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "High Energy Workout Music: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Energetic Rock Music: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Pump Up Songs: https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "Energetic EDM: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Workout Pop Hits: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "High Energy Dance Hits: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Energetic Pop Songs: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Upbeat Workout Music: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "High Energy Rock: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Pump Up Playlist: https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "Energetic Dance Playlist: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Workout Hits Mix: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "High Energy Pop Hits: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Energetic EDM Playlist: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Upbeat Rock Music: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "High Energy Workout Playlist: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Energetic Pop Hits: https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "Pump Up Dance Music: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "High Energy EDM: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Energetic Workout Hits: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Upbeat Pop Music: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "High Energy Dance Playlist: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "Energetic Pop Playlist: https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "Pump Up Rock Music: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "High Energy Workout Mix: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Energetic EDM Mix: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Upbeat Dance Hits: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "High Energy Rock Playlist: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Energetic Pop Mix: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Pump Up Dance Playlist: https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "High Energy EDM Hits: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "Energetic Workout Mix: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Upbeat Pop Playlist: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "High Energy Dance Mix: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Energetic Rock Playlist: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Pump Up Workout Music: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "High Energy Pop Music: https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "Energetic Dance Hits: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "Upbeat EDM: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",
        "High Energy Workout Songs: https://www.youtube.com/watch?v=hT_nvWreIhg",
        "Energetic Pop Dance: https://www.youtube.com/watch?v=PT2_F-1esPk",
        "Pump Up Music Mix: https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "High Energy Rock Hits: https://www.youtube.com/watch?v=VbfpW0pbvaU",
        "Energetic Dance Mix: https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "Upbeat Workout Playlist: https://www.youtube.com/watch?v=wXhTHyIgQ_U",
        "High Energy EDM Playlist: https://www.youtube.com/watch?v=8EJ3zbKTWQ8",

    ],
    'neutral': [
       "Chill Background Music: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Relaxing Ambient Sounds: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Instrumental Chill Playlist: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Calm Study Music: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Easy Listening Music: https://www.youtube.com/watch?v=3jWRrafhO7M",
        "Relaxing Jazz Music: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Mellow Acoustic Songs: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Chillhop Music: https://www.youtube.com/watch?v=5yx6BWlEVcY",
        "Relaxing Piano Music: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Soft Background Music: https://www.youtube.com/watch?v=2DVpys50LVE",
        "Lo-fi Chill Beats: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Ambient Music for Relaxation: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Chill Electronic Music: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Calm Acoustic Guitar: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Relaxing Classical Music: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Easy Listening Jazz: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Mellow Indie Songs: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Chillout Lounge Music: https://www.youtube.com/watch?v=5yx6BWlEVcY",
        "Soft Piano Background: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Relaxing Instrumental Music: https://www.youtube.com/watch?v=2DVpys50LVE",
        "Lo-fi Beats Playlist: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Chill Ambient Music: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Mellow Chill Music: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Calm Study Beats: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Relaxing Acoustic Guitar: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Soft Classical Music: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Easy Listening Lounge: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Mellow Jazz Music: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Chill Indie Playlist: https://www.youtube.com/watch?v=5yx6BWlEVcY",
        "Relaxing Piano Playlist: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Soft Background Beats: https://www.youtube.com/watch?v=2DVpys50LVE",
        "Lo-fi Chill Music: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Calm Ambient Playlist: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Mellow Electronic Music: https://www.youtube.com/watch?v=hHW1oY26kxQ",
        "Chill Acoustic Songs: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Relaxing Jazz Playlist: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Easy Listening Acoustic: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Mellow Classical Music: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Chill Beats for Studying: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Relaxing Lounge Music: https://www.youtube.com/watch?v=5yx6BWlEVcY",
        "Soft Instrumental Playlist: https://www.youtube.com/watch?v=2DVpys50LVE",
        "Lo-fi Hip Hop Beats: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Calm Chill Music: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Mellow Indie Music: https://www.youtube.com/watch?v=2gMIi7C2DdE",
        "Chillout Music Mix: https://www.youtube.com/watch?v=5yx6BWlEVcY",
        "Relaxing Piano Background: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Soft Acoustic Playlist: https://www.youtube.com/watch?v=2DVpys50LVE",
        "Lo-fi Music Mix: https://www.youtube.com/watch?v=5qap5aO4i9A",
        "Calm Relaxation Music: https://www.youtube.com/watch?v=QZbuj3RJcdc",
        "Mellow Background Music: https://www.youtube.com/watch?v=hHW1oY26kxQ",
    ],
    'angry': [
         "Relaxing Piano Music: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Calming Forest Sounds: https://www.youtube.com/watch?v=eKFTSSKCzWA",
        "Guided Meditation for Anger: https://www.youtube.com/watch?v=G_oUrxA9iAc",
        "Soothing Instrumental Music: https://www.youtube.com/watch?v=Mk7dKq3l9BM",
        "Yoga for Anger Release: https://www.youtube.com/watch?v=csO7ZeDxLJY",
        "Peaceful Guitar Music: https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "Deep Breathing Exercises: https://www.youtube.com/watch?v=_mZbzDOpylA",
        "Classical Music for Relaxation: https://www.youtube.com/watch?v=QxHkLdQy5f0",
        "Mindfulness Meditation: https://www.youtube.com/watch?v=ZToicYcHIOU",
        "Nature Sounds for Relaxation: https://www.youtube.com/watch?v=odCOip1Vvjc",
        "Stress Relief Music: https://www.youtube.com/watch?v=97wqQbxH1wI",
        "Anger Management Techniques: https://www.youtube.com/watch?v=xfiJrJWU4D4",
        "Calming Flute Music: https://www.youtube.com/watch?v=K86YzyS_78g",
        "Relaxing Jazz Music: https://www.youtube.com/watch?v=KQU7ntT5mbQ",
        "Ambient Music for Stress Relief: https://www.youtube.com/watch?v=yyL8ShQv2NE",
        "Progressive Muscle Relaxation: https://www.youtube.com/watch?v=ihO02wUzgkc",
        "Chill Out Music: https://www.youtube.com/watch?v=gn1qMYfFrro",
        "Relaxing Harp Music: https://www.youtube.com/watch?v=NuN7wDYCr1I",
        "Tai Chi for Stress Relief: https://www.youtube.com/watch?v=ZuXfFAumIc4",
        "Guided Imagery Meditation: https://www.youtube.com/watch?v=1vx8iUvfyCY",
        "Relaxing Piano Music for Stress Relief: https://www.youtube.com/watch?v=xN6bqYbIZn8",
        "Music for Deep Relaxation: https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "Gentle Yoga for Relaxation: https://www.youtube.com/watch?v=v7AYKMP6rOE",
        "Serene Zen Music: https://www.youtube.com/watch?v=Wl959QnD3lM",
        "Calming Water Sounds: https://www.youtube.com/watch?v=ugDvdGyr2zY",
        "Relaxing Cello Music: https://www.youtube.com/watch?v=hjHo8-K7wkM",
        "Meditative Music: https://www.youtube.com/watch?v=AG_84jqytbs",
        "Emotional Release Meditation: https://www.youtube.com/watch?v=wfDTp2GogaQ",
        "Nature Meditation: https://www.youtube.com/watch?v=ugDvdGyr2zY",
        "Calm Music for Meditation: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Anger Release Yoga: https://www.youtube.com/watch?v=bZrKFSHqRhA",
        "Soothing Background Music: https://www.youtube.com/watch?v=qFZKK7K52uQ",
        "Calming Ocean Waves: https://www.youtube.com/watch?v=VztCEeoO3Yc",
        "Relaxing Piano for Anger: https://www.youtube.com/watch?v=MI2V1PhOjuA",
        "Healing Meditation: https://www.youtube.com/watch?v=wfDTp2GogaQ",
        "Relaxing Music for Sleep: https://www.youtube.com/watch?v=iQ-zi5KqkG8",
        "Stress Management Techniques: https://www.youtube.com/watch?v=xfiJrJWU4D4",
        "Gentle Relaxing Music: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Relaxing Nature Scenes: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "Calming Instrumental Music: https://www.youtube.com/watch?v=WYeDsa4Tw0c",
        "Mindfulness for Anger: https://www.youtube.com/watch?v=Q1EEydWXAXQ",
        "Soft Music for Relaxation: https://www.youtube.com/watch?v=MI2V1PhOjuA",
        "Stress Reduction Meditation: https://www.youtube.com/watch?v=wruCI3bI_OU",
        "Relaxing Guitar for Anger: https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "Deep Relaxation Techniques: https://www.youtube.com/watch?v=ihO02wUzgkc",
        "Yoga Nidra for Stress Relief: https://www.youtube.com/watch?v=csO7ZeDxLJY",
        "Calming Soundscapes: https://www.youtube.com/watch?v=odCOip1Vvjc",
        "Soothing Background Music for Anger: https://www.youtube.com/watch?v=yyL8ShQv2NE",
        "Relaxing Music for Inner Peace: https://www.youtube.com/watch?v=gn1qMYfFrro",
        "Meditation for Anger Management: https://www.youtube.com/watch?v=G_oUrxA9iAc",
       
    ]}





playlists = {
    'angry': [
        "https://open.spotify.com/track/1dGr1c8CrMLDpV6mPbImSI",  # "Smells Like Teen Spirit" - Nirvana
        "https://open.spotify.com/track/2Kh43m04B1UkVcpcRa1Zug",  # "Break Stuff" - Limp Bizkit
        "https://open.spotify.com/track/1a4vY4m6VQltTJoW06Y4p1",  # "So What" - Metallica
        "https://open.spotify.com/track/0NWPxcsf5vdjdiFUI8NgkP",  # "Bring Me to Life" - Evanescence
        "https://open.spotify.com/track/0uUHzfTmKvEh71nGFrmzey",  # "Bhaag DK Bose" - Delhi Belly (Hindi)
        "https://open.spotify.com/track/5xrt93LWWdQ6Jmb2Qm8vQC",  # "Killing In The Name" - Rage Against The Machine
        "https://open.spotify.com/track/6s5MoQnGfs0kFSJ4cwsuX4",  # "Headstrong" - Trapt
        "https://open.spotify.com/track/1JHHF6OCU6XgLUGljfc16z",  # "Enter Sandman" - Metallica
        "https://open.spotify.com/track/2cFrymmkijnjDg9SS92EPM",  # "Duality" - Slipknot
        "https://open.spotify.com/track/3ZffCQKLFLUvYM59XKLbVm",  # "Chop Suey!" - System Of A Down
        "https://open.spotify.com/track/4yHqbL17uBzEJJPU5RZQzQ",  # "Psycho" - Muse
        "https://open.spotify.com/track/5V0MlUE1Bft0mbLlND7FJz",  # "Animal I Have Become" - Three Days Grace
        "https://open.spotify.com/track/1bNxY4Z4kGZxHAJccNQwOU",  # "Before I Forget" - Slipknot
        "https://open.spotify.com/track/2VpZyFEThQbPJWIQS7FgPS",  # "Not Afraid" - Eminem
        "https://open.spotify.com/track/1IueXOQyABrMOprrzwQJWN",  # "Disturbia" - Rihanna
        "https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9",  # "Feel Invincible" - Skillet
        "https://open.spotify.com/track/4eVknU0tIf8jE1M4eWc9Ws",  # "Monster" - Skillet
        "https://open.spotify.com/track/1ej6NQ1PuGDiAMkXr9HMMM",  # "Face Everything and Rise" - Papa Roach
        "https://open.spotify.com/track/1hM1Mcn8f0yspOhDxv5t3j",  # "Given Up" - Linkin Park
        "https://open.spotify.com/track/7w87IxuO7BDcJ3YUqCyMTT",  # "Bulls On Parade" - Rage Against The Machine
    ],
    'disgust': [
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
        "https://open.spotify.com/track/4VqPOruhp5EdPBeR92t6lQ",  # "Shallow" - Lady Gaga & Bradley Cooper
    ],
    'fear': [
        "https://open.spotify.com/track/6M6xD2N4D0oX6K4PrxKlbv",  # "Thriller" - Michael Jackson
        "https://open.spotify.com/track/1IueXOQyABrMOprrzwQJWN",  # "Disturbia" - Rihanna
        "https://open.spotify.com/track/1GlLCna7CzsaIXW4CZ5TPx",  # "Haunted" - Beyoncé
        "https://open.spotify.com/track/3AszgPDZd9q0DpDFt4HFBy",  # "Aao Kabhi Haveli Pe" - Stree (Hindi)
        "https://open.spotify.com/track/2d8JP84HNLKhmd6IYOoupQ",  # "Somebody's Watching Me" - Rockwell
        "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",  # "I Gotta Feeling" - The Black Eyed Peas
        "https://open.spotify.com/track/0uUHzfTmKvEh71nGFrmzey",  # "Bhaag DK Bose" - Delhi Belly (Hindi)
        "https://open.spotify.com/track/4V6fwHD14LEzvVacgO7aWX",  # "Bad Blood" - Taylor Swift ft. Kendrick Lamar
        "https://open.spotify.com/track/0Oe49j06Bjrxs8PltuVeaW",  # "Bohemian Rhapsody" - Queen
        "https://open.spotify.com/track/7FIWs0pqAYbP91WWM0vlTQ",  # "Billie Jean" - Michael Jackson
        "https://open.spotify.com/track/3h5tYJpWsf5rDqdWfZsaBa",  # "Ghost" - Ella Henderson
        "https://open.spotify.com/track/4JE6agDK5H9HpvEZflAOuT",  # "Demons" - Imagine Dragons
        "https://open.spotify.com/track/1jyiiauRYhJ6PL5VSz1dJt",  # "Human" - Christina Perri
        "https://open.spotify.com/track/2Z1D24qhQz0qC2xZ73hEZ8",  # "Cry Baby" - Melanie Martinez
        "https://open.spotify.com/track/7GHjEsjT0sQxDIu0uh5dXk",  # "Dark Horse" - Katy Perry
        "https://open.spotify.com/track/1nYeVF5y9lupHqfKiBNtHQ",  # "Get Out Alive" - Three Days Grace
        "https://open.spotify.com/track/2lbbOpLM98j24UxfwOe4dV",  # "Animals" - Martin Garrix
        "https://open.spotify.com/track/4eWQlBRaTjPPUlzacqEeoQ",  # "Ghostbusters" - Ray Parker Jr.
        "https://open.spotify.com/track/3iJr4a8CwxtCTLDfhgsQoK",  # "Monster" - Imagine Dragons
        "https://open.spotify.com/track/5H3Gcgwohoqtkho2xLsrmA",  # "Bad Moon Rising" - Creedence Clearwater Revival
    ],
    'happy': [
        "https://open.spotify.com/track/6c7U9NggVcArRVznL96CGe",  # "Happy" - Pharrell Williams
        "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",  # "I Gotta Feeling" - The Black Eyed Peas
        "https://open.spotify.com/track/0wjoPOltJ6pTrRZSuXYx8W",  # "Galway Girl" - Ed Sheeran
        "https://open.spotify.com/track/6H7KEPxO4rI7hV62q4ndHY",  # "Subha Hone Na De" - Desi Boyz (Hindi)
        "https://open.spotify.com/track/6QgjcU0zLnzq5OrUoSZ3OK",  # "Best Day of My Life" - American Authors
        "https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR",  # "Shape of You" - Ed Sheeran
        "https://open.spotify.com/track/1MSbgVtEnWk4roAnTgBeD6",  # "You're Beautiful" - James Blunt
        "https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9",  # "Feel Invincible" - Skillet
        "https://open.spotify.com/track/6c7U9NggVcArRVznL96CGe",  # "Happy" - Pharrell Williams
        "https://open.spotify.com/track/4iJyoBOLtHqaGxP12qzhQI",  # "Levitating" - Dua Lipa
        "https://open.spotify.com/track/6Qs4SXO9dwPj5GKvVOv8Ki",  # "Blinding Lights" - The Weeknd
        "https://open.spotify.com/track/5Fw5HhPjdzeFbWv3kXsMvA",  # "Don't Start Now" - Dua Lipa
        "https://open.spotify.com/track/3JVRyPQ34QSo7c5j9c3WGG",  # "Peaches" - Justin Bieber
        "https://open.spotify.com/track/1eHNi74bP2EN8y7rDfkiF9",  # "Save Your Tears" - The Weeknd
        "https://open.spotify.com/track/2DEZmgHKAvm41k4J3R2E9Y",  # "ROXANNE" - Arizona Zervas
        "https://open.spotify.com/track/5T8EDUDqKcs6OSOwEsfqG7",  # "Positions" - Ariana Grande
        "https://open.spotify.com/track/4RVwu0g32PAqgUiJoXsdF8",  # "Happier Than Ever" - Billie Eilish
        "https://open.spotify.com/track/7szuecWAPwGoV1e5vGu8tl",  # "Shivers" - Ed Sheeran
        "https://open.spotify.com/track/6I3mqTwhRpn34SLVafSH7G",  # "STAY" - The Kid LAROI, Justin Bieber
        "https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf",  # "When I Was Your Man" - Bruno Mars
    ],
    'neutral': [
        "https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR",  # "Shape of You" - Ed Sheeran
        "https://open.spotify.com/track/0k664IuFwVP557Gnx7RhIl",  # "Someone Like You" - Adele
        "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3",  # "Despacito" - Luis Fonsi ft. Daddy Yankee
        "https://open.spotify.com/track/4RiKqUDGvcGmpGQ2vDhssF",  # "Kabira" - Yeh Jawaani Hai Deewani (Hindi)
        "https://open.spotify.com/track/3ZFTkvIE7kyPt6Nu3PEa7V",  # "Photograph" - Ed Sheeran
        "https://open.spotify.com/track/6LsAAHotRLMOHfCsSfYCsz",  # "Closer" - The Chainsmokers
        "https://open.spotify.com/track/1zHlj4dQ8ZAtrayhuDDmkY",  # "I'm Yours" - Jason Mraz
        "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",  # "I Gotta Feeling" - The Black Eyed Peas
        "https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v",  # "Lean On" - Major Lazer & DJ Snake
        "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",  # "I Gotta Feeling" - The Black Eyed Peas
        "https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v",  # "Lean On" - Major Lazer & DJ Snake
        "https://open.spotify.com/track/6LsAAHotRLMOHfCsSfYCsz",  # "Closer" - The Chainsmokers
        "https://open.spotify.com/track/2gONQg5E4JlO6GXFsC0A1l",  # "The Nights" - Avicii
        "https://open.spotify.com/track/5HCyWlXZPP0y6Gqq8TgA20",  # "Stressed Out" - Twenty One Pilots
        "https://open.spotify.com/track/2dpaYNEQHiRxtZbfNsse99",  # "Heat Waves" - Glass Animals
        "https://open.spotify.com/track/1E1eyIwtEKaU14xbCU8gkH",  # "Heathens" - Twenty One Pilots
        "https://open.spotify.com/track/4iJyoBOLtHqaGxP12qzhQI",  # "Levitating" - Dua Lipa
        "https://open.spotify.com/track/3XIIOCu2xziABwAQ9JZqKt",  # "Don't Wanna Know" - Maroon 5
        "https://open.spotify.com/track/0hNduWmlWmEmuwEFcYvRu1",  # "Feel It Still" - Portugal. The Man
        "https://open.spotify.com/track/0ofHAoxe9vBkTCp2UQIavz",  # "Sunflower" - Post Malone, Swae Lee
    ],
    'sad': [
        "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7a",  # "Fix You" - Coldplay
        "https://open.spotify.com/track/0k664IuFwVP557Gnx7RhIl",  # "Someone Like You" - Adele
        "https://open.spotify.com/track/6LS6cP1X7eQFSOL0u31wPO",  # "Channa Mereya" - Ae Dil Hai Mushkil (Hindi)
        "https://open.spotify.com/track/3x6zHFA8kZ6X3nGnqxSxQ4",  # "Tujh Mein Rab Dikhta Hai" - Rab Ne Bana Di Jodi (Hindi)
        "https://open.spotify.com/track/5hc71nKsUgtwQ3z52KEKQk",  # "When I Was Your Man" - Bruno Mars
        "https://open.spotify.com/track/4E6cwWJWZw2zWf7VFbH7wf",  # "Jeene Laga Hoon" - Ramaiya Vastavaiya (Hindi)
        "https://open.spotify.com/track/5yY9lUy8nbvjM1Uyo1Uqoc",  # "Lucid Dreams" - Juice WRLD
        "https://open.spotify.com/track/7mWFF4gPADjTQjC97CgFVt",  # "Thinking Out Loud" - Ed Sheeran
        "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7a",  # "Fix You" - Coldplay
        "https://open.spotify.com/track/3Yv8T2B5FlNIX9l7dMyh0S",  # "Yesterday" - The Beatles
        "https://open.spotify.com/track/4jAiXlE6lOr4EfM4oeLkXy",  # "Stay With Me" - Sam Smith
        "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp",  # "Wonderwall" - Oasis
        "https://open.spotify.com/track/1i1fxkWeaMmKEB4T7zqbzK",  # "A Thousand Years" - Christina Perri
        "https://open.spotify.com/track/6b8Be6ljOzmkOmFslEb23P",  # "Say You Won't Let Go" - James Arthur
        "https://open.spotify.com/track/1qOL5x8MydsDfsz2k9jaSx",  # "Pachtaoge" - Arijit Singh (Hindi)
        "https://open.spotify.com/track/5fAixuTiZ2dJieSYkJr7nK",  # "Let Her Go" - Passenger
        "https://open.spotify.com/track/0GLUBbD96O2SrWkOFLV5iu",  # "Humdard" - Ek Villain (Hindi)
        "https://open.spotify.com/track/7fBv7CLKzipRk6EC6TWHOB",  # "Someone You Loved" - Lewis Capaldi
        "https://open.spotify.com/track/0rFke7jzqcjPtg1F4FDvLD",  # "Bruises" - Lewis Capaldi
        "https://open.spotify.com/track/4Fou5BfS2dPBY2Jei6i7a4",  # "Too Good At Goodbyes" - Sam Smith
    ],
    'surprised': [
        "https://open.spotify.com/track/6bo2Sc56kQZ2pSh5B1oqqt",  # "Somebody's Watching Me" - Rockwell
        "https://open.spotify.com/track/4kLLWz6uS0kp3ojvtF8cw5",  # "Bad Guy" - Billie Eilish
        "https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9",  # "Feel Invincible" - Skillet
        "https://open.spotify.com/track/6RUKPb4LETWmmr3iAEQktW",  # "Believer" - Imagine Dragons
        "https://open.spotify.com/track/1z1Hg7Vb0AhHDiEmnDE79l",  # "I Gotta Feeling" - The Black Eyed Peas
        "https://open.spotify.com/track/2Z1D24qhQz0qC2xZ73hEZ8",  # "Cry Baby" - Melanie Martinez
        "https://open.spotify.com/track/6M6xD2N4D0oX6K4PrxKlbv",  # "Thriller" - Michael Jackson
        "https://open.spotify.com/track/1IueXOQyABrMOprrzwQJWN",  # "Disturbia" - Rihanna
        "https://open.spotify.com/track/5OCJzvD7sykQEKHH7qAC3C",  # "SICKO MODE" - Travis Scott
        "https://open.spotify.com/track/4PzPvpE9TE4dD11s1MHpbf",  # "Bad Romance" - Lady Gaga
        "https://open.spotify.com/track/0k664IuFwVP557Gnx7RhIl",  # "Someone Like You" - Adele
        "https://open.spotify.com/track/0KFYjWwEtLAN8k8ZSPpMfw",  # "Castle" - Halsey
        "https://open.spotify.com/track/1wgoWgL9fGf2Hd5NXfxYEK",  # "Stairway to Heaven" - Led Zeppelin
        "https://open.spotify.com/track/5Nf0ApM3Aogz0U4wNW5rFd",  # "Wonderwall" - Oasis
        "https://open.spotify.com/track/3DTR4oKUIiF2y89Qcq29Lg",  # "Goosebumps" - Travis Scott
        "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7a",  # "Fix You" - Coldplay
        "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT",  # "Never Gonna Give You Up" - Rick Astley
        "https://open.spotify.com/track/0EmeFodog0BfCgMzAIvKQp",  # "Hips Don't Lie" - Shakira
        "https://open.spotify.com/track/1kT5m9XwyAiGHr9a3a7IrB",  # "Uptown Funk" - Mark Ronson ft. Bruno Mars
        "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC",  # "Bohemian Rhapsody" - Queen
    ],
}

articles= {
    'angry': [
        "https://www.psychologytoday.com/us/blog/anger-in-the-age-entitlement",
        "https://www.verywellmind.com/how-to-control-anger-2584781",
        "https://www.helpguide.org/articles/relationships-communication/anger-management.htm",
        "https://www.webmd.com/mental-health/mental-health-anger-management",
        "https://www.healthline.com/health/mental-health/how-to-control-anger",
    ],
    'disgust': [
        "https://www.psychologytoday.com/us/blog/inside-the-consulting-room/201506/the-psychology-disgust",
        "https://www.betterhelp.com/advice/how-to/feeling-disgusted-what-it-means-and-what-you-can-do/",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3192221/",
        "https://www.psychmechanics.com/psychology-of-disgust/",
        "https://www.goodtherapy.org/learn-about-therapy/issues/disgust",
    ],
    'fear': [
        "https://www.psychologytoday.com/us/blog/facing-fear",
        "https://www.helpguide.org/articles/anxiety/how-to-stop-worrying.htm",
        "https://www.verywellmind.com/how-to-cope-with-fear-and-anxiety-4164111",
        "https://www.healthline.com/health/how-to-overcome-fear",
        "https://www.mayoclinic.org/tests-procedures/exposure-therapy/about/pac-20384617",
    ],
    'happy': [
        "https://www.psychologytoday.com/us/basics/happiness",
        "https://www.verywellmind.com/ways-to-increase-happiness-5194772",
        "https://www.helpguide.org/articles/mental-health/mental-health-and-wellness.htm",
        "https://www.healthline.com/health/how-to-be-happy",
        "https://www.mind.org.uk/information-support/tips-for-everyday-living/happiness/",
    ],
    'neutral': [
        "https://www.psychologytoday.com/us/blog/your-emotional-meter/202202/the-state-of-being-neutral",
        "https://www.verywellmind.com/is-being-emotionally-numb-good-or-bad-for-your-health-4166129",
        "https://www.healthline.com/health/emotional-detachment",
        "https://www.helpguide.org/articles/relationships-communication/emotional-intelligence-eq.htm",
        "https://www.psychologytoday.com/us/blog/emotional-sobriety/202001/the-power-being-neutral",
    ],
    'sad': [
        "https://www.psychologytoday.com/us/blog/click-here-happiness/201901/how-be-happy-again-13-simple-ways-be-happier",
        "https://www.verywellmind.com/ways-to-be-happier-when-youre-sad-5194773",
        "https://www.helpguide.org/articles/depression/coping-with-depression.htm",
        "https://www.webmd.com/depression/guide/coping-with-depression",
        "https://www.healthline.com/health/how-to-deal-with-depression",
    ],
    'surprised': [
        "https://www.psychologytoday.com/us/basics/surprise",
        "https://www.betterhelp.com/advice/how-to/how-to-handle-being-surprised-and-why-we-feel-surprise/",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3173537/",
        "https://www.goodtherapy.org/blog/psychpedia/surprise",
        "https://www.psychologytoday.com/us/blog/hot-thought/201308/surprised-again",
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




# @app.get("/content_for/{mood}")
# async def content_for(mood: AvailableOptions):
#     if mood == AvailableOptions.angry:
#         return random.sample(emotions['angry'], 5)
#     if mood == AvailableOptions.happy:
#         return random.sample(emotions['happy'], 5)
#     if mood == AvailableOptions.sad:
#         return random.sample(emotions['sad'], 5)
#     if mood == AvailableOptions.fear:
#         return random.sample(emotions['fear'], 5)
#     if mood == AvailableOptions.neutral:
#         return random.sample(emotions['neutral'], 5)
#     if mood == AvailableOptions.excited:
#         return random.sample(emotions['excited'], 5)
#     else:
#         # Return the full list for other emotions
#         return emotions.get(mood, [])

@app.get("/mood/{mood}", response_model=MoodResponse)
async def get_mood_content(mood: AvailableOptions):
    selected_videos = random.sample(emotions[mood.value], min(7, len(emotions[mood.value])))
    selected_suggestions = random.sample(mood_suggestions[mood.value], min(2, len(mood_suggestions[mood.value])))
    selected_playlists = random.sample(playlists[mood.value], min(7, len(playlists[mood.value])))
    selected_articles = random.sample(articles[mood.value], min(2, len(articles[mood.value])))

    return MoodResponse(
        mood=mood,
        videos=selected_videos,
        playlists=selected_playlists,
        suggestions=selected_suggestions,
        articles=selected_articles
    )

