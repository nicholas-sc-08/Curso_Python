
# O " sep='' " tem como função de modificar o "caractere de espaço"
# entre por exemplos as strings abaixo

print("Abc", "Def", sep="-");

#saída: Abc-Def

# Já o " end='' " tem como função de você adicionar algum conteudo no final
# da linha, também ele deixa o conteúdo do outro print na mesma linha,
# veja o exemplo abaixo:

print("Hello world", end="outro end");

#saída: Hello world outro end


print("Programação", "Essenciais", "em", "Python ", end="este é o commando end ", sep="_");

#Você consegue multiplicar strings colocando a string vezes um número int.

print(" Consigo multiplicar strings?!" * 2);

# saída: Consigo multiplicar strings?! Consigo multiplicar strings?!

print("2");
print(2);

# Posso separar por legibilidade o valor de dois milhões com o underline,
# porém o output sera tudo junto, sem o underline,

print(2000000);
print(2_000_000);
print(-2_000_000);

print(" Número octal:", 0o345);
print("Numero hexadecimal:" , 0x123);

# É possível você fazer potências com a palavra mágica "E", sendo 10 elevado a X,
# no caso, o exemplo que fiz seria a velocidade da luz, sendo 3 x 10 ^ 8,

# a base, que seria o valor antes do "E", pode ser um int ou um float
# o expoente, que seria o valor após o "E", pode ser somente um int

print(3E8);

# o output deste print é "300000000.0", sendo um um número float.

# outro exemplo é a famosa constante de plank, sendo o zero absoluto ela tem o
# valor de 6.62607 x 10 ^ -34. Isto no python pode ser escrito como

print(6.62607E-34);

# a saída sera: 6.62607e-34;

# outra maneira que podemos para obter um valor em potência seria escrever o
# resultado para obter o valor na forma de potência, seria desta maneira?

print(0.000000000000001);

# output: 1e-15
#escrito matemáticamente como: 1 ^ -15;


# True é maior que false

if True > False : print("Verdade")
