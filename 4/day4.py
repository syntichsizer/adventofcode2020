import re

# i should learn regex and rewrite this asap

def validator(items):
    if 'byr' not in items:
        return False
    elif len(items['byr']) != 4 or int(items['byr'])<1920 or int(items['byr'])>2002:
        return False
    elif 'iyr' not in items:
        return False
    elif len(items['iyr']) != 4 or int(items['iyr'])<2010 or int(items['iyr'])>2020:
        return False
    elif 'eyr' not in items:
        return False
    elif len(items['eyr']) != 4 or int(items['eyr'])<2020 or int(items['eyr'])>2030:
        return False
    elif 'hgt' not in items:
        return False
    elif not (items['hgt'][-2:] == 'cm' and int(items['hgt'][:-2]) >= 150 and int(items['hgt'][:-2]) <= 193) and not (items['hgt'][-2:] == 'in' and int(items['hgt'][:-2]) >= 59 and int(items['hgt'][:-2]) <= 76):
        return False
    elif 'hcl' not in items:
        return False
    elif not re.match("#[a-f0-9]{6}",items['hcl']) or len(items['hcl']) != 7:
        return False
    elif 'ecl' not in items:
        return False
    elif items['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False
    elif 'ecl' not in items:
        return False
    elif 'pid' not in items:
        return False
    elif len(items['pid']) != 9 or not items['pid'].isnumeric():
        return False

    return True



passports = []

str = ''

for line in open(r'input.txt', 'r'):
    line = line[:-1]

    if len(line) > 0:
        str += line + " "
    else:
        passports.append(str[:-1])
        str = ''

passports.append(str)

counter = 0
counter2 = 0

for passport in passports:
    items_dict = {}

    passport = passport.split()

    for item in passport:
        item = item.split(':')
        items_dict[item[0]] = item[1]

    if len(items_dict) == 8 or (len(items_dict) == 7 and 'cid' not in items_dict):
        counter += 1

    if validator(items_dict):
        counter2 += 1

print(counter)
print(counter2)
