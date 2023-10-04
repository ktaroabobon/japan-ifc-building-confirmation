"""
建築基準法第21条第1号（大規模建築の主要構造部）
https://elaws.e-gov.go.jp/document?lawid=325AC0000000201#Mp-At_21-Pr_1
"""
from jpnifcbc.law.base_confirmation import BaseConfirmation, BaseConfirmationV2
from jpnifcbc.law.sub_methods.law109_4 import Confirmation as Law109_4
from jpnifcbc.law.sub_methods.law109_5 import Confirmation as Law109_5
from jpnifcbc.law.sub_methods.law109_4 import ConfirmationV2 as Law109_4_v2
from jpnifcbc.law.sub_methods.law109_5 import ConfirmationV2 as Law109_5_v2

from jpnifcbc.wrapper.element import Quantity


class Confirmation(BaseConfirmation):
    """
    基準法第21条第1号（大規模建築の主要構造部）の判定
    """

    def __init__(self, ifc_file):
        super().__init__(ifc_file)

    @classmethod
    def main(cls, ifc_file):
        """
        適合判定実行関数

        Returns:
            bool: 判定結果
        """
        target = cls(ifc_file=ifc_file)
        if not target.exception() and target.condition():
            target.verification()

        return [target.conformity_elements, target.not_conformity_elements, target.exception_elements]

    def exception(self):
        """
        例外部分の判定

        Returns:
            bool: 判定結果
        """
        # return sub_method(self.ifc_file)
        return False

    def condition(self) -> bool:
        """
        条件部分の判定

        Returns:
            bool: 判定結果
        """

        def __one() -> bool:
            """
            地階を除く階数が4以上であるかの判定

            Returns:
                bool: 判定結果

            """
            storeys = self.ifc_file.by_type('IfcBuildingStorey')
            flag = False
            cnt = 0

            for storey in storeys:
                for d in storey.IsDefinedBy:
                    try:
                        property_set = d.RelatingPropertyDefinition
                        if hasattr(property_set, "HasProperties"):
                            for property in property_set.HasProperties:
                                if property.is_a('IfcPropertySingleValue') and property.Name == "AboveGround":
                                    if property.NominalValue.wrappedValue:
                                        cnt += 1
                    except AttributeError:
                        """
                        FIXME:
                        AttributeError: entity instance of type 'IFC2X3.IfcRelDefinesByType' has no attribute 'RelatingPropertyDefinition'
                        """
                        pass

            if cnt >= 4:
                flag = True

            return flag

        def __two(idx=0) -> bool:
            """
            高さが16メートルを超える建築物であるかの判定

            Args:
                idx(int): 対象の建築物のインデックス番号

            Returns:
                bool: 判定結果

            """
            b = self.ifc_file.by_type('IfcBuilding')[idx]
            flag = False

            for d in b.IsDefinedBy:
                try:
                    property_set = d.RelatingPropertyDefinition
                    if hasattr(property_set, "HasProperties"):
                        for property in property_set.HasProperties:
                            if property.is_a('IfcPropertySingleValue') and property.Name == "Height":
                                if property.NominalValue.wrappedValue > 16000:
                                    flag = True
                                    break

                    if hasattr(property_set, "Quantities"):
                        for q in property_set.Quantities:
                            if q.Name == "Height":
                                if Quantity.value(q) > 16000:
                                    flag = True
                                    break
                except AttributeError:
                    """
                    FIXME:
                    AttributeError: entity instance of type 'IFC2X3.IfcRelDefinesByType' has no attribute 'RelatingPropertyDefinition'
                    """
                    pass

            return flag

        def __three(idx=0) -> bool:
            """
            別表第一(い)欄(五)項又は(六)項に掲げる用途に供する特殊建築物で、高さが十三メートルを超えるものの判定

            Args:
                idx(int): 対象の建築物のインデックス番号

            Returns:
                bool: 判定結果
            """
            b = self.ifc_file.by_type('IfcBuilding')[idx]
            flag = True

            for d in b.IsDefinedBy:
                try:
                    property_set = d.RelatingPropertyDefinition
                    if hasattr(property_set, "HasProperties"):
                        for property in property_set.HasProperties:
                            if property.is_a('IfcPropertySingleValue'):
                                if property_set.Name == "Pset_BuildingUse" and property.Name == "MarketCategory":
                                    if property.NominalValue.wrappedValue not in ["倉庫", "自動車車庫",
                                                                                  "自動車修理工場"]:
                                        flag = False
                                        break
                                if property.Name == "Height":
                                    if property.NominalValue.wrappedValue > 13000:
                                        flag = False
                                        break

                    if hasattr(property_set, "Quantities"):
                        for q in property_set.Quantities:
                            if q.Name == "Height":
                                if Quantity.value(q) > 13000:
                                    flag = False
                                    break
                except AttributeError:
                    """
                    FIXME:
                    AttributeError: entity instance of type 'IFC2X3.IfcRelDefinesByType' has no attribute 'RelatingPropertyDefinition'
                    """
                    pass

            return flag

        flag = False
        if __one() or __two() or __three():
            flag = True
        return flag

    def verification(self):
        """
        基準部分の判定

        Returns:
        """
        conformity_elements_by109_4, not_conformity_elements_by109_4 = Law109_4.main(self.ifc_file)
        conformity_elements_by109_5, not_conformity_elements_by109_5 = Law109_5.main(
            self.ifc_file,
            conformity_elements_by109_4
        )

        self.conformity_elements = conformity_elements_by109_5
        self.not_conformity_elements = not_conformity_elements_by109_4 + not_conformity_elements_by109_5


class ConfirmationV2(BaseConfirmationV2):
    """
    基準法第21条第1号（大規模建築の主要構造部）の判定
    独自API規格を実装するためのクラス
    """

    @classmethod
    def main(cls):
        """
        適合判定実行関数

        Returns:
            bool: 判定結果
        """
        target = cls()
        if not target.exception() and target.condition():
            target.verification()

        return [target.conformity_elements, target.not_conformity_elements, target.exception_elements]

    def exception(self):
        """
        例外部分の判定

        Returns:
            bool: 判定結果
        """
        return False

    def condition(self) -> bool:
        """
        条件部分の判定

        Returns:
            bool: 判定結果
        """

        def __one() -> bool:
            """
            地階を除く階数が4以上であるかの判定

            Returns:
                bool: 判定結果

            """

            cnt = 0

            for storey in self.target_building.storeys:
                if storey.pset('above_ground'):
                    cnt += 1

            return cnt >= 4

        def __two() -> bool:
            """
            高さが16メートルを超える建築物であるかの判定

            Returns:
                bool: 判定結果

            """

            return self.target_building.height > 16000

        def __three() -> bool:
            """
            別表第一(い)欄(五)項又は(六)項に掲げる用途に供する特殊建築物で、高さが十三メートルを超えるものの判定

            Returns:
                bool: 判定結果
            """
            target_building_use = ['倉庫', '自動車車庫', '自動車修理工場']

            return self.target_building.use in target_building_use and self.target_building.height > 13000

        flag = False
        if __one() or __two() or __three():
            flag = True
        return flag

    def verification(self):
        """
        基準部分の判定

        Returns:
        """
        conformity_elements_by109_4, not_conformity_elements_by109_4 = Law109_4_v2.main()
        conformity_elements_by109_5, not_conformity_elements_by109_5 = Law109_5_v2.main()

        self.conformity_elements = conformity_elements_by109_5
        self.not_conformity_elements = not_conformity_elements_by109_4 + not_conformity_elements_by109_5
