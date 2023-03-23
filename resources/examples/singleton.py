class Singleton:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance == None:
            cls._instance = cls()
        return cls._instance


instance1 = Singleton.instance()
instance2 = Singleton.instance()
instance3 = Singleton.instance()
print(instance1, instance2, instance3)
