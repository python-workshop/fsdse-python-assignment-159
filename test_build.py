import sys
from build import search_sorted_array
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(search_sorted_array(range(1,10),4,1,9)) # non duplicate item
test(search_sorted_array([12,45,85,6,4,8,7,4],4,1,9)) # Duplicate Item
test(search_sorted_array([12,45,85,6,4,8,7],None,1,9)) # value is none
