import random
class Sorting:

    def __init__(self, n):

        self.lists = [random.randint(1,20) for i in range(n)]
        print(self.lists)

    def buble_sort(self):

        for i in range(len(self.lists)):
            for j in range(i+1,len(self.lists)):
                if self.lists[i] > self.lists[j]:
                    temp = self.lists[i]
                    self.lists[i] = self.lists[j]
                    self.lists[j] = temp

        print(self.lists)


    def selection_sort(self):

        for i in range(len(self.lists)):
            min_pos = i
            for j in range(i, len(self.lists)):
                if self.lists[min_pos] > self.lists[j]:
                    min_pos = j

            temp = self.lists[i]
            self.lists[i] = self.lists[min_pos]
            self.lists[min_pos] = temp

        print(self.lists)
obj = Sorting(10)
#obj.buble_sort()
obj.selection_sort()