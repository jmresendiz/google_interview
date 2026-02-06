# 💻 Práctica de Código

Este directorio contiene implementaciones y soluciones a problemas de práctica.

## 📁 Estructura

```
practice/
├── algorithms/          # Implementaciones de algoritmos fundamentales
├── data_structures/    # Implementaciones de estructuras de datos
└── problems/           # Soluciones a problemas de LeetCode/HackerRank
```

## 🎯 Objetivo

Implementar desde cero las estructuras de datos y algoritmos más importantes para:
1. **Entender** profundamente cómo funcionan
2. **Practicar** escribir código limpio sin IDE
3. **Reforzar** conceptos para la entrevista

## 📝 Convenciones

### Naming
- Nombres de archivo: `snake_case.py`
- Clases: `PascalCase`
- Funciones: `snake_case`

### Comentarios
- Incluir complejidad de tiempo y espacio
- Explicar el enfoque/algoritmo usado
- Agregar ejemplos de uso

### Ejemplo

```python
def binary_search(arr: list[int], target: int) -> int:
    """
    Binary search implementation.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Sorted array of integers
        target: Value to search for

    Returns:
        Index of target if found, -1 otherwise

    Example:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## 🧪 Testing

Usar pytest para probar implementaciones:

```bash
# Test específico
pytest practice/algorithms/binary_search.py -v

# Test todo el directorio
pytest practice/ -v

# Con coverage
pytest practice/ --cov
```

## 📚 Recursos

- Ver [study_plan.md](../docs/study_plan.md) para saber qué implementar cada día
- Ver [checklist.md](../docs/checklist.md) para marcar progreso
