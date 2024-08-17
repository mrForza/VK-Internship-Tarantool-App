from fastapi import APIRouter


authorization_router = APIRouter(prefix='/auth', tags=['auth'])


@authorization_router.post('/register/')
def register():
    pass


@authorization_router.post('/login/')
def authenticate():
    pass


@authorization_router.post('/logout/')
def logout():
    pass
