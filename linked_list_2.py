class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data
            itr = itr.prev
        return llstr

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    # def insert_at_begining(self, data):
    #     if self.head == None:
    #         node = Node(data, self.head, None)
    #         self.head = node
    #     else:
    #         node = Node(data, self.head, None)
    #         self.head.prev = node
    #         self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    str1 = input("Enter first number")
    str2 = input("Enter second number")
    ll.insert_values(list(str1))
    first_number_reverse = ll.reverse()
    ll.insert_values(list(str2))
    second_number_reverse = ll.reverse()

    sum_both = str(int(first_number_reverse) + int(second_number_reverse))

    ll.insert_values(list(sum_both))

    final_answer = ll.reverse()

    print("My final answer is ", final_answer)

