import pytest
from pedidos_inicial import calcular_total as calcular_total_inicial
from pedidos_refactorizado import calcular_total as calcular_total_refactorizado

def test_totales_equivalentes():
  assert calcular_total_inicial("Laptop", 1) == calcular_total_refactorizado("Laptop", 1)
  assert calcular_total_inicial("Mouse", 2, cliente_vip=True) == calcular_total_refactorizado("Mouse", 2, cliente_vip=True)
  assert calcular_total_inicial("X", 5) == calcular_total_refactorizado("X", 5)