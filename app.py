from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from histogram import Histogram
import asyncio

app = FastAPI()

@app.post("/insertSamples/")
async def insertSamples(samples):
    try:
        # Insert the samples into the histogram
        histogram.insertSamples(samples)
        return {"message": "Sample inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/metrics/")
async def metrics():
    try:
        # Compute metrics and return as text
        metrics_text = histogram.metrics()
        return {"metrics": metrics_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

def make_intervals(boundaries):
    siz = len(boundaries)
    intervals = []
    for i in range(0, siz, 2):
        pair = [boundaries[i], boundaries[i + 1]]
        intervals.append(pair)
    return intervals
    
#main function
if __name__ == "__main__":
    import pathlib
    import sys
    import uvicorn

    here = pathlib.Path(__file__).parent

    try:
        # Attempt to read the "intervals.txt" file
        with open(here.joinpath("intervals.txt")) as infile:
            boundaries = []
            for line in infile:
                boundaries.extend([float(i) for i in line.split()])
        
        intervals = make_intervals(boundaries)

        hist = Histogram()
        hist.check_consistency(intervals)
        uvicorn.run(app, host="0.0.0.0", port=8000)
    
    except FileNotFoundError:
        print("Error: The 'intervals.txt' file is missing.")
    except Exception as e:
        print(f"Error: An exception occurred while reading 'intervals.txt': {str(e)}")

