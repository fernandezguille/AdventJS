"""
The grinch 👹 has passed through Santa Claus's workshop! And what a mess he has made. He has changed the order of some packages, so shipments cannot be made.

Luckily, the elf Pheralb has detected the pattern the grinch followed to jumble them. He has written the rules that we must follow to reorder the packages. The instructions are as follows:

You will receive a string containing letters and parentheses.
Every time you find a pair of parentheses, you need to reverse the content within them.
If there are nested parentheses, solve the innermost ones first.
Return the resulting string with parentheses removed, but with the content correctly reversed.
"""
def fix_packages(packages: str) -> str:
    l_index: int = packages.rfind("\u0028")
    if l_index >= 0:
        r_index: int = packages.find("\u0029", l_index)
        return fix_packages(packages.replace(packages[l_index:r_index+1], packages[r_index-1:l_index:-1]))
    return packages

def fix_packages1(packages: str) -> str:
    while packages.count("\u0028") > 0:
        l_index: int = packages.rfind("\u0028")
        r_index: int = packages.find("\u0029", l_index)
        packages = packages.replace(packages[l_index:r_index+1], packages[r_index-1:l_index:-1])
    return packages


def fix_packages2(packages: str) -> str:
    index: int = packages.find("\u0028")
    if index >= 0:
        saw = 0
        highest = 0
        l_index = 0
        for index, char in enumerate(packages):
            if char == "\u0028":
                saw += 1
                if saw > highest:
                    highest: int = saw
                    l_index: int = index
            elif char == "\u0029":
                saw -= 1
        r_index: int = packages.find("\u0029", l_index)
        return fix_packages2(packages.replace(packages[l_index:r_index+1], packages[r_index-1:l_index:-1]))
    return packages

# Example
print(fix_packages ('ab(cd(ef))(gh)'))
print(fix_packages1('ab(cd(ef))(gh)'))
print(fix_packages2('ab(cd(ef))(gh)'))