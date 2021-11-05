# importing importing built-in library to store
# our pairs
import collections
def matchingSocks(pairs):
    # the collections.Counter() is a builtin python dictionary which 
    # return the individual pairs and their frequencies and
    # stores them in a dictionary 
    
    socks_frequency = collections.Counter(pairs)
        
    # variable to hold our final result
    total_pairs = 0
    
    # loop throuh the dictionary to check the frequency
    for pair in socks_frequency:
        # To get the total pairs for a socks we divide 
        # its frequency by two and incrementing the total_pairs
        total_pairs += socks_frequency[pair] // 2
    
    # the function returns the total_pairs 
    return total_pairs


# Testing on the 2 arrays as instructed in the rubric 
testcase_1 = [6,1,2,4,19,5,6,7,1,3,4,5,11,15,17,1,20,20,2,3,4,5,6,7,1,2,2,2,13,18]
testcase_2 = [2,4,5,6,7,1,3,4,5,6,7,1,2,2,20,90,67,87,27,88,100,1,20,20,2,3,4,5,6,1,2,4,5,6,7,1,3,4,5,6,7,1,2,2,2,90,67,87,1,20,20,2,3,4,5,6,1,2,4,5,6,7,1,3,4,5,6,7,1,2,27,88,100,2,2,90,67,87,27,88]


# Print the result of the tests done 
print("Lenght of the testcase_1: " + str(len(testcase_1)), "and it returns " + str(matchingSocks(testcase_1)) + " pairs")
print("Lenght of the testcase_2: " + str(len(testcase_2)), "and it returns " + str(matchingSocks(testcase_2)) + " pairs")
