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

--------------------------------------------------------
#This is a modular function-based design where each step—calculation, discount, and shipping—is handled independently, forming a small data processing pipeline.
from __future__ import print_function, division


def calculate_totals(cart_items):
    totals = []
    for cart in cart_items:
        totals.append(round(sum(cart), 2))
    return totals


def apply_discounts(cart_totals):
    discounted_totals = []

    for total in cart_totals:
        if total < 50:
            final = total
        elif total < 100:
            final = total * 0.90
        elif total < 200:
            final = total * 0.85
        else:
            final = total * 0.80

        discounted_totals.append(round(final, 2))

    return discounted_totals


def calculate_shipping(final_totals):
    shipping_costs = []

    for total in final_totals:
        if total < 25:
            cost = 10.00
        elif total < 75:
            cost = 5.00
        else:
            cost = 0.00

        shipping_costs.append(round(cost, 2))

    return shipping_costs


def main():
    func = int(input())
    n = int(input())

    cart_items = []
    for _ in range(n):
        cart_items.append(list(map(float, input().split())))

    totals = calculate_totals(cart_items)

    if func == 1:
        result = totals
    elif func == 2:
        result = apply_discounts(totals)
    else:
        discounted = apply_discounts(totals)
        result = calculate_shipping(discounted)

    print(*["{:.2f}".format(x) for x in result])


if __name__ == "__main__":
    main()
==========================================================================
