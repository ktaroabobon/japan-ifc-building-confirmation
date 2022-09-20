from typing import Any, List

from pydantic import BaseModel


class ResponsePropertySet(BaseModel):
    """Property set of respose."""
    name: str
    value: Any


class ResponseElement(BaseModel):
    """Element of response."""
    globalId: str
    type: str
    name: str
    propertySetNumber: int
    propertySet: List[ResponsePropertySet]


class AnalysisResult(BaseModel):
    """Analysis result."""
    conformityElements: List[ResponseElement]
    nonConformityElements: List[ResponseElement]
    exceptionElements: List[ResponseElement]


class ApiResponse(BaseModel):
    """Base class for all API responses."""
    result: AnalysisResult
    metadata: dict
