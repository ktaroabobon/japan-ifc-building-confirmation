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


class Building(object):
    """建物クラス"""

    def __init__(
            self,
            height: float,
            use: str,
            storeys: List[Storey] = None,
    ):
        self.storeys: List[Storey] = storeys
        self.height: float = height
        self.use: str = use
