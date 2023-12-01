from fastapi import APIRouter

from comments import CommentModel, EditCommentModel

from database.commentservice import add_comment_db, edit_comment_db, delete_comment_db


comments_router = APIRouter(prefix='/comment', tags=['Работа с комментариями'])


@comments_router.post('/add_comment')
async def add_comment(data: CommentModel):
    pass


@comments_router.put('/edit_comment')
async def edit_comment(data: EditCommentModel):
    pass


@comments_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    pass


@comments_router.get('/get_comments')
async def get_comments(post_id: int):
    pass
