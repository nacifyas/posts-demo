import uvicorn
from fastapi import FastAPI
from models.post import Post
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/{pk}')
def get_by_id(pk):
    return Post.get(pk)


@app.get('/')
async def get_all():
    return [get_by_id(pk) for pk in Post.all_pks()]


@app.post('/')
async def create(post: Post):
    return post.save()


@app.put('/')
async def update(post: Post):
    return post.save()


@app.delete('/{pk}')
async def delete(pk: str):
    return Post.delete(pk)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8002, reload=True, host="127.0.0.1")