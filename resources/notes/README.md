# 📝 Notas de Estudio

Este directorio es para guardar notas personales, patrones identificados, y conceptos importantes.

## 📋 Sugerencias de Archivos

```
notes/
├── patterns.md           # Patrones comunes de solución
├── mistakes.md          # Errores comunes y cómo evitarlos
├── time_complexity.md   # Notas sobre Big O
├── templates.md         # Templates de código reutilizables
├── day1.md             # Notas del día 1
├── day2.md             # Notas del día 2
└── ...
```

## 💡 Qué Anotar

### Patrones
- Técnicas recurrentes (two pointers, sliding window, etc.)
- Cuándo aplicar cada patrón
- Ejemplos de problemas

### Errores Comunes
- Bugs frecuentes (off-by-one, null checks, etc.)
- Casos edge que olvidaste
- Optimizaciones que pasaste por alto

### Templates
- Código base para BFS/DFS
- Template de Binary Search
- DP patterns (memoization, tabulation)
- Backtracking template

## 📊 Formato Sugerido

### patterns.md
```markdown
# Two Pointers

## Cuándo usar
- Array/string sorted
- Necesitas buscar pares
- Optimizar de O(n²) a O(n)

## Template
...código...

## Problemas
- Two Sum (sorted)
- Container With Most Water
- 3Sum
```

### mistakes.md
```markdown
# Día 1

## Problema: Two Sum
- ❌ Olvidé manejar caso de array vacío
- ❌ No consideré números negativos
- ✅ Aprendí: siempre preguntar sobre constraints

## Problema: Binary Search
- ❌ Error off-by-one en `mid = (left + right) // 2`
- ✅ Solución: usar `mid = left + (right - left) // 2`
```
