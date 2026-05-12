# Sistema de pedidos refactorizado

PRECIOS = {
  "Laptop": 3000,
  "Mouse": 50,
  "Teclado": 100,
}

def calcular_total(producto, cantidad, cliente_vip=False):
  precio_base = PRECIOS.get(producto, 0) * cantidad
  if cliente_vip:
    precio_base *= 0.95
  return precio_base

def generar_factura(producto, cantidad, cliente_vip=False):
  total = calcular_total(producto, cantidad, cliente_vip)
  return {
    "producto": producto,
    "cantidad": cantidad,
    "total": total,
    "vip": cliente_vip
  }