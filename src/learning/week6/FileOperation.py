"""
File: FileOperation.py
Author: Shiqi Su
Date: 2025-09-12 19:40
Description: Learning how to operate files through Python.
"""
import os

os.getcwd()
'/Users/sushiqi/PycharmProjects/python-learning-lab/src/learning/week6'


# First method to open, iterate lines, and close file.
# file = open('Test.txt', 'r')
# for line in file:
#     line
# file.close()
#
# # Second method to automatically close file.
# with open('Test.txt', 'r') as file_test:
#     for line in file_test:
#         print(line)

# Calculate the count of empty lines in the file.
# def foo(file_name: str):
#     """
#     Count the number of empty lines in a given text file.
#
#     Args:
#         file_name (str): Path to the text file to be read.
#
#     Returns:
#         int: The number of empty lines (lines that contain only a newline character) in the file.
#     """
#
#     count = 0
#     with open('Test.txt', 'r') as file_lines:
#         for line in file_lines:
#             if line == '\n':
#                 count += 1
#     return count
#
#
# print(foo('Test.txt'))
#
# Open the file through absolutely path.
# file = open('/Users/sushiqi/PycharmProjects/python-learning-lab/src/learning/week6/Test.txt', 'r')
# for line in file:
#     print(line)
#
#
# def foo2(file_name: str) -> list[int]:
#     """
#     Find all numbers in the file, then show in a list.
#     Args:
#         file_name (str): Path to the test file to be read.
#
#     Returns:
#         list[int]: A
#
#     """
#     with open('Test.txt', 'r') as file:
#         ans = []
#         for line in file:
#             ans.append(int(line))
#     return ans
#
#
# print(foo2('Test.txt'))
#
# def find_highest_rating(file_name: str) -> str:
#     """
#     Return the name of the bank that has the highest rating.
#     Args:
#         file_name (str):
#
#     Returns:
#         str: The band name.
#
#     """
#     highest_rating_band_name = ''
#     rating_num = -1
#     with open('Band.txt', 'r') as file:
#         file.readline()
#         for line in file:
#             band, rating, _ = line.split(',')
#             print(band, rating)
#             rating = int(rating)
#             if rating > rating_num:
#                 rating_num = rating
#                 highest_rating_band_name = band
#         return highest_rating_band_name
# print(find_highest_rating('Band.txt'))

# def write_file(file_name: str):
#     f = open('Test.txt', 'w')
#     f.write('This is a number text \n')
#     text = ['look \n', 'in \n', 'my \n', 'eyes \n', 'I\'m \n', 'SuperStar! \n']
#     # for word in text:
#     #     f.write(word + '\n')
#     f.writelines(text)
#     f.close()





def make_all_caps(in_filename: str, out_file_name: str):
    """
    Covert all characters in 'In_filename' to caps and save to 'Out_filename'.

    Args:
        in_filename (str): Name of the file from which to read the data.
        out_file_name (str): Name of the file to which the data is to be saved.

    Returns:

    """
    in_text = [' I \n hope \n everyone \n can \n find \n\n their \n happiness \n']

    # Input operation
    with open('In_filename.txt', 'w') as fin_w:
        fin_w.writelines(in_text)

    with open('In_filename.txt', 'r') as fin_r:
        print(fin_r.readlines())

    with (open('Out_filename.txt', 'w') as fon_w,
          open('In_filename.txt', 'r') as fin_rr):
        for line in fin_rr:
            fon_w.write(line.upper())

    with open('Out_filename.txt', 'r') as fon_r:
        print(fon_r.readlines())

make_all_caps('In_filename.txt', 'Out_filename.txt')



