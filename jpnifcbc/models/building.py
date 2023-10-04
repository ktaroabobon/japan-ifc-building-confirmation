from typing import List


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
        self.height: float = height


class Wall(BuildingElement):
    """壁クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)


class Column(BuildingElement):
    """柱クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)


class Slab(BuildingElement):
    """床クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)


class Beam(BuildingElement):
    """梁クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)


class Roof(BuildingElement):
    """屋根クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)


class Stair(BuildingElement):
    """階段クラス"""

    def __init__(
            self,
            id: str,
            name: str,
            psets: dict,
    ):
        super().__init__(id, name, psets)


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
