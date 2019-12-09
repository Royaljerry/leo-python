#!/usr/bin/env python3

adatok = []
kint = []
autók = {}
rszkm={}
ember = []
legnagyobb_távolság = 0

#task 1
with open("4_Ceges_autok/autok.txt") as ff:
    for line in ff:
        line = line.strip()
        # print (line)
        if not line: 
            continue
        nap,óópp,rsz,szem,km,irány= line.split()
        km = int(km)
        adatok.append( (nap,óópp,rsz,szem,km,irány) )

#task 2
        if (irány == '0'):
            last_rent_id = rsz
            last_rent_day = nap
#task 4
        if (irány == '0'):
            kint.append(rsz)
        else: 
            kint.remove(rsz)
#task 5
        if (rsz not in autók):
            autók[rsz]=[km,km, str]
        else: 
            autók[rsz][1] = km 
#task 6
        if (rsz not in rszkm):
            rszkm[rsz] = km
        elif (irány == '1'):
            táv = km-rszkm[rsz]
            if (táv > legnagyobb_távolság):
                legnagyobb_távolság = táv
                ember = szem
            rszkm[rsz] = km

task_5 =''
for rsz in autók:
    autók[rsz][2] = autók[rsz][1]-autók[rsz][0]
    task_5 += rsz + ' ' + str(autók[rsz][2]) +'\n'




print('2. feladat:\n' + last_rent_day + '. nap rendszám: ' +last_rent_id)
#task 3
print('3. feladat:')
user_input = input('Nap: ')
print('Forgalom a(z) '+ user_input+'. napon:')
for item in adatok:
    #print (item)
    if user_input == item[0]:
        print(item[1] +' '+ item[2] + ' '+ item[3]+ ' ' + item[5])


print('4. feladat:\nA hónap végén ' + str(len(kint))+ ' autót nem hoztak vissza.')
print('5. feladat:\n' + task_5)
print('6. feladat:\nLeghosszabb út: '+ str(legnagyobb_távolság)+' km, személy: ' + ember)

#task 7
print("7. feladat")
rendszám= input("Rendszám: ").strip().upper()
fájlnév=f"{rendszám}_menetlevel.txt"

with open(fájlnév,"w") as ff:
    
    for nap,óópp,rsz,szem,kmóra,irány in adatok:
        if rendszám==rsz:
            if irány=='0':
                ff.write(f"{szem}\t{nap}. {óópp}\t{kmóra} km")
            else:
                ff.write(f"\t{nap}. {óópp}\t{kmóra} km\n")

print("Menetlevél kész.")

            