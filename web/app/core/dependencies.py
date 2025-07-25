"""
의존성 주입을 위한 공통 의존성 모듈
"""
from typing import Generator
from fastapi import Depends
from web.app.core.config import settings
from web.app.services.file_service import FileService
from web.app.services.chat_service import ChatService


def get_file_service() -> FileService:
    return FileService()

def get_chat_service() -> ChatService:
    return ChatService()

def get_settings():
    return settings 