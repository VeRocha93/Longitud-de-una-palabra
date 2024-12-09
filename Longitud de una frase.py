contraseña = input("Ingresa una contraseña:")


#rango de cuatro a ocho letras:la palabra es correcta.
#menos de 4 letras : “Hacen falta letras. Solo tiene N letras” (siendo N el número de letras de la palabra).
#más de 8 letras: “Sobran letras. Tiene N letras” (siendo N el número de letras de la palabra).

if 4 <= len(contraseña) <= 8:
    print("Tu contraseña es correcta")
elif len(contraseña) < 4:
    print(f"Hacen falta letras, solo tiene {len(contraseña)}") 
elif len(contraseña) > 8:
    print(f"Sobran letras, tiene {len(contraseña)}")

