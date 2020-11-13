import eulerlib


def shareDigits(nums: list[int]) -> bool:
    for i in range(len(str(nums[0]))):
        for n in range(8):
            if str(n)[i] == str(n)[i+1] == str(n)[i+2]:


def test_getFactors():
    assert getFactors(230) == {2, 5, 23}
