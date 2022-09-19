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
