"""DOCUMENTATION"""
###  https://ecma-international.org/wp-content/uploads/ECMA-404.pdf

###   international standard named ISO4217



"""TypeError: Object of type 'Class' is not JSON serializable"""

# import json


# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# def encode_who(w):
#     if isinstance(w, Who):
#         return w.__dict__
#     else:
#         raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


# some_man = Who('John Doe', 42)
# print(json.dumps(some_man, default=encode_who))


# import json


# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class MyEncoder(json.JSONEncoder):
#     def default(self, w):
#         if isinstance(w, Who):
#             return w.__dict__
#         else:
#             return super().default(self, z)


# some_man = Who('John Doe', 42)
# print(json.dumps(some_man, cls=MyEncoder))

"""{"name": "John Doe", "age": 42}"""

# import json


# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# def encode_who(w):
#     if isinstance(w, Who):
#         return w.__dict__
#     else:
#         raise TypeError(w.__class__.__name__ + 'is not JSON serializable')


# def decode_who(w):
#     return Who(w['name'], w['age'])


# old_man = Who("Jane Doe", 23)
# json_str = json.dumps(old_man, default=encode_who)
# new_man = json.loads(json_str, object_hook=decode_who)
# print(type(new_man))
# print(new_man.__dict__)

"""{"name": "Jane Doe", "age": 43}"""


import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)
