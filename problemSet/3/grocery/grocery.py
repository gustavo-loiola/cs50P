def main():
    set_list = get_items()
    org_list = organize(set_list)
    for item in org_list:
        print(org_list[item], item)


def get_items():
    list_items = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            return list_items

        if item in list_items:
            list_items[item] += 1
        else:
            list_items[item] = 1


def organize(d):
    d_org = {}
    fruits_list_org = sorted(list(d))  # its a copy organized
    for item in fruits_list_org:
        d_org[item] = d[item]

    return d_org


main()
