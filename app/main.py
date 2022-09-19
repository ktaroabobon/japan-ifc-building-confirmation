import io
import sys
from pathlib import Path

import ifcopenshell

from app.jpnifcbc.law.standard_methods.law21_1 import Confirmation as Law21_1

# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

base_dir = Path().parent.resolve()
data_dir = base_dir / "data"

SAMPLE_DATA_PATH = data_dir / 'test.ifc'

if __name__ == '__main__':
    ifc_file = ifcopenshell.open(str(SAMPLE_DATA_PATH))
    l1, l2, l3 = Law21_1.main(ifc_file=ifc_file)
    print(f"conformity elements len: {len(l1)}")
    print(f"no conformity elements len: {len(l2)}")
    # print(f"exception elements len: {len(l3)}")
    print(f"acc: {len(l1) / (len(l1) + len(l2)) * 100}")

    print("=============================")
    print("適合部材")
    print("=============================")

    for i, e in enumerate(l1):
        if i >= 5:
            break
        print(f"No.{i + 1}")
        print(f"type: {e.is_a()}")
        print(f"name: {e.Name}")
        print(f"global id: {e.GlobalId}")
        for d in e.IsDefinedBy:
            property_set = d.RelatingPropertyDefinition
            if hasattr(property_set, "HasProperties"):
                for p in property_set.HasProperties:
                    if p.is_a('IfcPropertySingleValue') and p.Name == "FireRating":
                        print(f"Fire Rating value: {p.NominalValue.wrappedValue}")
        print("------")

    print("=============================")
    print("不適合部材")
    print("=============================")

    for i, e in enumerate(l2):
        if i >= 5:
            break
        print(f"No.{i + 1}")
        print(f"type: {e.is_a()}")
        print(f"name: {e.Name}")
        print(f"global id: {e.GlobalId}")
        for d in e.IsDefinedBy:
            property_set = d.RelatingPropertyDefinition
            if hasattr(property_set, "HasProperties"):
                for p in property_set.HasProperties:
                    if p.is_a('IfcPropertySingleValue') and p.Name == "FireRating":
                        print(f"Fire Rating value: {p.NominalValue.wrappedValue}")

        print("------")
