# %% palindrome checker (reversing the string)


def palindrome_checker1(input_string: str) -> bool:
    # making the string clean
    cleaned_string = ''.join(char.lower()
                             for char in input_string if char.isalnum())

    # compare the string with its reverse
    if cleaned_string == cleaned_string[::-1]:
        # if they are the same, it's a palindrome
        return True
    # otherwise, it's not a palindrome
    return False


print("\nMethod 1 - String Reversal:")
print(f"'Gate-man sees name, garage-man sees name-tag': {
      palindrome_checker1('Gate-man sees name, garage-man sees name-tag')}")
print(f"'Never odd or even': {palindrome_checker1('Never odd or even')}")
print(f"'racecar': {palindrome_checker1('racecar')}")
print(f"'hello': {palindrome_checker1('hello')}")
print(f"'Madam': {palindrome_checker1('Madam')}")
print(f"'Was it a car or a cat I saw?': {
      palindrome_checker1('Was it a car or a cat I saw?')}")
print(f"'12321': {palindrome_checker1('12321')}")
print(f"'A': {palindrome_checker1('A')}")
print(f"'': {palindrome_checker1('')}\n")

# %% palindrome checker (two pointer method)


def palindrome_checker2(input_string: str) -> bool:
    # making the string clean
    cleaned_string = ''.join(char.lower()
                             for char in input_string if char.isalnum())

    # set two pointers: one at the start and one at the end of the string
    l, r = 0, len(cleaned_string) - 1

    # loop until the two pointers meet
    while l < r:
        # if the characters at the pointers don't match
        if cleaned_string[l] != cleaned_string[r]:
            # The string is not a palindrome
            return False

        # move the left pointer to the right, and the right pointer to the left
        l += 1
        r -= 1

    # if all characters match, it's a palindrome
    return True


print("Method 2 - Two Pointer:")
print(f"'A man, a plan, a canal, Panama!': {
      palindrome_checker2('A man, a plan, a canal, Panama!')}")
print(f"'Never odd or even': {palindrome_checker2('Never odd or even')}")
print(f"'python': {palindrome_checker2('python')}")
print(f"'Able was I ere I saw Elba': {
      palindrome_checker2('Able was I ere I saw Elba')}")
print(f"'No lemon, no melon': {palindrome_checker2('No lemon, no melon')}")
print(f"'Step on no pets': {palindrome_checker2('Step on no pets')}")
print(f"'12345': {palindrome_checker2('12345')}")
print(f"'A Santa at NASA': {palindrome_checker2('A Santa at NASA')}")
print(f"'not a palindrome': {palindrome_checker2('not a palindrome')}")
