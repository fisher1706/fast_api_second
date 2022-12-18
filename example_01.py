# https://www.youtube.com/watch?v=W6aqCFJp7Xo&t=2791s

import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/greet/{name}')
def greet(name: str):
    return {'message': f'Hello, {name}'}


if __name__ == '__main__':
    uvicorn.run(app)

