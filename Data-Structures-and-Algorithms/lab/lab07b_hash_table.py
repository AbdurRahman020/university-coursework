import time
import random


# %% HASH FUNCTIONS

def h0(key, ht_size):
    """Very Simple - always returns 0"""
    return 0


def h1(key, ht_size):
    """First Character ASCII"""
    return ord(key[0]) % ht_size


def h2(key, ht_size):
    """Totaled ASCII Characters using enumerate"""
    x = 0

    for _, ch in enumerate(key):
        x += ord(ch)

    return x % ht_size


def h3(key, ht_size):
    """Radix-128 (position-sensitive)"""
    x = 0

    for _, ch in enumerate(key):
        ascii_code = ord(ch)
        x = 128 * x + ascii_code

    return x % ht_size


# CHALLENGE: OWN HASH FUNCTION(OPTIONAL)

def h4(key, ht_size):
    """
    CHALLENGE: Design your own hash function!

    This uses polynomial rolling hash with prime multiplier (31)
    - Position-sensitive
    - Uses all characters
    - Good distribution
    """
    hash_value = 0
    prime = 31  # common prime for string hashing

    for _, ch in enumerate(key):
        hash_value = hash_value * prime + ord(ch)

    return hash_value % ht_size


# %% HASH TABLE OPERATIONS

def new_hash_table(size):
    """Create a new hash table with 'size' empty buckets"""
    ht = []
    for _ in range(0, size):
        ht.append([])
    return ht


def ht_insert(ht, key, hash_fun):
    """Insert a key into the hash table using specified hash function"""
    if hash_fun == "h0":
        bucket = ht[h0(key, len(ht))]
    elif hash_fun == "h1":
        bucket = ht[h1(key, len(ht))]
    elif hash_fun == "h2":
        bucket = ht[h2(key, len(ht))]
    elif hash_fun == "h3":
        bucket = ht[h3(key, len(ht))]
    elif hash_fun == "h4":
        bucket = ht[h4(key, len(ht))]

    bucket.append(key)


def ht_search(ht, key, hash_fun):
    """Search for a key in the hash table using specified hash function"""
    if hash_fun == "h0":
        bucket = ht[h0(key, len(ht))]
    elif hash_fun == "h1":
        bucket = ht[h1(key, len(ht))]
    elif hash_fun == "h2":
        bucket = ht[h2(key, len(ht))]
    elif hash_fun == "h3":
        bucket = ht[h3(key, len(ht))]
    elif hash_fun == "h4":
        bucket = ht[h4(key, len(ht))]

    for _, value in enumerate(bucket):
        if value == key:
            return True

    return False


# %% STATISTICS FUNCTIONS

def mean_bucket(ht):
    """Returns the arithmetic mean of non-empty bucket sizes"""
    nonempty_buckets = 0
    entries = 0

    for bucket in ht:
        if len(bucket) > 0:
            nonempty_buckets += 1
            entries += len(bucket)

    return entries / nonempty_buckets


def largest_bucket(ht):
    """Returns the size of the largest bucket"""
    max_so_far = 0

    for bucket in ht:
        max_so_far = max(max_so_far, len(bucket))

    return max_so_far


# %% TEST YOUR STATISTICS FUNCTIONS

# test with example from lab
test_ht = [["a", "b"], [], ["w", "x", "y", "z"], ["c"]]

print("Testing statistics functions:")
print(f"Test hash table: {test_ht}")
print(f"largest_bucket: {largest_bucket(test_ht)} (expected: 4)")
print(f"mean_bucket: {mean_bucket(test_ht):.10f} (expected: 2.333...)\n")

# %% PART 1.2 - HASH FUNCTION TESTING WITH SPECIFIC STRINGS


def test_hash_functions():
    """Test hash functions with specific strings from lab instructions"""
    test_strings = ["Hash table", "Table hash", "Towers of Hanoi"]
    ht_size = 100000

    print("=" * 70)
    print("PART 1.2 - HASH FUNCTION RESULTS")
    print("=" * 70)

    for hash_name, hash_func in [("h0", h0), ("h1", h1), ("h2", h2), (
            "h3", h3), ("h4", h4)]:
        print(f"\n   Hash function {hash_name}")

        # add description
        descriptions = {
            "h0": "Very Simple (always returns 0)",
            "h1": "First Character ASCII",
            "h2": "Totaled ASCII Characters",
            "h3": "Radix-128 (position-sensitive)",
            "h4": "Polynomial Rolling Hash (prime multiplier 31)"
        }
        print(f"Description: {descriptions[hash_name]}")

        results = {}
        for s in test_strings:
            result = hash_func(s, ht_size)
            results[s] = result
            print(f'  "{s}": {result}')

        # check for collisions
        values = list(results.values())
        unique_values = set(values)

        if len(values) != len(unique_values):
            print("  Collisions: YES")
            # find which strings collide
            for val in unique_values:
                matching = [k for k, v in results.items() if v == val]
                if len(matching) > 1:
                    print(f"    → {matching} all hash to {val}")
        else:
            print("  Collisions: NO")

    print("\n" + "=" * 70)


# run the test
test_hash_functions()

# %% MAIN EXPERIMENT RUNNER (PART 2.2)


def run(hash_fun):
    """
    Run timing experiments on hash table with specified hash function
    Inserts 100,000 words and searches for 1,000 words
    """
    hash_fun = str(hash_fun)

    # create a hash table with 100,000 buckets
    size = 100000
    start_time = time.time()
    ht = new_hash_table(size)
    end_time = time.time()

    print("=" * 70)
    print(f"RUNNING EXPERIMENT WITH {hash_fun.upper()}")
    print("=" * 70)
    print(f"Created hash table with {size} buckets in {
          end_time - start_time:.6f} seconds")

    # generate random words
    words_array = []
    for _ in range(size):
        word = ""
        random_word_length = random.randint(4, 10)
        for _ in range(random_word_length):
            word = word + chr(random.randint(97, 122))
        words_array.append(word)

    assert size == len(words_array)

    # insert each word into the hash table
    insert_start = time.time()
    for words in words_array:
        ht_insert(ht, words, hash_fun)
    insert_end = time.time()

    print(f"Inserted {len(words_array)} words in {
          insert_end - insert_start:.6f} seconds.")

    # lookup 1000 words
    lookup_start = time.time()
    for _ in range(1000):
        random_word = words_array[random.randint(0, len(words_array) - 1)]
        ht_search(ht, random_word, hash_fun)
    lookup_end = time.time()

    print(f"Searched for 1000 words in {
          lookup_end - lookup_start:.6f} seconds\n")

    # statistics
    print(f"---Statistics for {hash_fun}---\n")
    print(f"Number of entries in largest bucket: {largest_bucket(ht)}")
    print(f"Mean size of non-empty buckets: {mean_bucket(ht):.6f}")
    print("=" * 70)
    print("\n")


# %% RUN EXPERIMENTS FOR h0, h1, h2, h3 and h4

print("\n EXPERIMENT 1: Testing h0 (worst hash function)\n")
run("h0")

print("\n EXPERIMENT 2: Testing h1 (first character)\n")
run("h1")

print("\n EXPERIMENT 3: Testing h2 (sum of characters)\n")
run("h2")

print("\n EXPERIMENT 4: Testing h3 (radix-128, best)\n")
run("h3")

print("\n EXPERIMENT 5: Testing h4 (polynomial rolling hash with prime multiplier)\n")
run("h4")


# %% SUMMARY AND ANALYSIS

print("""
===============================================================================
SUMMARY OF RESULTS
===============================================================================

Expected Performance (from best to worst):
1. h3/h4 - Radix-128 / Polynomial Rolling Hash: Excellent distribution, ~O(1)
2. h2 - Sum ASCII: Good distribution, fast search
3. h1 - First char: Poor distribution, slow search
4. h0 - Constant 0: Terrible, degenerates to linked list, O(n) search

Key Insights:
- Better distribution → Smaller buckets → Faster searches
- h0: All in one bucket (100,000 entries)
- h1: ~26 buckets used (~3,800 entries each)
- h2: Many buckets used (mean ~2-5 entries)
- h3: Best distribution (mean ~1.0 entry per non-empty bucket)
- h4: Comparable to h3 with excellent distribution using prime multiplier

Search time is proportional to average bucket size!

===============================================================================
""")
