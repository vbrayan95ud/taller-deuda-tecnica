# Taller: Deuda Técnica en un Sistema de Pedidos

Este repositorio muestra cómo la deuda técnica afecta la evolución de un sistema.

## Objetivo
- Experimentar cómo las decisiones rápidas generan deuda técnica.
- Refactorizar para mejorar mantenibilidad y escalabilidad.
- Usar GitHub para documentar la evolución del proyecto.

## Escenario inicial

Una tienda online ha solicitado la creación de un sistema simplificado de gestión de pedidos con una lista inicial de 3 productos, para ser desarrollado en 30 minutos.

Se realiza un commit inicial con una lógica rápida y sin verificación de buenas prácticas debido a la restricción temporal de entrega establecida. El código inicial está lleno de duplicaciones, malas prácticas y ausencia de pruebas. La dinámica será extender el sistema bajo presión y luego refactorizarlo.

## Problemas del commit inicial con deuda técnica

1. Código duplicado para cada producto
2. Lógica de descuento repetida
3. No hay separación de responsabilidades (facturación y cálculo mezclados)
4. No hay pruebas unitarias

## Modificación del escenario inicial

Se realiza una refactorización del código para mejorar la lógica inicial y eliminar la deuda técnica

## Ventajas de la nueva lógica

1. Diccionario centralizado para precios
2. Lógica de descuento única
3. Factura como objeto estructurado (más fácil de entender)
4. código más limpio y mantenible
5. implementación de pruebas unitarias

## Actividad

La tienda ha eviado un requisito de último momento: 

"se debe modificar la lista inicial de productos para agregar los siguientes: 

* un monitor de de 27 pulgadas al cual se le aplicará un 10% de descuento para clientes VIP
* una barra de sonido a la cual se le aplicará un 8% de descuento para clientes VIP" 

**El cambio debe estar en ambiente productivo dentro de los siguientes 10 minutos.**

1. Haz un fork de este repositorio
2. implementa la solución al nuevo requisito en `pedidos_inicial.py`y observa cómo el sistema se complica.
3. ejecuta un commit a main para que los cambios se publiquen en producción.
4. abrir al menos un issue (ver ejemplo más abajo) en GitHub describiendo la deuda técnica encontrada.
5. implementar la misma funcionalidad del punto 2 en ``pedidos_refactorizado.py`` de la rama "manejo-deuda-tecnica".
6. ejecutar commit de la versión refactorizada.
7. crear un pull request (ver ejemplo más abajo) con la refactorización que soluciona el issue. El PR debe incluir una descripición clara de los cambios, la referencia al issue que cierra (``closes #x``) y evidencia de que las pruebas unitarias pasen
8. agregar un archivo .txt al repositorio respondiendo las siguientes preguntas:

    * ¿qué versión fue más fácil de extender, la inicial o la refactorizada y por qué?
    * ¿cómo se refleja la deuda técnica en el historial de commits?
    * ¿qué pasaría si el sistema creciera a 50 productos?
    * ¿de qué manera los issues y los PR ayudan a documentar la deuda técnica y a mantener un historial claro de decisiones? 


# Ejemplo de Issues

### Issue: Código duplicado en cálculo de precios
*   **Título:** "Duplicación de lógica en calcular_total"
*   **Descripción:** Actualmente la función `calcular_total` repite la lógica de descuento en cada producto. Esto genera deuda técnica porque dificulta la extensión del sistema.
*   **Sugerencia:** Centralizar la lógica de descuento en un solo lugar.
*   **Etiqueta:** `deuda técnica`, `refactorización`

### Issue: Factura poco estructurada
*   **Título:** "Factura generada como string plano"
*   **Descripción:** La función `generar_factura` devuelve un string, lo que limita la reutilización. Esto complica la integración con otros sistemas (ej. exportar a JSON).
*   **Sugerencia:** Devolver un objeto estructurado.
*   **Etiqueta:** `mejora`, `arquitectura`

---

# 🔀 Ejemplo de Pull Requests

### Pull Request: Refactorización de cálculo de precios
*   **Título:** "Refactorizar ``calcular_total`` para eliminar duplicación"
*   **Descripción:**
```bash    
- Se creó un diccionario centralizado de precios.
- Se unificó la lógica de descuento en una sola línea.
- Se agregaron pruebas unitarias para validar equivalencia con la versión anterior.
```
*   **Closes:** #1 (Issue de duplicación de lógica)


### Pull Request: Factura como objeto estructurado
*   **Título:** "Cambiar salida de `generar_factura` a objeto"
*   **Descripción:**
```bash
- La factura ahora devuelve un diccionario con producto, cantidad, total y estado VIP.
- Esto facilita la extensión y la integración con otros sistemas.
- Se actualizaron las pruebas unitarias.
```
*   **Closes:** #2 (Issue de factura poco estructurada)