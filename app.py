#code to extract all zeros to left and all non zeros to right

mylist=[0,3,5,0,56,23]
mylist2= [i for i in mylist if i==0]+[i for i in mylist if i!=0]
print(mylist2)

# code to find the largest and smallest elements in a list
--------------------------------------------------------------
list1 = [3, 45, 87, 21, 90, 21]

largest = list1[0]
smallest = list1[0]
for i in list1:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)

----------------------------------------------------------------
#Factorial Program
n = 5
fact = 1

for i in range(1, n+1):
    fact = fact * i

print(fact)

-----------------------------------------------------------------

def ladderLength(beginWord, endWord, wordList):

    word_set = set(wordList)

    if endWord not in word_set:
        return 0

    begin_set = {beginWord}
    end_set = {endWord}

    visited = set()
    level = 1

    while begin_set and end_set:

        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set

        next_level = set()

        for word in begin_set:

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":

                    new_word = word[:i] + c + word[i+1:]

                    if new_word in end_set:
                        return level + 1

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        next_level.add(new_word)

        begin_set = next_level
        level += 1

    return 0

----------------------------------------------------------------------------------

#code for fibbo
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fib(10)
----------------------------------------------------------------------------------
import json
import boto3
import pandas as pd
from io import BytesIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    records = []

    # read Firehose records
    for record in event['records']:
        payload = json.loads(record['data'])
        records.append(payload)

    # convert to dataframe
    df = pd.DataFrame(records)

    # basic transformation
    df['processed_time'] = pd.Timestamp.now()

    # convert to parquet
    buffer = BytesIO()
    df.to_parquet(buffer, index=False)

    # upload to S3
    s3.put_object(
        Bucket='my-processed-bucket',
        Key='processed/data.parquet',
        Body=buffer.getvalue()
    )

    return {"status": "success"}

-----------------------------------------------------------------------------
#Find the largest number in a list
def find_max(nums):
    max_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num

    return max_num


---------------------------------------------------------------------------
#Group of anagram

input1 = ["eat","tea","act","ate","cat","bat","silent","listen", "madam"]

from collections import defaultdict

def group_anagram(words):
    anagram_map = defaultdict(list)

    for word in words:
        key = "".join(sorted(word.lower()))
        anagram_map[key].append(word)

    return list(anagram_map.values())


print(group_anagram(input1))

--------------------------------------------------------------------------
# group of anagram

def group_anagrams(words):
    anagram_map = {}

    for word in words:
        key = ''.join(sorted(word))  # sort letters

        if key not in anagram_map:
            anagram_map[key] = []

        anagram_map[key].append(word)

    return list(anagram_map.values())


# example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

----------------------------------------------------------------------
#code for non repeating character 
def first_non_repeating(s: str):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None


# Taking input from user
s = input("Enter string: ")

result = first_non_repeating(s)

if result:
    print("First non-repeating character is:", result)
else:
    print("No non-repeating character found")

--------------
