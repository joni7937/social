from fastapi import FastAPI
from photo.photo_api import photo_router
from users.user_api import user_router
from post.user_post_api import posts_router
from comments.comment_api import comments_router


from database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')


app.include_router(photo_router)
app.include_router(user_router)
app.include_router(posts_router)
app.include_router(comments_router)


@app.get('test')
async def test():
    return 'this is test page'



