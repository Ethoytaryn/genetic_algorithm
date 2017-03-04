from src.Tools.Math import moyenne, variance


class TestMath:

    tableau = [2, 2, 2, 2, 2]

    def test_moyenne(self):
        assert moyenne(self.tableau) == 2
        assert type(moyenne(self.tableau)) == float

    def test_variance(self):
        assert variance(self.tableau) == 0
        assert type(moyenne(self.tableau)) == float
