from typing import List

from collections import defaultdict


class BuildingElement(object):
    """建物要素クラス"""

    def __init__(self, id: str, name: str, psets: dict, metadata: dict):
        self.id: str = id
        self.name: str = name
        self.psets: dict = psets
        self.metadata: dict = metadata

    def pset(self, name: str):
        return self.psets.get(name, None)


class Storey(BuildingElement):
    """階クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
            height: float,
            metadata: dict,
    ):
        super().__init__(id, name, psets, metadata)
        self.type: str = "Storey"
        self.height: float = height

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id=d.get('id'),
            name=d.get('name'),
            psets=d.get('psets'),
            height=d.get('height'),
            metadata=d.get('metadata'),
        )

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
            "height": self.height,
            "metadata": self.metadata,
        }


class Wall(BuildingElement):
    """壁クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
            metadata: dict,
    ):
        super().__init__(id, name, psets, metadata)
        self.type: str = "Wall"

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id=d.get('id'),
            name=d.get('name'),
            psets=d.get('psets'),
            metadata=d.get('metadata'),
        )

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
            "metadata": self.metadata,
        }


class Column(BuildingElement):
    """柱クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
            metadata: dict,
    ):
        super().__init__(id, name, psets, metadata)
        self.type: str = "Column"

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id=d.get('id'),
            name=d.get('name'),
            psets=d.get('psets'),
            metadata=d.get('metadata'),
        )

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
            "metadata": self.metadata,
        }


class Slab(BuildingElement):
    """床クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
            metadata: dict,
    ):
        super().__init__(id, name, psets, metadata)
        self.type: str = "Slab"

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id=d.get('id'),
            name=d.get('name'),
            psets=d.get('psets'),
            metadata=d.get('metadata'),
        )

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
            "metadata": self.metadata,
        }


class Beam(BuildingElement):
    """梁クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
            metadata: dict,
    ):
        super().__init__(id, name, psets, metadata)
        self.type: str = "Beam"

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id=d.get('id'),
            name=d.get('name'),
            psets=d.get('psets'),
            metadata=d.get('metadata'),
        )

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
            "metadata": self.metadata,
        }


class Roof(BuildingElement):
    """屋根クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
            metadata: dict,
    ):
        super().__init__(id, name, psets, metadata)
        self.type: str = "Roof"

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id=d.get('id'),
            name=d.get('name'),
            psets=d.get('psets'),
            metadata=d.get('metadata'),
        )

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
            "metadata": self.metadata,
        }


class Stair(BuildingElement):
    """階段クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
            metadata: dict,
    ):
        super().__init__(id, name, psets, metadata)
        self.type: str = "Stair"

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id=d.get('id'),
            name=d.get('name'),
            psets=d.get('psets'),
            metadata=d.get('metadata'),
        )

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
            "metadata": self.metadata,
        }


class Building(object):
    """建物クラス"""

    def __init__(
            self,
            height: float,
            use: str,
            storeys: List[Storey] = None,
            building_elements: list = None,
            metadata: dict = None,
    ):
        self.storeys: List[Storey] = storeys
        self.building_elements: list = building_elements
        self.metadata: dict = metadata
        self.height: float = height
        self.use: str = use

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            height=d.get('height'),
            use=d.get('use'),
            metadata=d.get('metadata'),
        )

    def export_as_dict(self):
        building_elements = [b for b in self.building_elements]
        building_elements_dict = defaultdict(list)

        for b in building_elements:
            building_elements_dict[b.type].append(b.export_as_dict())

        return {
            "storeys": [s.export_as_dict() for s in self.storeys],
            "building_elements": building_elements_dict,
            "height": self.height,
            "use": self.use,
            "metadata": self.metadata,
        }
