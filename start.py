from Main import Main
import os
from time import sleep
import sys


def mulai():
    #printout
    print('Program Hitung Honor Karyawan Kontrak\nPT. STAY COOL')
    input('Press Enter to start')
    print('installing requirements.txt')
    os.system('pip install -r requirements.txt || pip3 install -r requirements.txt') #install module yang diperlukan
    os.system('cls||clear') #clear terminal
    #printout pake animasi
    kata1 = "-------------------Program Hitung Honor Karyawan Kontrak-------------------\n"
    kata2 = "-------------------------------PT. STAY COOL-------------------------------\n"
    for char in kata1:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in kata2:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    #jalankan program
    Main()

#variasi
if len(sys.argv) > 1:

    if sys.argv[1] == 'Main':
        Main()
    elif sys.argv[1] == 'start' or sys.argv[1] == 'mulai' or sys.argv[1] == 'run':
        try:
            mulai()
        except KeyboardInterrupt:
            print('\nSee you!!')
            sys.exit()
        except IndexError :
            print('Completed but ada yang salah')
        except ValueError :
            print('Harus pake Integer')
    elif sys.argv[1] == 'credit' :
        print('\n')
        print('Muhamad Dafa Prasetya')
        print('Devi Alvandi')
        print('Dimas Ajie')
        print('Chairil Fajri')
        print('Arie Sutiawan')
        print('\n')

    else:
        for i in range(len(sys.argv[1:])):
            print(sys.argv[i+1],end=' ')
        print('\n')



