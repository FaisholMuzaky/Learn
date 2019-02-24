# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def awal():
    print("==========================================")
    print("Aplikasi Menghitung Nilai Akhir Mahasiswa")
    print("==========================================")

def hitung(N):
    for i in range(N):
        print("==========================================")
        mhs.append(input("Nama \t\t\t: "))
        if (mhs[i].isalpha() == False):
            print("Maaf Nama yang dimasukan salah")
            break
        elif (mhs[i].isalpha()):
            nim.append(input("Nim  \t\t\t: "))
            if (nim[i].isdigit() == False):
                print("Maaf Nim yang dimasukan salah")
                break
            else:
                kls.append(input("Kelas \t\t\t: "))
                t1.append(int(input("Nilai Tugas 1 \t: ")))
                t2.append(int(input("Nilai Tugas 2 \t: ")))
                uts.append(int(input("Nilai UTS \t\t: ")))
                uas.append(int(input("Nilai UAS \t\t: ")))
            
                total.append(t1[i]*0.25+t2[i]*0.3+uts[i]*0.25+uas[i]*0.2)
        
                if total[i] >= 80.01:
                    index.append("A")
                elif total[i] <= 80 and total[i] >= 70.01:
                    index.append("AB")
                elif total[i] <= 70 and total[i] >= 65.01:
                    index.append("B")
                elif total[i] <= 65 and total[i] >= 60.01:
                    index.append("BC")
                elif total[i] <= 60 and total[i] >= 50.01:
                    index.append("C")
                elif total[i] <= 50 and total[i] >= 40.01:
                    index.append("D")
                else:
                    index.append("E")
            
def tampil(N):
    print(" ")
    print("No\t","Nama\t\t","Nim\t\t","Kelas\t\t","total\t\t","Index")
    for j in range(N):
        print(j+1,".\t",mhs[j],"\t\t",nim[j],"\t\t",kls[j],"\t\t",total[j],"\t\t",index[j])

mhs=[]
nim=[]
kls=[]
t1=[]
t2=[]
uts=[]
uas=[]
total=[]
index=[]

awal()
N = int(input("Banyaknya Mahasiswa : "))
hitung(N)
tampil(N)