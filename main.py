hora = input('Digite a hora: ')

hora = float(hora)

if hora < 12:
    print('BOM DIA!!')
elif hora < 18:
    print('BOA TARDE!!')
else:
    print('BOA NOITE!!')
