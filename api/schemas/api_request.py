from pydantic import BaseModel


class HealthAPIRequest(BaseModel):
    ifc: str
    zipped: bool


class APIRequest(BaseModel):
    """Base class for all API requests."""
    ifc: str
    zipped: bool
    metadata: dict
