sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(word_lengths)

word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)


# create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(n) for n in numbers if n > 0]
print(newlist)


def foo(first, second, third, *therest):
    print("First: %s" %first)
    print("Second: %s" %second)
    print("Third: %s" %third)
    print("And all the rest... %s" %list(therest))


foo(1,2,3,4,5)


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print("Result: %d" % result)


# edit the functions prototype and implementation
def foo(a, b, c, *extra):
    print(type(extra))
    return len(extra)


def bar(a, b, c, **options):
    print(type(options))
    return True if options["magicnumber"] == 7 else False


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")

if foo(1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c') == 7:
    print("Best.")
if not bar(1, 2, 3, magicnumber=6):
    print("Great.")
if bar(1, 2, 3, magicnumber=7):
    print("Awesome!")