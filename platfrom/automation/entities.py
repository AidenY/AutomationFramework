class teststep():
    def __init__(self, step, test_object_name, test_object_value, addition_infos=[]):
        self.__step = step
        self.__test_object_name = test_object_name;
        self.__test_object_value = test_object_value
        self.__addition_infos = addition_infos;
        pass

    @property
    def step(self):
        return self.__step

    @property
    def test_object_name(self):
        return self.__test_object_name

    @property
    def test_object_value(self):
        return self.__test_object_value

    @property
    def addition_infos(self):
        return self.__addition_infos


class testobject():
    def __init__(self, test_object_name, test_object_value):
        self.__test_object_name = test_object_name;
        self.__test_object_value = test_object_value

    @property
    def test_object_name(self):
        return self.__test_object_name

    @property
    def test_object_value(self):
        return self.__test_object_value


class config():
    def __init__(self, key, value):
        self.__key = key;
        self.__value = value

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value
