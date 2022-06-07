from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#requirement: python fatsapi & uvicorn
formData = []
graphData = []
import csv
with open('dataset_world_bank_220119.csv', 'r') as file:
    filecontent = csv.reader(file)
    for index, data in enumerate(filecontent):
        if index > 3:
            formData.append(data)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    tempKey=[]
    finalLabel = []
    prepData = []
    tempData=[]
    finalData = []
    dataKey = []
    for i, d in enumerate(formData):
        if i == 0:
            k = d[4:]
            finalLabel.append(k)
        if i > 0:
            prepData.append(d)
            # r=d[:1]
            tempKey.append(d[0])
    dataKey = sorted(tempKey)

    for i, d in enumerate(prepData):
        a = d[4:]
        tempData.append(( d[0],a))
    tempData.sort(key=lambda data:data[0])
    return {"datakey": dataKey, "finalData": tempData, "label": finalLabel}
