import secrets
import uuid
from datetime import time
from typing import Annotated, Any
from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix="/demo-auth", tags=["Demo Auth"])
security = HTTPBasic()


@router.get("/basic-auth/")
def demo_basic_auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    return {
        "message": "Hi!",
        "user_name": credentials.username,
        "password": credentials.password,
    }


# для проверки, пока нет БД
user_names = {
    "admin": "admin",
    "sveta": "sveta",
}
static_auth_token_user_names = {
    "17b986727066488efe91a16edf0ecdd8": "admin",
    "bb4d1bf0e0f371a18e02117203c98c95": "sveta",
}


def get_auth_user_name(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    unauth_exp = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Введи пароль нормально",
        headers={"WWW-Authenticate": "Basic"},
    )
    correct_pass = user_names.get(credentials.username)
    if correct_pass:
        raise unauth_exp
    # быстрее проверки через == и безопаснее
    if not secrets.compare_digest(
        credentials.password.encode("utf-8"), correct_pass.encode("utf-8")
    ):
        raise unauth_exp

    return credentials.username


def get_username_by_static_auth_tocken(
    static_token: str = Header(alias="x-auth-token"),
) -> str:
    if static_token not in static_auth_token_user_names:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="токен инвалид"
        )
    return static_auth_token_user_names[static_token]


@router.get("/basic-auth-username/")
def demo_basic_auth_user_name(
    auth_user_name: str = Depends(get_auth_user_name),
):
    return {
        "message": f"Hi, {auth_user_name}",
        "user_name": auth_user_name,
    }


@router.get("/some-http-header-auth/")
def demo_auth_some_http_header(
    user_name: str = Depends(get_username_by_static_auth_tocken),
):
    return {
        "message": f"Hi, {user_name}",
        "user_name": user_name,
    }


# Временное хранилище для демонтрации
COOKIES: dict[str, dict[str, Any]] = {}
COOKIES_SESSION_ID_KEY = "web-app-session-id"


def generate_session_id() -> str:
    return uuid.uuid4().hex


def get_session_data(session_id: str = Cookie(alias=COOKIES_SESSION_ID_KEY)) -> dict:
    if session_id not in COOKIES:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="не залогинились"
        )
    return COOKIES[session_id]


@router.get("/login-cookie/")
def demo_auth_login_cookie(
    respons: Response,
    # auth_user_name: str = Depends(get_auth_user_name),
    user_name: str = Depends(get_username_by_static_auth_tocken),
):
    session_id = generate_session_id()
    COOKIES[session_id] = {"user_name": user_name, "login_at": time()}
    respons.set_cookie(COOKIES_SESSION_ID_KEY, session_id)
    return {"result": "ok"}


@router.get("/check-cookie/")
def demo_auth_check_cookie(user_session_data: dict = Depends(get_session_data)):
    username = user_session_data["user_name"]
    return {
        "message": f"Hello, {username}",
        **user_session_data,
    }


@router.get("/logout-cookie/")
def demo_auth_logout_cookie(
    respons: Response,
    session_id: str = Cookie(alias=COOKIES_SESSION_ID_KEY),
    user_session_data: dict = Depends(get_session_data),
):
    COOKIES.pop(session_id)
    respons.delete_cookie(COOKIES_SESSION_ID_KEY)
    user_name = user_session_data["user_name"]
    return {"message": f"By, {user_name}"}
