test_results = [37,51,44,23,78,92,39,84,83,51]

minimum_results = [70, 40, 30]

def min_pts(limit):
   return lambda pts: pts>=limit

for min in minimum_results:
    print(list(filter(min_pts(min), test_results)))