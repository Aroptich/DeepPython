class Last_name:

    @classmethod
    def symbols(cls, text: str):
        if not text.isalpha():
            raise TypeError('В инициалах должны быть только буквы!')


    @classmethod
    def verify_last_name(cls, last_name: str) -> str:
        return last_name.capitalize()

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        value = self.verify_last_name(value)
        self.symbols(value)
        setattr(instance, self.name, value)
