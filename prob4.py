def find_intersection(list1, list2):
    
   intersection = list(filter(lambda x: x in list2, list1))
   return intersection

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)
print("Intersection:", intersection)