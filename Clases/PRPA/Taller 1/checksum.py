def checksum(binary_numbers):
  # Convertir los números binarios a enteros
  decimal_numbers = [int(num, 2) for num in binary_numbers]

  # Sumar los números enteros
  total = sum(decimal_numbers)

  # Convertir el resultado a binario
  binary_total = bin(total)

  # Calcular el complemento a dos
  ones_complement = ~int(binary_total, 2)
  twos_complement = ones_complement + 1

  # Convertir de nuevo a binario y eliminar el '0b' inicial
  return bin(twos_complement)[2:]

# Usando la función
numbers = ["0101100001101111", "0110110001100001", "0101101100101111"]
result = checksum(numbers)
print("Checksum:", result)