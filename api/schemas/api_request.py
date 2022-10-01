from pydantic import BaseModel


class APIRequest(BaseModel):
    """Base class for all API requests."""
    ifc: str
    zipped: bool
    metadata: dict
