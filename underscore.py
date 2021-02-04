class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable

    def filter(self, iterable, callback):
        new_list = []
        for i in range(len(iterable)):
            if callback(iterable[i]):
                new_list.append(iterable[i])
        return new_list

    def reject(self, iterable, callback):
        new_list = []
        for i in range(len(iterable)):
            if not callback(iterable[i]):
                new_list.append(iterable[i])
        return new_list

    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]

_ = Underscore()
square = _.map([1, 2, 3, 4], lambda num: num*num)
evens = _.filter([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0)
odds = _.reject([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0)
even = _.find([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0)

print(square)
print(evens)
print(odds)
print(even)

# Print Output:
# [1, 4, 9, 16]
# [2, 4, 6]
# [1, 3, 5]
# 2