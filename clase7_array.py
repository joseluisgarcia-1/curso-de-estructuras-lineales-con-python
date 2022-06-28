class Array():
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
        
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self,index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    
menu = Array(5)
print(len(menu))
for i in range(len(menu)):
    menu[i] = i+1
print(menu)
print()
for option in menu:
    print((menu[option-1]))
print()
print(menu.__len__())
print()
print(menu.__str__())
print()
print(menu.__iter__())
print()
print(menu.__getitem__(3))
print()
print(menu.__setitem__(1,30))
print()
print(menu.__getitem__(1))