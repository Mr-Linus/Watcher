from faker import Faker


def main():
    f = Faker(locale='zh_CN')
    print("Generating information:")
    print("Name: "+f.name())
    print("Birthdate: "+f.profile()['birthdate'])
    print("E-mail: "+f.email())
    print("Phone: "+f.phone_number())
    print("Blood: "+f.profile()['blood_group'])
    print("Address: "+f.address())
    print("Website: "+f.uri())
    print("Username: "+f.user_name())
    print("Password: "+f.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
    print("Company: "+f.company())
    print("Job: "+f.job())
    print("Credit Card: \n"+f.credit_card_full(card_type=None), end='')
    print("ISBN: "+f.isbn13(separator="-"))
    print("IPv4: "+f.ipv4_public(network=False, address_class=None))
    print("IPv6: "+f.ipv6())
    print("UUID: "+f.uuid4())
    print("Win Token: "+f.windows_platform_token())
    print("Linux Token: "+f.linux_platform_token())
    print("Chrome Agent: "+f.chrome(version_from=13, version_to=63, build_from=800, build_to=899))
    print("Firefox Agent: "+f.firefox())


if __name__ == '__main__':
    main()