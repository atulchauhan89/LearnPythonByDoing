class TestClass():
    hello =1

    def test_one(self):
        x="this"
        assert 'h'in x
    def test_two(self):
        x='hey'


        assert hasattr(object, 'hello')
object = TestClass()