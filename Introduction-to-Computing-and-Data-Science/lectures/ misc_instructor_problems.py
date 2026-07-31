'''
fUN qUESTIONS gIVEN bY iNSTRUCTOR
'''

# from IPython import get_ipython
# get_ipython().run_line_magic('reset', '-sf')

# %%

from math import hypot
import numpy as np
import matplotlib.pyplot as plt

# %% count matches


def count_matches(d):
    count = 0

    for k, v in d.items():
        if k == v:
            count += 1

    return count


d = {1: 2, 3: 4, 5: 6}
print(count_matches(d))

d = {1: 2, 3: 3, 5: 5}
print(count_matches(d))

# %% list element cleanup


def remove_all(L, e):
    L_copy = L[:]
    L.clear()

    for i in L_copy:
        if i != e:
            L.append(i)


L = [1, 2, 2, 2]
remove_all(L, 2)
print(L)

# %% flatten 3D list to 2D by column indexing

L = [[[1, 2, 3], [4, 5, 6], [10, 11, 12]], [
    [7, 8, 9], [13, 14, 15], [16, 17, 18]]]

L_2D = []

for sub_list in L:
    inner_list = []
    for sub_sub_list in sub_list:
        inner_list.append(sub_sub_list[0])
    L_2D.append(inner_list)

print(L_2D)

# print([[sub_sub_list[0] for sub_sub_list in sub_list] for sub_list in L])
# print(np.array(L)[:,:,0].tolist())

# %% euclidean distance calculator


def distanceFormula(x1, y1, x2, y2):
    return hypot(x1 - x2, y1 - y2)


points = []
for i in range(5):
    point = input(f"Enter two numbers seperated by a comma for point {i+1}: ")
    x, y = map(float, point.split(','))
    points.append((x, y))

print('\nThe points are:')
for i, (x, y) in enumerate(points, start=1):
    print(f"\t\tpoint {i}: ({x}, {y})")

while True:
    p1 = int(input('\nEnter index of first point to calculate distance: ')) - 1
    p2 = int(input('Enter index of second point to calculate distance: ')) - 1

    if 0 <= p1 < 5 and 0 <= p2 < 5:
        x1, y1 = points[p1]
        x2, y2 = points[p2]
        d = distanceFormula(x1, y1, x2, y2)
        print(f'\nThe distance between point {
              p1+1} & point {p2+1} is: {d:.4f}')
        break
    else:
        print('\nINVALID INDEX, please enter a number from 1 and 5')

# %% class grade stats


def get_stats(class_list):
    new_stats = []

    for stu in class_list:
        new_stats.append([stu[0], stu[1], avg(stu[1])])

    return new_stats


def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
        return 0.0


test_grades = [[['peter', 'parker'], [10.0, 55.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 80.0, 75.0]],
               [['captain', 'america'], [80.0, 10.0, 96.0]],
               [['deadpool'], []]]

print(get_stats(test_grades))

# %% word frequency analysis

song = "RAH RAH AH AH AH ROM MAH RO MAH MAH"


def generate_word_dict(song):
    # remove special characters and convert to lowercase
    song_words = song.lower()
    words_list = song_words.split()
    word_dict = {}

    for w in words_list:
        if w in word_dict:
            # seen word again, so add one to frequency
            word_dict[w] += 1
        else:
            # first time seeing word, insert a dict entry with freq 1
            word_dict[w] = 1

    # return is a dict mapping str:int like {'word1':1, 'word2':3}
    return word_dict


word_dict = generate_word_dict(song)
print(word_dict)


def find_frequent_word(word_dict):
    # a list in case there is more than one word occuring that often
    words = []
    highest = max(word_dict.values())  # this is an int

    # loop to find words occurring with `highest` freq
    for k, v in word_dict.items():
        # k is a word and v is its frequency
        if v == highest:
            # word in dict has a value that matches `highest` so append it
            words.append(k)

    # return looks like (['word1', 'word2'], 4)
    return (words, highest)


most_freq = find_frequent_word(word_dict)
print(most_freq)


def occurs_often(word_dict, x):
    freq_list = []
    word_freq_tuple = find_frequent_word(word_dict)

    # repeat for the frequencies greater than 'x'
    while word_freq_tuple[1] > x:
        # extract most frequent word(s) using function we wrote
        word_freq_tuple = find_frequent_word(word_dict)
        # keep track of most common words, append them in order
        freq_list.append(word_freq_tuple)

        # remove every entry that matches words in `word_freq_tuple`
        # so that you are left with next most frequent words
        for word in word_freq_tuple[0]:
            del (word_dict[word])

    return freq_list


print(occurs_often(word_dict, 2))


# %% BATMAN Symbol Equation

xs = np.arange(-7.25, 7.25, 0.01)
ys = np.arange(-5, 5, 0.01)
x, y = np.meshgrid(xs, ys)

eq1 = ((x/7)**2*np.sqrt(abs(abs(x)-3)/(abs(x)-3))+(y/3)**2 *
       np.sqrt(abs(y+3/7*np.sqrt(33))/(y+3/7*np.sqrt(33)))-1)
eq2 = (abs(x/2)-((3*np.sqrt(33)-7)/112)*x **
       2-3+np.sqrt(1-(abs(abs(x)-2)-1)**2)-y)
eq3 = (9*np.sqrt(abs((abs(x)-1)*(abs(x)-.75)) /
       ((1-abs(x))*(abs(x)-.75)))-8*abs(x)-y)
eq4 = (3*abs(x)+.75*np.sqrt(abs((abs(x)-.75)*(abs(x)-.5))/((.75-abs(x)
                                                            )*(abs(x)-.5)))-y)
eq5 = (2.25*np.sqrt(abs((x-.5)*(x+.5))/((.5-x)*(.5+x)))-y)
eq6 = (6*np.sqrt(10)/7+(1.5-.5*abs(x))*np.sqrt(abs(abs(x)-1) /
       (abs(x)-1))-(6*np.sqrt(10)/14)*np.sqrt(4-(abs(x)-1)**2)-y)

colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown']
eqs = [eq1, eq2, eq3, eq4, eq5, eq6]

for f, color in zip(eqs, colors):
    plt.contour(x, y, f, [0], colors=color)

plt.title('Batman Symbol - Equations with Different Colors')
plt.axis('equal')
plt.grid()

plt.show()

# %% trigonometric function plot

x = np.linspace(-2*np.pi, 2*np.pi, 400)

functions = {
    'sin(x)': np.sin(x),
    'cos(x)': np.cos(x),
    'tan(x)': np.tan(x),
    'sec(x)': 1/np.cos(x),
    'csc(x)': 1/np.sin(x),
    'cot(x)': 1/np.tan(x)
}

fig, axes = plt.subplots(2, 3, figsize=(12, 8))


def plot_function(ax, x, y, title, color):
    ax.plot(x, y, label=title, color=color)
    ax.set_title(title)
    ax.set_ylim(-10, 10) if title in ['tan(x)',
                                      'sec(x)', 'csc(x)', 'cot(x)'] else None
    ax.grid(True)
    ax.legend()


for ax, (title, y) in zip(axes.flat, functions.items()):
    plot_function(ax, x, y, title, color='r' if title == 'cos(x)'
                  else 'g' if title == 'tan(x)' else 'm' if title == 'sec(x)'
                  else 'b' if title == 'csc(x)' else 'y')

plt.tight_layout()
plt.show()

# %% exponential functions plot

x = np.linspace(0, np.pi, 1000)

functions = {
    'e^x': np.exp(x)*np.sin(x),
    'e^-x': np.exp(-x),
    '1 - e^(-x)': 1 - np.exp(-x),
    '-e^x': -np.exp(x),
    '1 - e^x': 1 - np.exp(x),
    'sin(x)*e^(|x|)':  np.sin(x) * np.where(x >= 0, np.exp(-x), np.exp(x)),
}

fig, axes = plt.subplots(2, 3, figsize=(12, 8))


def plot_function(ax, x, y, title, color):
    ax.plot(x, y, label=title, color=color)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()


colors = ['b', 'r', 'g', 'm', 'b', 'y']

for ax, (title, y), color in zip(axes.flat, functions.items(), colors):
    plot_function(ax, x, y, title, color)

plt.tight_layout()
plt.show()
