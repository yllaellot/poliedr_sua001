from pytest import approx
from math import sqrt
from shadow.polyedr import Polyedr


class TestPolyedr:

    def test_polyedr_1(self):
        assert Polyedr(f"data/test1.geom")._lenght() == approx(1.0)

    def test_polyedr_2(self):
        assert Polyedr(f"data/test2.geom")._lenght() == approx(0.0)

    def test_polyedr_3(self):
        assert Polyedr(f"data/test3.geom")._lenght() == 0.0

    def test_polyedr_4(self):
        assert Polyedr(f"data/test4.geom")._lenght() == 0.0

    def test_polyedr_5(self):
        assert Polyedr(f"data/test5.geom")._lenght() == approx(1.0)

    def test_polyedr_6(self):
        assert Polyedr(f"data/test6.geom")._lenght() == approx(4.0)

    def test_polyedr_7(self):
        assert Polyedr(f"data/test7.geom")._lenght() == approx(3.0)
