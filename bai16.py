def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)  # Fixed function name hyphen to underscore
if result:
    print("Phan tu da duoc xoa tu Dictionary:", my_dict)  # Fixed variable name hyphen to underscore
else:
    print("Khong tim thay phan tu can xoa trong Dictionary")