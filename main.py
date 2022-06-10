alphabet_size = 256
modulus = 1000003


def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return False

    p_hash = 0
    text_hash = 0
    modulus_power = 1
    count = 0

    for i in range(p_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        if i == p_len - 1:
            continue
        modulus_power = (modulus_power * alphabet_size) % modulus

    for i in range(0, t_len - p_len + 1):
        if text_hash == p_hash and text[i: i + p_len] == pattern:
            count += 1
        if i == t_len - p_len:
            continue
        text_hash = ((text_hash - ord(text[i]) * modulus_power) * alphabet_size + ord(text[i + p_len])) % modulus
    return count


if __name__ == "__main__":
    pattern = "12k23"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1a" \
            "bc12sfabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
            "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12s" \
            "fabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
            "alskfjaldsabc1abc1abc12kas23adsfabcabcalskfjaldsk23adasadbc1abc12s" \
            "fabcabcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
            "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabc" \
            "abcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
            "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabc" \
            "abcalskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcabc" \
            "alskfjaldsabc1abc1abc12k23adsfabcabcalskfjaldsk23adasadbc1abc12sfabcab" \

    print(rabin_karp(pattern, text1))