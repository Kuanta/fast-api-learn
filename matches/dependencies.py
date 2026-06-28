from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from core.config import settings

# İsteklerde "X-API-Key: <key>" header'ını arar
api_key_header = APIKeyHeader(name="X-API-Key")


def verify_service_key(key: str = Security(api_key_header)):
    """
    Authoritative game server authorization with api key
    """
    if key != settings.GAME_SERVER_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid service credentials",
        )
    return True
