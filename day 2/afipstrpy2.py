class person: 
    def_init_(self, name, age): 
    self.name = name 
    self.age = age 
    def_str_(self): 
    return f"{self.name}({self.age})"
p1 = person("jhon", 36) 
print(p1)