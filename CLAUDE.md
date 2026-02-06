# CLAUDE.md - Google Technical Interview Preparation

Este repositorio es para preparación de **entrevista técnica de Google** en **12 días**.

---

## Propósito del Proyecto

Preparación intensiva para entrevista técnica de Google con:
- Plan de estudio estructurado de 12 días
- Práctica de problemas en NeetCode y LeetCode
- Implementaciones de algoritmos y estructuras de datos
- Seguimiento de progreso con checklists

**Fecha de inicio**: 6 de Febrero, 2026
**Entrevista estimada**: ~18 de Febrero, 2026

---

## Estructura del Proyecto

```
google_interview/
├── docs/                           # Documentación
│   ├── study_plan.md              # Plan de 12 días (PRINCIPAL)
│   ├── checklist.md               # Checklist de progreso
│   ├── libros_capitulos.md        # Capítulos a leer
│   ├── plataformas_recomendadas.md # Guía de plataformas
│   ├── google_warmup_guia.md      # Guía de Google Warmup
│   └── google_technical_interview.md # Guía oficial de Google
│
├── practice/                      # Código de práctica
│   ├── algorithms/                # Implementaciones de algoritmos
│   ├── data_structures/           # Estructuras de datos
│   └── problems/                  # Soluciones a problemas
│
└── resources/notes/               # Notas de estudio
```

---

## Documentos Clave

### 📖 Documentación Principal

1. **`docs/study_plan.md`** ⭐
   - Plan detallado de 12 días
   - Qué hacer cada día (teoría + práctica)
   - Plataformas a usar por fase

2. **`docs/checklist.md`**
   - Checklist de tópicos técnicos
   - Lecturas obligatorias (Cracking Interview, Elements)
   - Tracking de progreso

3. **`docs/libros_capitulos.md`**
   - Capítulos obligatorios de libros
   - Plan de lectura por día
   - Priorización (Must/Should/Nice)

4. **`docs/plataformas_recomendadas.md`**
   - NeetCode (Días 1-6, gratis)
   - LeetCode Premium (Días 7-11, $35)
   - Google Warmup (Diario, gratis)

5. **`docs/google_warmup_guia.md`**
   - Qué es Google Warmup
   - Cómo usarlo diariamente (15-20 min)
   - Practica "pensar en voz alta"

6. **`docs/google_technical_interview.md`**
   - Guía oficial de Google
   - Expectativas de la entrevista
   - Tips de comunicación

---

## Estrategia de Preparación

### Fases del Estudio

**Fase 1 (Días 1-6): NeetCode**
- Construir fundamentos
- Seguir NeetCode Roadmap
- 60-70 problemas (Easy y Medium)
- Focus en patrones

**Fase 2 (Días 7-11): LeetCode Premium**
- Problemas específicos de Google
- Filtrar por company tag
- 40-50 problemas (Medium)
- Simular presión real

**Durante Todo el Periodo:**
- Google Warmup: 1 sesión diaria (15-20 min)
- Lectura: ~2 horas/día (Cracking Interview, Elements)
- Notas: Documentar patrones y errores

### Meta Total
- **100-120 problemas** resueltos
- **15 capítulos** de libros leídos
- **12 sesiones** de Google Warmup
- **1 mock interview** con Googler

---

## Recursos de Estudio

### Libros (Capítulos Obligatorios)

**Cracking the Coding Interview (6th Ed):**
- Cap VI: Big O
- Cap I: Arrays and Strings
- Cap II: Linked Lists
- Cap III: Stacks and Queues
- Cap IV: Trees and Graphs
- Cap VIII: Recursion and Dynamic Programming
- Cap X: Sorting and Searching

**Elements of Programming Interviews in Python:**
- Cap 5: Arrays
- Cap 6: Strings
- Cap 7: Linked Lists
- Cap 8: Stacks and Queues
- Cap 9: Binary Trees
- Cap 12: Hash Tables
- Cap 15: Recursion
- Cap 16: Dynamic Programming

### Plataformas de Práctica

1. **NeetCode** (Días 1-6)
   - URL: https://neetcode.io/roadmap
   - Costo: Gratis
   - Usar: Videos explicativos + roadmap

2. **LeetCode Premium** (Días 7-11)
   - URL: https://leetcode.com
   - Costo: $35/mes (1 mes)
   - Filtrar: Company=Google

3. **Google Warmup** (Diario)
   - URL: https://grow.google/certificates/interview-warmup/
   - Costo: Gratis
   - Usar: 15-20 min/día para comunicación

---

## Tópicos Técnicos Clave

### Prioridad MUST (70% del tiempo)
1. Big O Notation
2. Arrays & Strings (Two Pointers, Sliding Window)
3. Hash Tables
4. Trees (Binary Trees, BST, Traversals)
5. Graphs (BFS, DFS)

### Prioridad SHOULD (20% del tiempo)
6. Sorting algorithms (QuickSort, MergeSort)
7. Recursion basics
8. Dynamic Programming (patrones simples)

### Prioridad NICE (10% del tiempo)
9. Advanced DP
10. Dijkstra/A*
11. Advanced tree structures

---

## Convenciones del Proyecto

### Archivos de Práctica

**Naming:**
- `snake_case.py` para archivos
- `PascalCase` para clases
- `snake_case` para funciones

**Estructura de archivos:**
```python
"""
Problem: [Nombre del problema]
Difficulty: Easy/Medium/Hard
Source: NeetCode/LeetCode #[número]
Company: Google

Time Complexity: O(?)
Space Complexity: O(?)

Pattern: [Two Pointers/Hash Table/BFS/etc]
"""

def solution(input):
    """
    Brief description of approach.

    Args:
        input: Description

    Returns:
        Description

    Example:
        >>> solution([1, 2, 3])
        6
    """
    # Implementation
    pass


# Tests
if __name__ == "__main__":
    assert solution([1, 2, 3]) == 6
    print("All tests passed!")
```

### Notas Diarias

Crear en `resources/notes/dayX.md`:

```markdown
# Día X - [Tema]

## Problemas Resueltos
- [x] Problema 1 (25 min) ✅
- [x] Problema 2 (45 min) - Necesité video
- [ ] Problema 3 (pendiente)

## Patrones Aprendidos
1. **[Patrón]**: Descripción
   - Cuándo usar
   - Ejemplo de código

## Errores Comunes
- Error que cometí
- Cómo evitarlo

## Para Revisar
- Tópicos que necesito reforzar
```

---

## Tracking de Progreso

### Actualizar Diariamente

**En `docs/checklist.md`:**
- Marcar tópicos completados
- Marcar libros leídos
- Actualizar contador de problemas

**En `resources/notes/`:**
- Crear archivo por día
- Documentar patrones
- Anotar errores comunes

---

## Comandos Útiles

### Setup Inicial
```bash
# Ya configurado, solo si necesitas reinstalar
poetry install
```

### Durante Práctica
```bash
# Ejecutar un problema
python practice/problems/two_sum.py

# Ejecutar tests
pytest practice/problems/two_sum.py -v

# Usar IPython para experimentar
ipython
```

### Formateo (Opcional)
```bash
# Formatear código
black practice/

# Linter
ruff practice/
```

---

## Guía para Claude

### Cuando el Usuario Pide Ayuda

**Para Resolver Problemas:**
1. NO dar la solución completa de inmediato
2. Dar pistas: "¿Has considerado usar un hash table?"
3. Si insiste, dar pseudocódigo primero
4. Solo dar código si explícitamente lo pide

**Para Explicar Conceptos:**
1. Explicar con ejemplos simples
2. Incluir análisis de complejidad (Big O)
3. Mencionar casos edge
4. Relacionar con problemas similares

**Para Implementaciones:**
1. Incluir docstring con complejidad
2. Agregar ejemplos en docstring
3. Incluir tests básicos
4. Comentar partes no obvias

**Para Revisar Código:**
1. Verificar complejidad de tiempo/espacio
2. Identificar casos edge no cubiertos
3. Sugerir optimizaciones
4. Verificar estilo Python (pythonic)

### Formato de Respuestas

**Para problemas de código:**
```python
"""
Time: O(n)
Space: O(1)

Approach:
1. Paso 1
2. Paso 2
3. Paso 3

Edge cases:
- Array vacío
- Un solo elemento
- Duplicados
"""

def solution(arr):
    # Implementation
    pass
```

**Para explicaciones:**
- Empezar con analogía simple
- Mostrar ejemplo visual/diagrama (ASCII art)
- Dar complejidad
- Mencionar cuándo usar

---

## Mock Interview

**Contacto:** gustavohar@google.com
**Tipo:** Coding (Tech Only)
**Cuándo:** Día 10-11 (Feb 15-16)
**Formato:** Google Meet

**Preparación:**
- Agendar con 1 semana de anticipación
- Especificar: Python como lenguaje
- Practicar "pensar en voz alta"

---

## Expectativas de Google

### Comunicación
- ✅ Pensar en voz alta
- ✅ Hacer preguntas clarificadoras
- ✅ Declarar suposiciones
- ✅ Escuchar pistas del entrevistador

### Resolución de Problemas
1. Definir y enmarcar el problema
2. Describir enfoque antes de codificar
3. Evitar fuerza bruta, optimizar
4. Explorar múltiples soluciones
5. Probar código manualmente
6. Código de calidad (limpio, eficiente)

### Plataforma
- Google Docs (sin IDE ni compilador)
- Verificación manual de código
- Entrevista en inglés

---

## Estado Actual del Proyecto

### Documentación Completa ✅
- [x] Plan de 12 días
- [x] Checklist de tópicos
- [x] Capítulos de libros identificados
- [x] Guía de plataformas
- [x] Guía de Google Warmup

### Siguiente Paso
- [ ] Empezar Día 1: NeetCode Arrays & Hashing
- [ ] Resolver primeros 5-7 problemas
- [ ] Primera sesión de Google Warmup
- [ ] Crear resources/notes/day1.md

---

## Tips para Claude al Ayudar

1. **Referirse siempre a la documentación:**
   - "Según tu `study_plan.md`, hoy deberías..."
   - "En tu `checklist.md` puedes marcar..."

2. **Recordar el timeline:**
   - Solo 12 días disponibles
   - Priorizar lo importante
   - No profundizar en temas "Nice to have"

3. **Enfatizar práctica sobre teoría:**
   - 60% resolver problemas
   - 30% lectura teórica
   - 10% notas y revisión

4. **Mantener motivación:**
   - Celebrar problemas resueltos
   - Recordar que Google valora el proceso, no la perfección
   - Es normal tardar en problemas Medium

5. **Usar recursos existentes:**
   - Videos de NeetCode
   - Discusiones de LeetCode
   - No reinventar la rueda

---

## Recursos Externos

- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode](https://leetcode.com/)
- [Google Warmup](https://grow.google/certificates/interview-warmup/)
- [Cracking the Coding Interview](https://www.crackingthecodinginterview.com/)
- [Elements of Programming Interviews](https://elementsofprogramminginterviews.com/)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [VisuAlgo](https://visualgo.net/) - Visualizar algoritmos

---

## Contactos Importantes

- **Recruiter de Google:** [Tu recruiter]
- **Mock Interview:** gustavohar@google.com
- **Emergencias:** Contactar recruiter

---

## Notas Finales

Este es un **proyecto de preparación intensiva**. El objetivo NO es completar todo perfectamente, sino:

1. Entender patrones fundamentales
2. Practicar comunicación (pensar en voz alta)
3. Resolver 100+ problemas
4. Ganar confianza

**Recuerda:** Google busca problem solvers, no memorizadores. Focus en entender el PROCESO, no en memorizar soluciones.

---

**Última actualización:** 6 de Febrero, 2026
**Estado:** En preparación activa (Día 1)
