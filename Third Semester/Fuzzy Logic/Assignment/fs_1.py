class CrispSet:
    def __init__(self):
        self.elements = []
        self.memberships = []
        self.total_elements = []

    def add_element(self, element, membership):
        if membership != 0 and membership != 1:
            print("Invalid membership value. Membership value should be either 0 or 1.")
            again_membership = float(input(f"Enter membership value of {element} AGAIN! (either 0 or 1): "))
            self.elements.append(element)
            self.memberships.append(again_membership)
        else:
            self.elements.append(element)
            self.memberships.append(membership)

    def add_total_element(self, element):
        self.total_elements.append(element)


    def union(self, other_set):
        union_set = CrispSet()
        for element in self.elements:
            if element in other_set.elements:
                membership = max(self.memberships[self.elements.index(element)], other_set.memberships[other_set.elements.index(element)])
            else:
                membership = self.memberships[self.elements.index(element)]
            if membership == 1:
                union_set.add_element(element, membership)
        for element in other_set.elements:
            if element not in self.elements:
                membership = other_set.memberships[other_set.elements.index(element)]
                if membership == 1:
                    union_set.add_element(element, membership)
        return union_set

    def intersection(self, other_set):
        intersection_set = CrispSet()
        for element in self.elements:
            if element in other_set.elements:
                membership = min(self.memberships[self.elements.index(element)], other_set.memberships[other_set.elements.index(element)])
                if membership == 1:
                    intersection_set.add_element(element, membership)
        return intersection_set

    def complement(self, other_set):
        complement_set = CrispSet()
        
        for i in range(len(other_set.total_elements)):
          if other_set.total_elements[i]  in self.elements and self.memberships[self.elements.index(element)] == 0:
            complement_set.add_element(other_set.total_elements[i], 1)

          if other_set.total_elements[i] not in self.elements:
            complement_set.add_element(other_set.total_elements[i], 1)

        return complement_set

    def subset(self, other_set):
        for i in range(len(other_set.elements)):
            if other_set.elements[i] not in self.elements or self.memberships[self.elements.index(other_set.elements[i])] < other_set.memberships[i]:
                return False
        return True

    def print_set(self):
        for i in range(len(self.elements)):
            print(self.elements[i], self.memberships[i])

    def print_data(self):
        for i in range(len(self.total_elements)):
            print(self.total_elements[i])


total = CrispSet()

total_elements = int(input("Enter the total number of elements in the set: "))

for i in range(total_elements):
    element = input(f"Enter element {i+1}: ")
    total.add_total_element(element)



set1 = CrispSet()

total_elements = int(input("Enter the total number of elements in the set A: "))

for i in range(total_elements):
    element = input(f"Enter element {i+1} for set A: ")
    membership = int(input(f"Enter membership value of {element} in set A (0 or 1): "))
    set1.add_element(element, membership)

set2 = CrispSet()
total_elements = int(input("Enter the total number of elements in the set B: "))
for i in range(total_elements):
    element = input(f"Enter element {i+1} for set B: ")
    membership = int(input(f"Enter membership value of {element} in set B (0 or 1): "))
    set2.add_element(element, membership)

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)

total.print_data()

print("\nSet 1:")
set1.print_set()
print("\nSet 2:")
set2.print_set()
print("\nUnion Set:")
union_set.print_set()
print("\nIntersection Set:")
intersection_set.print_set()

print("\nComplement of Set A:")
complement_set1 = set1.complement(total)
complement_set1.print_set()

print("\nComplement of Set B:")
complement_set2 = set2.complement(total)
complement_set2.print_set()

print("\nIs Set 2 a subset of Set 1?", set1.subset(set2))
print("Is Set 1 a subset of Set 2?", set2.subset(set1))