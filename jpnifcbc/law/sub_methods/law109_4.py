"""
建築基準法施行令第109条第4項
https://elaws.e-gov.go.jp/document?lawid=325CO0000000338#Mp-At_109_4-Pr_1
"""
from jpnifcbc.law.base_confirmation import BaseConfirmation
from jpnifcbc.law.standard_methods.law2_5 import Confirmation as Law2_5


class Confirmation(BaseConfirmation):
    """
    施行令第109条第4項

    基準法第21条第1項の政令で定められている部分の技術的基準について
    """

    def __init__(self, ifc_file):
        super().__init__(ifc_file)

    @classmethod
    def main(cls, ifc_file):
        """
        実行関数

        Returns:

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
        self.target_elements, _ = Law2_5.main(self.ifc_file)

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
                try:
                    property_set = d.RelatingPropertyDefinition
                    if hasattr(property_set, "HasProperties"):
                        for property in property_set.HasProperties:
                            if property.is_a('IfcPropertySingleValue') and property.Name == "LoadBearing":
                                if property.NominalValue.wrappedValue:
                                    conformity_elements.append(element)
                                else:
                                    not_conformity_elements.append(element)
                except AttributeError:
                    """
                    FIXME:
                    AttributeError: entity instance of type 'IFC2X3.IfcRelDefinesByType' has no attribute 'RelatingPropertyDefinition'
                    """
                    pass

        self.conformity_elements = conformity_elements
        self.not_conformity_elements = not_conformity_elements
