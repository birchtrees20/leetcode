from is_palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Was it a car or a cat I saw") == True
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("step on no pets") == True
    assert is_palindrome("Eva, can I see bees in a cave?") == True
    assert is_palindrome("Madam, in Eden, I'm Adam") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False
    assert is_palindrome("a") == True
    assert is_palindrome("") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("tacocat") == True
    assert is_palindrome("123321") == True
    assert is_palindrome("palindrome") == False
    assert is_palindrome("abcdba") == False
