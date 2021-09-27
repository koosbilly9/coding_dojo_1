import os
def get_chr_min_2(character: 'some cool comment') -> "return type is char":
    val = ord(character)
    return chr(val - 2)

if __name__ == "__main__":
    print(get_chr_min_2("b"))
    print(get_chr_min_2("c"))