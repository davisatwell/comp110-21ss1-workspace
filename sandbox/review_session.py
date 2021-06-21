
list_1: list[str] = ["davis", "mason"]
list_2: list[str] = ["18", "20"]
# Column Oriented
x: dict[str, list[str]] = {"name": list_1, "age": list_2}
# Row Oriented
y: list[dict[str, str]] = []

xs: dict[str,str] = {"team": "UNC", "color": "blue"}
xs["state"] = "NC" # since key "state" IS NOT already in the dict object 'xs', this statement adds the key "state" that is assigned the value "NC"
xs["color"] = "Black" # since "color" IS already in the dict object 'xs', the value assigned to the "color" key is updated from "blue" to "Black"
print(xs)