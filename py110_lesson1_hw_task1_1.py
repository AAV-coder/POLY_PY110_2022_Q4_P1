some_iterable = ('sds', 'ruer', 'qwa')


if __name__ == "__main__":
   enum = zip(range(len(some_iterable)), some_iterable)


print(next(enum))
print(next(enum))
print(next(enum))
print(next(enum))

