print("Introduce el precio con dos decimales tras un punto")
precio = str(input())
print(precio[:precio.find(".")] + " euros con " + precio[precio.find(".")+1:] + " céntimos ")