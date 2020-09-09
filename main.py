from linked_list import LinkedList, Node
from statistics import stdev

def calculate_mean(linked_list: LinkedList) -> float:
    node = linked_list.head
    total_sum = 0
    size = 0
    while node is not None:
        total_sum += node.data
        size += 1
        node = node.next
    return total_sum/size

def calculate_standard_deviation(linked_list: LinkedList) -> float:
    return stdev(linked_list.get_simple_list())

def get_valid_input():
    inpt = inpt = input('Please enter a NUMBER or type NEXT to proceed:\n')

    if inpt.lower() == 'next':
        return 'next'

    try:
        number = float(inpt)
    except ValueError:
        print('You have entered an invalid input, please try again\n')
        number = get_valid_input()

    return number

def test_calculation_methods() -> bool:
    list_a = [160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503]
    list_b = [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

    expected_mean_a = 550.6
    expected_mean_b = 60.32

    expected_std_dev_a = 572.03
    expected_std_dev_b = 62.26

    linked_list_a = LinkedList()
    linked_list_a.dump_from_simple_list(list_a)

    actual_mean_a = calculate_mean(linked_list_a)
    actual_std_dev_a = calculate_standard_deviation(linked_list_a)

    linked_list_b = LinkedList()
    linked_list_b.dump_from_simple_list(list_b)

    actual_mean_b = calculate_mean(linked_list_b)
    actual_std_dev_b = calculate_standard_deviation(linked_list_b)

    print('expected mean for list a:', expected_mean_a)
    print('actual mean for list a:', actual_mean_a)

    print('expected mean for list b:', expected_mean_b)
    print('actual mean for list b:', actual_mean_b)

    print('expected std. dev. for list a:', expected_std_dev_a)
    print('actual std. dev. for list a:', actual_std_dev_a)

    print('expected std. dev. for list b:', expected_std_dev_b)
    print('actual std. dev. for list b:', actual_std_dev_b)

def main():
    keep_asking = True

    numbers = LinkedList()

    inpt = get_valid_input()

    node = Node(inpt)
    numbers.head = node
    first_loop = True
    last_node = node

    while keep_asking:
        inpt = get_valid_input()
        if inpt == 'next':
            break
        next_node = Node(inpt)
        last_node.next = next_node
        last_node = next_node

    print('linked list:', numbers)

    print('mean:', calculate_mean(numbers))

    print('standard deviation:', calculate_standard_deviation(numbers))

if __name__ == "__main__":
    #test_calculation_methods()
    main()
