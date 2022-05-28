# this function formats input to mailing address format
def Address(f_name, street_num, s_name, city, prov, p_code, apt_n, apt):
    # correcting format for values
    p_full_name = f_name.upper()
    p_street_name = s_name.upper()
    p_city = city.upper()
    p_province = prov.upper()
    p_postal_code = p_code.upper()
    # apartment check
    if apt == "y":
        p_full_name = p_full_name
        p_street_address = apt_n + "-" + street_num + " " + p_street_name
        p_loc_info = p_city + " " + p_province + " " + p_postal_code
        address = p_full_name + "\n" + p_street_address + "\n" + p_loc_info
        return address
    # print formating
    p_full_name = p_full_name
    p_street_address = street_num + " " + p_street_name
    p_loc_info = p_city + " " + p_province + " " + p_postal_code
    address = p_full_name + "\n" + p_street_address + "\n" + p_loc_info
    return address


# this function gathers input and displays output
def main():
    # values
    apt_n = "0"
    apt = "N"
    f_name = input("Enter your full name: ")
    s_num = input("Enter your street number: ")
    apt = input("Do you live in an appartment? (y/n): ")

    if apt != "n":
        apt_n = input("What is your apartment_num: ")
        print("Enter your street name and", end="")
        s_name = input(" type (Main St., Flower Cres., etc.): ")
        city = input("Enter your city: ")
        print("Enter your province (as an ", end="")
        prov = input("abbreviation, 1.e. ON, AB, etc.): ")
        p_code = input("Enter your postal code: ")
        Address(f_name, s_num, s_name, city, prov, p_code, apt_n, apt)
        print(Address(f_name, s_num, s_name, city, prov, p_code, apt_n, apt))

    else:
        print("Enter your street name and", end="")
        s_name = input(" type (Main St., Flower Cres., etc.): ")
        city = input("Enter your city: ")
        print("Enter your province (as an ", end="")
        prov = input("abbreviation, 1.e. ON, AB, etc.): ")
        p_code = input("Enter your postal code: ")
        Address(f_name, s_num, s_name, city, prov, p_code, apt_n, apt)
        print(Address(f_name, s_num, s_name, city, prov, p_code, apt_n, apt))


if __name__ == "__main__":
    main()
