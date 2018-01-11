from hashlib import sha1
from django.conf import settings as djsettings
from random import choice
from binascii import hexlify, unhexlify

from . import settings


def question():
    n1, n2 = choice(settings.NUMBERS), choice(settings.NUMBERS)

    if n2 > n1:
        # avoid negative answers
        n1, n2 = n2, n1

    question_str = "%s %s %s" % (n1, choice(settings.OPERATORS), n2)
    return question_str.encode('utf-8')


def captchaencode(question):
    """
    Given a mathematical question, eg '1 - 2 + 3', the question is hashed
    with the ``SECRET_KEY`` and the hex version of the question is appended.
    To the end user it looks like an extra long hex string,
    but it cryptographically ensures against any tampering.
    """
    question_hex = hexlify(question).decode()
    return sha1(djsettings.SECRET_KEY.encode() + question).hexdigest() + question_hex


def captchadecode(answer):
    """
    Returns the SHA1 answer key and the math question text.
    If the answer key passes, the question text is evaluated and compared to
    the user's answer.
    """
    return answer[:40], unhexlify(answer[40:])
