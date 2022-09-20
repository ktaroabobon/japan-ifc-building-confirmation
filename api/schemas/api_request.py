from pydantic import BaseModel


class ApiRequest(BaseModel):
    """Base class for all API requests."""
    ifc: str
    metadata: dict
