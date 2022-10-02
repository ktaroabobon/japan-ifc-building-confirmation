from typing import List


class IfcOpenShellObj(object):
    @classmethod
    def get_obj_info(cls, obj_list: list) -> List[dict]:
        """ifcopenshell形式のオブジェクトから情報を取得する関数

        Args:
            obj_list (list):  ifcopenshellのオブジェクトを格納したリスト

        Returns:
            List[dict]: オブジェクトの情報を格納したリスト
        """
        if obj_list is None:
            return list()
        obj_info_list = list()

        for obj in obj_list:
            info_dict = {
                'globalId': obj.GlobalId,
                'type': obj.is_a(),
                'name': obj.Name,
            }

            property_list = list()
            for d in obj.IsDefinedBy:
                property_set = d.RelatingPropertyDefinition
                if hasattr(property_set, "HasProperties"):
                    for p in property_set.HasProperties:
                        property_dict = {
                            'name': p.Name,
                            'value': p.NominalValue.wrappedValue
                        }
                        property_list.append(property_dict)

            info_dict['propertySetNumber'] = len(property_list)
            info_dict['propertySet'] = property_list

            obj_info_list.append(info_dict)

        return obj_info_list
