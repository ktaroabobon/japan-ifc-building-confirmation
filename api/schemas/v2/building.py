from typing import List

from pydantic import BaseModel


class Storey(BaseModel):
    id: str
    name: str
    psets: dict
    height: float


class Wall(BaseModel):
    id: str
    name: str
    psets: dict


class Column(BaseModel):
    id: str
    name: str
    psets: dict


class Slab(BaseModel):
    id: str
    name: str
    psets: dict


class Beam(BaseModel):
    id: str
    name: str
    psets: dict


class Roof(BaseModel):
    id: str
    name: str
    psets: dict


class Stair(BaseModel):
    id: str
    name: str
    psets: dict


class Building(BaseModel):
    id: str
    name: str
    storeys: List[Storey]
    walls: List[Wall]
    columns: List[Column]
    slabs: List[Slab]
    beams: List[Beam]
    roofs: List[Roof]
    stairs: List[Stair]
    height: float
    use: str
