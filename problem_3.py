def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Example
print(count_vowels("Hello World"))  # 3



