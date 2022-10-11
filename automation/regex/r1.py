import re
from re import match

text = """Lorem ipsum minimd32@domain1.com dolor sit amet, 054-668-4675 consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad  , quis nostrud exercitation ullamco@domain2.il 
        nisi ut aliquip ex 052-586-5632 ea commodo consequat. Duis aute irure dolor in 
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."""


def find_phone():
    phone_pattern = r"\d+-\d+-\d+"
    mo = re.findall(phone_pattern, text)
    print(f"findall() : {mo}")


def find_mail():
    mail_pattern = r'[\w\.-]+@[\w\.-]+\w{2,}'
    match = re.findall(mail_pattern, text)
    print(match)


def using_groups():
    # group is () and you can put any option for this group 
    #  ([\d]{3}-)? -> this group can be 0 or 1 time 
    # that contains exactly 3 digits and dash after  (452-, 856-)   
    regex = r"(\d+)-(\d+-\d+)"
    mo = re.search(regex, text)
    print(mo.group(0))
    print(mo.group(1))
    print(mo.group(2))


def option_to():
    text = "Batman is cool with batmobile"
    # match = re.findall(r"bat[\w]+", text.lower())
    match = re.search(r"bat(mobile|man|[\w]+)", text.lower())

    if (match != None):
        print(f"whole word : {match.group()}")


def all_():
    # same pattern for couple options
    #    (* -  0 or more times )
    #    (? -  0 or 1 times )
    #    (+ -  1 or more times )
    text = "this is the phone number 452-569-5214 of some person ."
    text2 = "this is the phone number 569-5214 of some person ."
    mo = re.search(r"([\d]+-)?\d{3}-\d{4}", text)
    mo2 = re.search(r"([\d]+-)?\d{3}-\d{4}", text2)
    print(mo.group())
    print(mo2.group())


if __name__ == "__main__":
    # find_phone()
    find_mail()
    # using_groups()
    # option_to()
    # all_()
