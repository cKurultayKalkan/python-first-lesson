import requests

from test_folder.test import sa

if __name__ == '__main__':
    sa('Ahmet, Gizem, Tuğba, Mehmet, Onur')

arr = [1, 2, 3, 4]
t = ["Merhaba Öğrenci" + str(a) for a in arr]

has_coffee = False
t = "Kahve var" if has_coffee else "Kahve Yok"
