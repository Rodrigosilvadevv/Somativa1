print(f"Iremos descobrir os 2 paises com maiores reservas de terras raras do mundo: ")

seu_nome = input(f"Digite seu nome:  ").upper()
peso1 = input(f"Digite o nome do seu país:  ").upper()
if peso1 == "brasil":
    print(f"Oi {seu_nome}, o nosso pais esta entre")
    print(F"nosso passaporte é aceito em 169 paises... lembre disso")
else:
         print("Dica, qual a maior economia da america latina?:  ")

peso2 = input(f"qual o pais esta se tornando a maior economia mundial?  ")

if peso2 == "china":
       print("isso mesmo, a china é o maior em processamento e producao seguido do nosso brasil")
else:
       print("Dica: a dica é que esse pais é a segunda em populacao, e tem bandeira red")

while True:
     comando =  input(f"Digite um cmd: about, add, quit:  ").strip().upper()

if comando == "ABOUT":
      print("Seu pais é Brasil e a 2º maior reserva")
      print("O primeiro em reserva é a china")
      print("o nosso passaporte é aceito em mais de 169 paises sem visto")

elif comando == "ADD":
            quantidade = int(input("Em quantos países entramos sem visto?  "))

            if quantidade < 1:
                print("O valor não pode ser zero ou negativo.")
            elif quantidade == 169:
                print("Você acertou!")
            else:
                print("São 169 países.")
       
                             
elif comando == "QUIT":
    print("Voce foi otimo tchau tchau!!!")

    '''
Atividade formativa 3, depois para entregar, mas esta na mão
feito por RODRIGO
'''