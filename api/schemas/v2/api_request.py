from pydantic import BaseModel

from api.schemas.v2.building import Building


class APIRequest(BaseModel):
    """Base class for all API requests."""
    building: Building
    metadata: dict

