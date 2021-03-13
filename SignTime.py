# Cyrus Otero
# Sign Time boi

from SignMath import mathMode
import random

wordZ = open('10000_words.txt', 'r')
f = wordZ.read().splitlines()


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

# Craft the ol list, added end because I had different plans when I started
class LinkedList:

    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

    def traverse(self):
        current = self.head
        if self.head != None:
            while current.next:
                print(current.data)
                current = current.next
                if current == self.head:
                    break
        else:
            print('gonna need some nodes buddy')

    def append_right(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.head.next = new_node
            self.end = new_node

        if self.end != None:
            self.end.next = new_node
            new_node.next = self.head
            self.end = new_node
            return

    def append_left(self, data):
        new_node = Node(data)
        new_node.next = self.head
        current = self.head

        if current == None:
            self.head = new_node
            self.end = new_node
            self.head.next = new_node
            return

        if self.end != None:
            self.end.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

signTime = LinkedList()

# Function that takes the output from SignMath.py and crafts the amount of slides that would have been seen
def sign_crafter(slide):
    slide = slide
    num = 2
    for i in range(slide):
        for i in range(num): 
            wrd = ''
            wrd += f'{random.choice(f).capitalize()} {random.choice(f).capitalize()}'
        signTime.append_left(f'|{wrd}|')


iCommandYoutoWork = mathMode()

maybe = iCommandYoutoWork.userExperience()

# Splits the tuple output into two separate variables
frickinsickin = maybe[0]
yupthisllwork = maybe[1]

# Had a bug that would not generate any nodes if the value of signs was an integer between 1 and 0
# defaulted values less than 1 to 1
if frickinsickin < 1:
    frickinsickin = 1
    sign_crafter(int(frickinsickin))
else:
    sign_crafter(int(frickinsickin))

print(f'{yupthisllwork}% of the slides were viewed')
print(f'This dood sighted {int(frickinsickin)} slides!\n')
print('These were the signs viewed')

signTime.traverse()
wordZ.close()