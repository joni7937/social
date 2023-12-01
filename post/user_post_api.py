from fastapi import APIRouter, UploadFile, Body

from post import PublicPostValidator, EditPostValidator

from database.postservice import add_post_db, add_post_photo_db, edit_post_db, delete_post_db, get_exact_post_db

posts_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])


@posts_router.post('/public_post')
async def public_post(data: PublicPostValidator):
    result = add_post_db(**data.model_dump())

    return {'message': result}


@posts_router.put('/change-post')
async def change_post(data: EditPostValidator):
    result = edit_post_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'пост не найден'}


@posts_router.delete('delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    if result:
        return {'message': result}

    else:
        return {'message': 'Что пошло не так'}


@posts_router.get('/get_all_posts')
async def get_all_posts():
    pass


@posts_router.post('/add_photo')
async def add_photo(post_id: int = Body(), user_id: int = Body(), photo_file: UploadFile = None):
    photo_path = f'/media/{photo_file.filename}'

    try:
        with open(f'media/{photo_file.filename}', 'wb') as file:
            user_photo = await photo_file.read()

            file.write(user_photo)

            result = add_post_photo_db(post_id=post_id, photo_file=photo_path)

    except Exception as error:
        result = error


    return {'message': result}


@posts_router.get('get_exact_post')
async def get_exact_post(post_id: int):

    result = get_exact_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return 'Пост не найден'



