class App():
    __instance = None

    @staticmethod
    def get_instance():
        if App.__instance is None:
            App.__instance = App()
        return App.__instance


print(App.get_instance(), App.get_instance())

# ----------------------------------

from unittest import TestCase


class MyTest(TestCase):
    def test_singleton(self):
        first = App()
        second = App()
        self.assertEqual(first, second)


