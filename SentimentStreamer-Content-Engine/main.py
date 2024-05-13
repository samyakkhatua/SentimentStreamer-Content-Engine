from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class AvailableOptions(str,Enum):
    happy="happy"
    sad="sad"
    neutral="neutral"
    excited="excited"
    surprised="surprised"

emotions={
   'happy':["khush rhoo bettuuuu"],
   'sad':["akela chorde bhaii"],
   'surprised':["arisss hbyyy"],
   'excited':["harddd bhaiii"],
   'neutral':["hn thikkk h"]
}

valid_mood=emotions.keys()

@app.get("/content_for/{mood}")
async def content_for(mood:AvailableOptions):
    return emotions.get(mood)
