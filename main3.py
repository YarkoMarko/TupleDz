class Firma:
    __dict = {
        "Surname": "Mykhasiak",
        "Name": "Yarema",
        "Father`s name": "Olegovich",
        "Number": "003543254",
        "Corp email": "asjfbaskj@gmail.com",
        "Position": "sfsasafsa",
        "Cabinat number": "0545",
        "Skype": "hgjdsbhgsdjh"
    }

    def show(self):
        lst_keys = self.__dict.keys()

        for i in lst_keys:
            print(f"{i}: {self.__dict[i]}")

    def add(self):
        lst_keys = self.__dict.keys()

        category = input("Enter new category: : ")

        if category not in lst_keys:
            self.__dict[category] = input("Enter data: ")

        else:
            print(f"{category} is in infocard")

    def delete(self):
        lst_keys = self.__dict.keys()

        category = input("Enter new category: : ")

        if category in lst_keys:
            self.__dict.pop(category)

        else:
            print(f"{category} is not in infocard")

    def edit(self):
        lst_keys = self.__dict.keys()

        category = input("Enter new category: : ")

        if category in lst_keys:
            self.__dict[category] = input("Enter new translation: ")

        else:
            print(f"{category} is not in dictionary")

