
# create an empty list to store marks
marks = []

# open the file "marks.txt" in read mode
# "with" ensures the file is automatically closed after use
with open("week1\\WEEK2\\marks.txt", "r") as file:

    # loop through each line of the file
    for line in file:

        # remove extra spaces or newline characters like \n
        clean_line = line.strip()

        # convert the string into an integer
        mark = int(clean_line)

        # add the mark to the list
        marks.append(mark)


# create variable to store total marks
total = 0

# loop through each mark in the list
for m in marks:

    # add each mark to total
    total = total + m


# calculate average using total marks divided by number of marks
average = total / len(marks)


# assume the first mark is the highest initially
highest = marks[0]

# loop through marks to find the real highest value
for m in marks:

    # if current mark is greater than highest
    if m > highest:

        # update highest value
        highest = m


# print the complete marks list
print("Marks:", marks)

# print average marks
print("Average:", average)

# print highest mark
print("Highest:", highest)