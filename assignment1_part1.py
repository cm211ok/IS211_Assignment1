
def list_divide(numbers, divide=2):
    count_ = 0
    for i in numbers:
        if i % divide == 0:
            count_ += 1
    return count_
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    pass

class ListDivideException:
    pass

def test_list_divide():
    """
    Test listDivide
    """
    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30, 54, 63,98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5], 1) == 5
    
if __name__ == "__main__":
    testListDivide()
