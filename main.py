"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x - 1) + foo(x - 2)
    
    print foo(12)
    

def longest_run(mylist, key):
    count = 0
    max = 0
    for x in mylist:
      if x == key:
        count += 1
        if count > max:
          max = count
        else:
          count = 0
    return max 


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def merge(result, result_):
  if result.is_entire_range:
    if result_.is_entire_range:
      longestrun = result.left_size + result_.left_size
      testres = Result(longestrun, longestrun, longestrun, True)
      return testres
    else:
      leftresult = result.left_size + result_.left_size
  else:
    leftresult = result.left_size

  if result_.is_entire_range:
    rightresult = result.right_size + result_.left_size
  else:
    rightresult = result_.right_size

  combine_res = result.right_size + result_.left_size

  longestres = result.longest_size
  longestres_ = result_.longest_size

  maxrun = max(longestres, longestres_)
  if combine_res > maxrun:
    testres = Result(leftresult, rightresult, combine_res, False)
    return testres
  else:
    testres = Result(leftresult, right result, maxrun, False)
    return testres
    
def longest_run_recursive(mylist, key):
  if len(mylist) == 1 and mylist[0] == key:
    testrest = Result(1, 1, 1, True)
  elif len(mylist) == 1 and mylist[0]!= key:
    testres = Result(0, 0, 0, False)
  else: 
    listlen = len(mylist)//2
    result = longest_run_recursive(mylist[:listlen], key)
    result_ = longest_run_recursive(mylist[listlen:], key)
    testres = merge(result, result_)
    return testres

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
