class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  

    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index should be 1 or greater.")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node at position {n} with value {deleted_data}")
                return

            current = self.head
            prev = None
            count = 1

            while current and count < n:
                prev = current
                current = current.next
                count += 1

            if not current:
                raise IndexError("Index out of range.")

            deleted_data = current.data
            prev.next = current.next
            print(f"Deleted node at position {n} with value {deleted_data}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    ll = LinkedList()
    print("Adding nodes:")
    try:
        N = int(input("Enter the number of nodes to add: "))
        if N <= 0:
            raise ValueError("Number of nodes must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        exit(1)

    for _ in range(N):
        data = input("Enter node data: ")
        ll.add_node(data)

    ll.print_list()
    print()

    try:
        n = int(input("Enter the node position to delete (1-based index): "))
        ll.delete_nth_node(n)
    except ValueError:
        print("Please enter a valid integer.")

    ll.print_list()

    print("\nDeleting 10th node:")
    ll.delete_nth_node(10)

    print("\nDeleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nDeleting remaining nodes:")
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTrying to delete from empty list:")
    ll.delete_nth_node(1)