
def birthday_from_cnp(param_cnp):
    """
    Deduce date of birth from CNP
    :param param_cnp: string
    :return: birthday
    """
    code = param_cnp[0]
    year = int(param_cnp[1:3])
    month = int(param_cnp[3:5])
    day = int(param_cnp[5:7])

    if code in ['1', '2']:
        year += 1900
    elif code in ['3', '4']:
        year += 1800
    elif code in ['5', '6']:
        year += 2000

    birthday_as_tuple = (year, month, day)
    return birthday_as_tuple


def is_birthday_in_range(param_cnp):
    """
    Check if birthday is in a given range.
    :return: Birthday message
    """
    from datetime import date, timedelta
    today = date.today()
    year, month, day = birthday_from_cnp(param_cnp)
    birthday_as_date = date(year, month, day)

    start_range = today - timedelta(days=7)
    end_range = today + timedelta(days=7)

    start_md = (start_range.month, start_range.day)
    end_md = (end_range.month, end_range.day)
    birthday_md = (birthday_as_date.month, birthday_as_date.day)

    if start_md <= birthday_md <= end_md:
        return f"Happy Birthday!🎉🎉"
    else:
        return f"It's not your birthday yet, but you should get your wishes ready!🎁"


if __name__ == '__main__':
    param_cnp = '2961020000000'
    print(birthday_from_cnp(param_cnp))
    print(is_birthday_in_range(param_cnp))
