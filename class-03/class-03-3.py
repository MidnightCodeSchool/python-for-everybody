# dictionary
pet_1 = {
    "name": "จอห์น",
    "kind": "แมว",
    "legs": 4,
    "ears": 2
}

pet_1["name"]
pet_1["kind"]
pet_1["legs"]
pet_1["ears"]

pet_1["age"]
pet_1["age"] = 3
pet_1["age"]
del pet_1["age"]
pet_1

for key, value in pet_1.items():  # [("name", "จอห์น"), (key, value), ...]
    print(key, value)

# splitting
paragraph = "The quick brown fox jumps over the lazy dog dog dog"
words = paragraph.split(" ")

# in, เช็คว่ามีอยู่หรือไม่
my_list = [1, 2, 3, 4]
4 in my_list
5 in my_list
my_dictionry = {"a": 1, "b": 2, "c": 3}
"a" in my_dictionry
"X" in my_dictionry
