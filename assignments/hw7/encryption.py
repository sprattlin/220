def encode_better(message, key):
    empty_str = ''
    for i in range(len(message)):
        conv_mes = ord(message[i]) - 65
        conv_key = ord(key[i % len(key)]) - 65
        shift = (conv_mes + conv_key) % 58
        cipher = shift + 65
        cipher_conv = chr(cipher)
        empty_str += cipher_conv
    print(empty_str)
def encode(message, key):
    for i in range(len(message)):
        first_conv = ord(message[i])
        x = first_conv + int(key)
        convert_back = chr(x)
        print(convert_back, end="")