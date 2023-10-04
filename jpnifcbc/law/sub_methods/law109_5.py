"""
建築基準法施行令第109条第5項
https://elaws.e-gov.go.jp/document?lawid=325CO0000000338#Mp-At_109_5-Pr_1
"""

from jpnifcbc.law.base_confirmation import BaseConfirmation, BaseConfirmationV2
from jpnifcbc.models.building import Wall, Column, Slab, Beam, Roof, Stair


class Confirmation(BaseConfirmation):
    """
    施行令第109条第5項

    大規模建築物の主要構造部に関する技術的基準について
    """

    def __init__(self, ifc_file):
        super().__init__(ifc_file)

    @classmethod
    def main(cls, ifc_file, target_elements):
        """
        実行関数

        Returns:

        """
        target = cls(ifc_file=ifc_file)
        target.condition(target_elements)
        target.verification()

        return [target.conformity_elements, target.not_conformity_elements]

    def condition(self, target_elements):
        """
        条件部分の判定

        Returns:

        """
        self.target_elements = target_elements

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
            if element.is_a() in ["IfcWall", "IfColumn", "IfcSlab", "IfcBeam"]:
                for d in element.IsDefinedBy:
                    try:
                        property_set = d.RelatingPropertyDefinition
                        if hasattr(property_set, "HasProperties"):
                            for property in property_set.HasProperties:

                                if property.is_a('IfcPropertySingleValue') and property.Name == "FireRating":
                                    if int(property.NominalValue.wrappedValue) >= 45:
                                        conformity_elements.append(element)
                                    else:
                                        not_conformity_elements.append(element)
                    except AttributeError:
                        """
                        FIXME:
                        AttributeError: entity instance of type 'IFC2X3.IfcRelDefinesByType' has no attribute 'RelatingPropertyDefinition'
                        """
                        pass

            else:
                for d in element.IsDefinedBy:
                    try:
                        property_set = d.RelatingPropertyDefinition
                        if hasattr(property_set, "HasProperties"):
                            for property in property_set.HasProperties:
                                if property.is_a('IfcPropertySingleValue') and property.Name == "FireRating":
                                    if int(property.NominalValue.wrappedValue) >= 30:
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


class ConfirmationV2(BaseConfirmationV2):
    """
    施行令第109条第5項

    大規模建築物の主要構造部に関する技術的基準について
    """

    @classmethod
    def main(cls):
        """
        実行関数

        Returns:

        """
        target = cls()
        target.condition()
        target.verification()

        return [target.conformity_elements, target.not_conformity_elements]

    def condition(self):
        """
        条件部分の判定

        Returns:

        """
        pass

    def verification(self):
        """
        基準部分の判定

        Returns:

        """

        patter1_instances = [Wall, Column, Slab, Beam]

        conformity_elements = list()
        not_conformity_elements = list()

        for element in self.target_elements:
            fire_rating_value = element.pset("fire_rating")
            if isinstance(element, tuple(patter1_instances)):
                if fire_rating_value >= 45:
                    conformity_elements.append(element)
                else:
                    not_conformity_elements.append(element)
            else:
                if fire_rating_value >= 30:
                    conformity_elements.append(element)
                else:
                    not_conformity_elements.append(element)

        self.conformity_elements = conformity_elements
        self.not_conformity_elements = not_conformity_elements
