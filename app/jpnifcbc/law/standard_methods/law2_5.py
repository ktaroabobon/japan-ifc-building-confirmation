"""
建築基準法第2条第5号（主要構造部）
https://elaws.e-gov.go.jp/document?lawid=325AC0000000201#Mp-At_2-Pr_1-It_5
"""
from app.jpnifcbc.law.base_confirmation import BaseConfirmation


class Confirmation(BaseConfirmation):
    """
    基準法第2条第5号（主要構造部）の判定
    """

    def __init__(self, ifc_file):
        super().__init__(ifc_file)

    @classmethod
    def main(cls, ifc_file) -> list:
        """
        適合判定実行関数

        Returns:
            bool: 判定結果
        """
        target = cls(ifc_file=ifc_file)
        target.condition()
        target.verification()

        return [target.conformity_elements, target.not_conformity_elements]

    def condition(self):
        """
        条件部分の判定

        Returns:

        """
        target_elements = ["IfcWall", "IfcColumn", "IfcSlab", "IfcBeam", "IfcRoof", "IfcStair"]

        self.target_elements = self.filter_elements(target_elements)[0]

    def verification(self):
        """
        基準部分の判定

        Returns:

        """
        if self.target_elements is None:
            return

        conformity_elements = list()
        not_conformity_elements = list()

        for element in self.target_elements:
            for d in element.IsDefinedBy:
                property_set = d.RelatingPropertyDefinition
                if hasattr(property_set, "HasProperties"):
                    for property in property_set.HasProperties:
                        if property.is_a('IfcPropertySingleValue') and property.Name == "LoadBearing":
                            if property.NominalValue.wrappedValue:
                                conformity_elements.append(element)
                            else:
                                not_conformity_elements.append(element)

        self.conformity_elements = conformity_elements
        self.not_conformity_elements = not_conformity_elements
