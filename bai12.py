def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhap danh sach cacs so,cach nhau bang dua phay:")
numbers = list(map(int,input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi dao nguoc:",list_dao_nguoc)