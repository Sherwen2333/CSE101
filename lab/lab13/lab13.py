# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 13


import re


# Part I
def street_addresses(addresses):
    a=r'(\d{1}(\d*)?\s[A-Z].*\s((Street)|(Road)|(Path)))'
    b=r'((\sApt\.\s[A-Z]))'
    res=[]
    for i in range(len(addresses)):
        if re.search(a,addresses[i]):
            line=re.sub(a,r'',addresses[i])
            if line is '':
                res.append(i)
            else:
                if re.search(b,line):
                    res.append(i)
    return res


# Part II
def package_destination(package_code, country_codes):
    res='error'
    pattern=r'\d{3}-\d{3}-[A-Z]\d'
    if re.search(pattern,package_code):
        z=package_code[0:3]
        if z in country_codes.keys():
            return country_codes[z]
    return res


# Part III
def business_card(contact_info):
    res='error'
    a=r'\*N(\s[A-Z].+)\s\*P\s(\d{3})(\d{3})(\d{4})\s\*T(\s[A-Z].+)'
    if (re.search(a,contact_info)):
        res=re.sub(a,r'Name:\1, Title:\5, Phone: (\2) \3-\4',contact_info)
    return res
