from typing import List

from collections import defaultdict


class BuildingElement(object):
    """建物要素クラス"""

    def __init__(self, id: str, name: str, psets: dict):
        self.id: str = id
        self.name: str = name
        self.psets: dict = psets

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
    ):
        super().__init__(id, name, psets)
        self.type: str = "Storey"
        self.height: float = height

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
            "height": self.height,
        }


class Wall(BuildingElement):
    """壁クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)
        self.type: str = "Wall"

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
        }


class Column(BuildingElement):
    """柱クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)
        self.type: str = "Column"

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
        }


class Slab(BuildingElement):
    """床クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)
        self.type: str = "Slab"

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
        }


class Beam(BuildingElement):
    """梁クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)
        self.type: str = "Beam"

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
        }


class Roof(BuildingElement):
    """屋根クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)
        self.type: str = "Roof"

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
        }


class Stair(BuildingElement):
    """階段クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)
        self.type: str = "Stair"

    def export_as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'type': self.type,
            "psets": self.psets,
        }


class Building(object):
    """建物クラス"""

    def __init__(
            self,
            height: float,
            use: str,
            storeys: List[Storey] = None,
            building_elements: list = None,
    ):
        self.storeys: List[Storey] = storeys
        self.building_elements: list = building_elements
        self.height: float = height
        self.use: str = use

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
        }
