#dane = input('Wpisz imie, nazwisko i wiek, odzielajac gwiazdką').split('*')
#print('czesc',dane[0],'.Masz',dane[2],'lat')

#wyplata = int(input('Wpisz wyplate'))
#if wyplata > 5000:
 #    print('Gratulaje')
  #   print('wyslanie maila')
#print('kolejna instrukcja')

dane = input('Wpisz imie, wiek i wyplate').split()
#if int(dane[1]) >= 18:
 #   print("Dzien dobry",int(dane[0])
#if int(dane[1]) < 18:
 #   print('Czesc',int(dane[0])
#print('zaplłacisz podatek',dane[2]*0.15)

if int(dane[1]) >= 18:
    print('Dzien dobry',dane[0])
elif int(dane[1]) <18:
    print('Czesc',dane[0])
else:
    print('Sory, zly wiek')
print('zaplacisz',int(dane[2])*0.15)
