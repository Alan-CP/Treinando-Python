
Res = 'S'
while Res == 'S':
  number = int(input('Digite um número: '))
  if number % 2 == 0:
      print(f'O {number} é par!')
  else:
      print(f'O {number} é impar!')
  Res = input('Você quer continuar? (S/N)')
else:
    print('Fim do programa!')
