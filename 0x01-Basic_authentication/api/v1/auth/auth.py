from typing import List, TypeVar
from flask import request

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method that returns False"""
        return False

    def authorization_header(self, request=None) -> str:
        """Public method that returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method that returns None"""
        return None
