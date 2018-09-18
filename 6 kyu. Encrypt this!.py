# https://www.codewars.com/kata/encrypt-this/


def encrypt_this(text):
    """
    You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

    Your message is a string containing space separated words.
    You need to encrypt each word in the message using the following rules:
    The first letter needs to be converted to its ASCII code.
    The second letter needs to be switched with the last letter
    Keepin' it simple: There are no special characters in input.

    :param text: message
    :return: secret message
    """
    res = ''
    for x in text.split():
        if len(x) > 3:
            res += str(ord(x[0].encode())) + x[len(x) - 1] + x[2:len(x) - 1] + x[1] + ' '
        else:
            res += str(ord(x[0].encode())) + x[len(x):0:-1] + ' '
    return res.strip()


assert encrypt_this("") == ""
assert encrypt_this("A wise old owl lived in an oak") == "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
assert encrypt_this("The more he saw the less he spoke") == "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
assert encrypt_this("The less he spoke the more he heard") == "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
assert encrypt_this("Why can we not all be like that wise old bird") == "87yh 99na 119e 110to 97ll 98e 108eki 116tah " \
                                                                        "119esi 111dl 98dri"
assert encrypt_this("Thank you Piotr for all your help") == "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"
