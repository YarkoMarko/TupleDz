class Dictionary:
    __dict = {}

    def show(self):
        if self.__dict is not None:
            lst_keys = self.__dict.keys()

            for i in lst_keys:
                print(f"{i}: {self.__dict[i]}")

        else:
            print("Dictionary is empty")

    def add(self):
        lst_keys = self.__dict.keys()

        english_word = input("Enter english word: ")

        if english_word not in lst_keys:
            self.__dict[english_word] = input("Enter french translation: ")

        else:
            print(f"{english_word} is in dictionary")

    def delete(self):
        lst_keys = self.__dict.keys()

        english_word = input("Enter english word: ")

        if english_word in lst_keys:
            self.__dict.pop(english_word)

        else:
            print(f"{english_word} is not in dictionary")

    def edit(self):
        lst_keys = self.__dict.keys()

        english_word = input("Enter english word: ")

        if english_word in lst_keys:
            self.__dict[english_word] = input("Enter new translation: ")

        else:
            print(f"{english_word} is not in dictionary")


d = Dictionary()

d.add()
d.add()
d.add()

d.show()

d.edit()

d.show()