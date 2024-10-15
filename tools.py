import ipaddress


def valid_ip(address):
    try: 
        # socket.inet_aton(address)
        ip = ipaddress.ip_address(address)
        return True
    except:
        return False
    return False



# write set/list to a file
def write2file(items, fname):
    with open(fname, "w") as f:
        f.write("\n".join(items))



def is_valid_json(json_string):
    # print("JSON String:", json_string)
    try:
        json.loads(json_string)
        print("  Is valid?: True")
    except ValueError:
        print("  Is valid?: False")
        return False
    return True
