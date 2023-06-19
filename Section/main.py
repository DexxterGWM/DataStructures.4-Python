print('\n\t Sorting Algorithms\n\t #Section 4')

# Challenge

'''
As a developer at a consulting firm, you are still assigned to a client that needs to ingest data from a new source and treat it. You've already made a delivery where you implemented a solution that does the dedup on a list of CPFs, returns only the numerical part of the CPF and checks if they have 11 digits.
Customers approved the solution, but requested that the list of valid CPFs be delivered in ascending order to facilitate registration. They emphasized the need to have a solution capable of doing the job for large volumes of data, in the best possible time. Since the list of CPFs can grow exponentially, choosing the most suitable algorithms is important in this case.
Therefore, in this new step, you must both carry out the cleaning and validation transformations in the CPFs (remove the dot and dash, check that it has 11 digits and do not leave duplicate values) and deliver it in ascending order. Which algorithms will you choose to implement the solution? You must provide evidence that you made the right choice!
'''

# // Resolution

# Part 1 - Implement the merge sort sort algorithm

def executeMergeSort(List, start = 0, end = None):
    if not end:
        end = len(List)
        
    if end - start > 1:
        middle = (start + end) // 2
        executeMergeSort(List, start, middle)
        executeMergeSort(List, middle, end)
        executeMerge(List, start, middle, end)

    return List

def executeMerge(List, start, middle, end):
    left = List[start:middle]
    right = List[middle:end]
    topLeft = topRight = 0

    for p in range(start, end):
        if topLeft >= len(left):
            List[p] = right[topRight]
            topRight += 1
        elif topRight >= len(right):
            List[p] = left[topLeft]
            topLeft += 1
        elif left[topLeft] < right[topRight]:
            List[p] = left[topLeft]
            topLeft += 1
        else:
            List[p] = right[topRight]
            topRight += 1 

# Part 2 - Implement the binary search algorithm

def executeBinarySearch(List, value):
    minimum = 0
    maximum = len(List) - 1

    while minimum <= maximum:
        middle = (minimum + maximum) // 2
        if value < List[middle]:
            maximum = middle - 1
        elif value > List[middle]:
            minimum = middle + 1
        else: return True

    return False

# Part 3 - Implement the function that checks the cpf, the dedup and returns the expected result

def createOrderedDedupList(List):
    List = [str(cpf).replace('.','').replace('-','') for cpf in List]
    List = [cpf for cpf in List if len(cpf) == 11]
    List = executeMergeSort(List)
    
    listDedup = []
    for cpf in List:
        if not executeBinarySearch(listDedup, cpf):
            listDedup.append(cpf)
    return listDedup

# Part 4 - Create a test function

def testFunction(listCpfs):
    listDedup = createOrderedDedupList(listCpfs)
    print(f'\n ——————————\n {listDedup}\n ——————————\n')
    
listCpfs = ['44444444444', '111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
testFunction(listCpfs)

# // Internet Challenge

'''
The website https://www.hackerrank.com/ is a great option for those who want to train their programming skills. In this portal, it is possible to find several challenges, divided by category and programming language. On the home page, you will find the option for companies and for developers. Choose the second and register.
After registering, log in to access the challenges dashboard. Navigate to the algorithms option and click on it. A new page will open, on the right side of which you must choose the "sort" subdomain to access the relevant challenges to search algorithms. Try to solve the "Insertion Sort - Part 1" challenge!
'''

# Resolution

'''
Complete the 'insertionSort1' function below.

The function accepts following parameters:
    1. INTEGER n
    2. INTEGER_ARRAY arr
'''

def insertionSort(size, nums):
    tmp = nums[-1]
    for i in range(size - 2, -1, -1):
        if nums[i] > tmp:
            nums[i+1] = nums[i]
            print(' '.join(map(str, nums)))
        
        else:
            nums[i+1] = tmp
            print(' '.join(map(str, nums)))
            return

    nums[0] = tmp
    print(' '.join(map(str, nums)))

size = int(input())
nums = list(map(int, input().rstrip().split()))

insertionSort(size, nums)

'''
if __name__ == '__main__':
    size = int(input())
    nums = list(map(int, input().rstrip().split()))

    insertionSort(size, nums)
'''
