import odd_even
import pytest

@pytest.mark.parametrize("x,result",[(2,True),(3,False),(4,False),(5,False),(6,True)])
def test_odd_even(x,result):
    oddeven=odd_even.odd_even(x)
    assert oddeven == result
