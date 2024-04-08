#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
str_var = "¡Hola mundo perfecto!"
num_var = 102030
lista_var = ["Hello", "Kaixo", "Hola", "Aloha"]
blogpost_var = True

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
index_var = str_var[:3]
print(index_var)

#Exercise 3: Use an index to grab the first element from your list.
first_var = lista_var[0]
print(first_var)

#Exercise 4: Create a new number variable that adds 10 to your original number
newnum_var = num_var + 10
print(newnum_var)


#Exercise 5: Use an index to get the last element in your list.
last_var = lista_var[-1]
print(last_var)


#Exercise 6: Use split to transform the following string into a list. names = 'harry,alex,susie,jared,gail,conner'
names = "harry, alex, susie, jared, gail, conner"
name_list = names.split()
print(name_list)


#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. 
#Create a new string that takes the uppercase word and the rest of the original string.
word = 1
result = str_var.split(' ')[word - 1]
print(result.upper() + str_var[5:])


#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
order_var = f"""Order {num_var} will arrive on schedule."""
print(order_var)

#Exercise 9: Print “hello world”.
print('Hello world.')


#Exercise 10: Además necesito que me crees una cadena que contenga la palabra "Hola". 
#Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. 
#Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".
str_var = str_var.replace('Hola', 'Adios')
print(str_var.replace('Hola', 'Adios'))



 

.




	names = 'harry,alex,susie,jared,gail,conner'








