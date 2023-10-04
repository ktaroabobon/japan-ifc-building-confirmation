from typing import Optional

from jpnifcbc.models.building import Building


class BaseConfirmation(object):
    def __init__(self, ifc_file):
        self.ifc_file = ifc_file
        self.target_elements = None
        self.exception_elements = None
        self.conformity_elements = None
        self.not_conformity_elements = None

    def filter_elements(self, target: list):
        conformity_elements = list()
        not_conformity_elements = list()
        for t in target:
            conformity_elements += self.ifc_file.by_type(t)

        return [conformity_elements, not_conformity_elements]


class BaseConfirmationV2(object):
    def __init__(self):
        self.target_building: Optional[Building] = None
        self._target_elements = None
        self.exception_elements = None
        self.conformity_elements = None
        self.not_conformity_elements = None

    def filter_by_instances(self, target: list, filter: list):
        """
        指定したクラスのインスタンスを抽出する

        Args:
            target: 対象のクラス
            filter: 抽出するクラス

        Returns:
            list: 抽出したインスタンス
        """
        result = list()
        for t in target:
            if isinstance(t, tuple(filter)):
                result.append(t)

        return result

    @property
    def target_elements(self):
        if self.target_elements is not None:
            return self._target_elements
        else:
            return self.target_building.building_elements

    @target_elements.setter
    def target_elements(self, elements):
        self._target_elements = elements

