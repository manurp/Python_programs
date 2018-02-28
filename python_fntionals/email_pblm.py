# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# Using Python 2
# import re
# lst = list()
# for i in range(int(raw_input())):
#     lst.append(raw_input())
# print sorted(list(filter(lambda x: re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',x),lst)))

import re


def fun(s):
    li_splitted = re.split('[@.]', s)
    if len(li_splitted) is not 3:
        return False
    usr_name = li_splitted[0]
    web_name = li_splitted[1]
    ext = li_splitted[2]
    usr_pattern = re.compile('[a-zA-Z0-9-_]+')
    res = usr_pattern.fullmatch(usr_name)
    if res is None:
        return False

    web_pattern = re.compile('[a-zA-Z0-9]+')
    res = web_pattern.fullmatch(web_name)
    if res is None:
        return False

    if len(ext) > 3:
        return False

    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
