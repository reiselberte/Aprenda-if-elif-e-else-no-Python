#entendendo if, else e elif
#velocidade maxima permitida 80kh

#abaixo eu solicitei só nome e cpf, mas eu poderia pedir CNH, PLACA do veiculo etc...

print  ("Sistema Simulatorio de multa por excesso de velocidade")
nome = input(" Qual o seu nome completo: ")
cpf = input (" Qual o seu CPF: ")

velocidade = input ("Obrigado " + nome  +  " " "CPF:"+ cpf +  ", " + " Obrigado por confirmar seus dados, qual a velocidade que voce passou na VIA? ")

#Voce tera que converter str velocidade para int dessa forma abaixo, se nao o codigo vai dar erro
velocidade = int (velocidade)

#if é um "SE" ex: SE(if) velocidade for maior ">" que 81, print....
#elif é a continuação do if, mesma dinamica
#else é um "OU" e serve para finalizar. OU seja a ordem segue sempre em if, elif e else, beleza? vc poderá usar usar quantos elif quiser, vai de acordo com a situação que for criada.

if velocidade > 80:
    print ("Velocidade acima da media permitida, favor reduzir, fiscalizacao eletronica na via, EVITE ACIDENTES!!!")
elif velocidade < 60:
    print ("Favor aumentar velocidade, via de fluxo alto, evite acidentes")
else:
    print("Velocidade OK")
    
   
