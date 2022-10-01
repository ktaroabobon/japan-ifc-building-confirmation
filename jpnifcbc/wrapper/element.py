class BuildingElement(object):
    @classmethod
    def get_storey(cls, e):
        if not e.is_type("IfcBuildingElement"):
            return


class Quantity(object):
    @classmethod
    def value(cls, q):
        if q.is_a("IfcQuantityArea"):
            return q.AreaValue
        elif q.is_a("IfcQuantityCount"):
            return q.CountValue
        elif q.is_a("IfcQuantityLength"):
            return q.LengthValue
        elif q.is_a("IfcQuantityTime"):
            return q.TimeValue
        elif q.is_a("IfcQuantityVolume"):
            return q.VolumeValue
        elif q.is_a("IfcQuantityWeight"):
            return q.WeightValue
        else:
            return
