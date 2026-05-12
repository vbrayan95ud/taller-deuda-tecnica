## Código inicial con deuda (`pedidos_inicial.py`)
# Sistema de pedidos con deuda técnica

def calcular_total(producto, cantidad, cliente_vip=False):
  if producto == "Laptop":
    precio = cantidad * 3000
    if cliente_vip:
      precio = precio - (precio * 0.05)
    return precio
  elif producto == "Mouse":
    precio = cantidad * 50
    if cliente_vip:
      precio = precio - (precio * 0.05)
    return precio
  elif producto == "Teclado":
    precio = cantidad * 100
    if cliente_vip:
      precio = precio - (precio * 0.05)
    return precio
  else:
    return 0

def generar_factura(producto, cantidad, cliente_vip=False):
  total = calcular_total(producto, cantidad, cliente_vip)
  return f"Factura: {producto} x {cantidad} = ${total}"