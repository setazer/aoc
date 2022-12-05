from aocframework import AoCFramework
import re

def check_passport(passport):
    need_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl',  'ecl', 'pid']  # 'cid']
    missing = ' '.join([field for field in need_fields if field not in passport])
    field_dict = dict(map(lambda x: x.split(':'),passport.split()))
    all_fields = all(nf in field_dict for nf in need_fields)
    is_valid = (
        all_fields
        and (
            len(field_dict['byr']) == 4
            and (1920 <= int(field_dict['byr']) <= 2002)
        )
        and (
            len(field_dict['iyr']) == 4
            and (2010 <= int(field_dict['iyr']) <= 2020)
        )
        and (
            len(field_dict['eyr']) == 4
            and (2020 <= int(field_dict['eyr']) <= 2030)
        )
        and (
                (
                    field_dict['hgt'].endswith('cm')
                    and 150 <= int(field_dict['hgt'].replace('cm', '')) <= 193
                )
            or (
                    field_dict['hgt'].endswith('in')
                    and 59 <= int(field_dict['hgt'].replace('in', '')) <= 76
                )
            )
        and (
            re.search(r"#[0-9a-f]{6}", field_dict['hcl']) is not None
        )
        and (
            field_dict['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']
        )
        and field_dict['pid'].isdigit() and len(field_dict['pid']) == 9
    )
    return all_fields, is_valid


class DayPart1(AoCFramework):
    test_cases = (
        ('''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in''', 2),
    )
    known_result = 222

    def go(self):
        passports = self.puzzle_input.split('\n\n')
        return sum(check_passport(passport)[0] for passport in passports)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('', ),
    )
    known_result = 140

    def go(self):
        passports = self.puzzle_input.split('\n\n')
        return sum(check_passport(passport)[1] for passport in passports)


DayPart2()
