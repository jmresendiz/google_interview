# 🚀 Inicio Rápido - Google Interview Prep

## ✅ Repositorio Limpiado y Listo

El repositorio ha sido completamente reorganizado para tu preparación de entrevista técnica de Google en 12 días.

---

## 📁 Nueva Estructura

```
google_interview/
├── 📄 README.md                    # Información general del proyecto
├── 📄 QUICKSTART.md               # Esta guía de inicio rápido
├── 📄 pyproject.toml              # Dependencias Python simplificadas
│
├── 📂 docs/                       # Documentación y guías
│   ├── google_technical_interview.md  # Guía oficial de Google (formateada)
│   ├── study_plan.md                  # Plan de estudio de 12 días
│   └── checklist.md                   # Checklist de tópicos
│
├── 📂 practice/                   # Tu código de práctica
│   ├── algorithms/                # Implementaciones de algoritmos
│   ├── data_structures/           # Estructuras de datos
│   └── problems/                  # Soluciones a problemas
│
├── 📂 resources/                  # Recursos adicionales
│   └── notes/                     # Tus notas de estudio
│
├── 📂 scripts/                    # Scripts de utilidad (ambiente virtual)
└── 📂 .vscode/                    # Configuración de VS Code
```

---

## 🎯 Primeros Pasos (HOY - Día 1)

### 1. Instalar Dependencias
```bash
cd /home/jomi/repos/jmresendiz/google_interview
poetry install
```

### 2. Leer la Documentación
- [ ] **Leer**: `docs/google_technical_interview.md` (15-20 min)
- [ ] **Revisar**: `docs/study_plan.md` (10 min)
- [ ] **Abrir**: `docs/checklist.md` (marcar en otro tab para referencia)

### 3. Configurar Cuentas (si no lo has hecho)
- [ ] Crear cuenta en [LeetCode](https://leetcode.com/)
- [ ] Crear cuenta en [NeetCode](https://neetcode.io/)
- [ ] Explorar [Google Warmup](https://grow.google/certificates/interview-warmup/)

### 4. Empezar con el Plan (Día 1)

#### 📖 Lectura (1-1.5 horas)
- [ ] **Cracking the Coding Interview** - Capítulo VI (Big O)
- [ ] **Elements of Programming Interviews** - Capítulos 1-2

#### 💻 Práctica (2-3 horas)
Empezar con problemas de Arrays & Strings en NeetCode:

1. **Two Sum** (LeetCode #1) - EASY
   ```
   https://leetcode.com/problems/two-sum/
   ```

2. **Contains Duplicate** (LeetCode #217) - EASY
   ```
   https://leetcode.com/problems/contains-duplicate/
   ```

3. **Valid Anagram** (LeetCode #242) - EASY
   ```
   https://leetcode.com/problems/valid-anagram/
   ```

4. **Group Anagrams** (LeetCode #49) - MEDIUM
   ```
   https://leetcode.com/problems/group-anagrams/
   ```

#### 📝 Implementar (1-2 horas)
Crear estos archivos con tus implementaciones:
- [ ] `practice/algorithms/big_o_examples.py`
- [ ] `practice/data_structures/arrays.py`

#### ✍️ Tomar Notas (30 min)
- [ ] Crear `resources/notes/day1.md`
- [ ] Anotar conceptos de Big O
- [ ] Documentar errores cometidos
- [ ] Identificar patrones

---

## 📚 Recursos por Prioridad

### 🔴 Críticos (Usar Diariamente)
1. **NeetCode Roadmap** - Seguir orden de problemas
   - https://neetcode.io/roadmap

2. **Google Warmup** - 1 sesión diaria (15 min)
   - https://grow.google/certificates/interview-warmup/

3. **LeetCode** - 5-10 problemas diarios
   - Focus en Easy/Medium
   - Usar filtro de empresa "Google" cuando sea posible

### 🟡 Importantes (Consultar Según Necesidad)
4. **Cracking the Coding Interview** - 1 capítulo/día
5. **Elements of Programming Interviews in Python** - Secciones relevantes
6. **Big O Cheat Sheet** - https://www.bigocheatsheet.com/

### 🟢 Complementarios
7. **Fluent Python** - Lectura opcional sobre Python idioms
8. **Google Tech Dev Guide** - Recursos adicionales

---

## 🎤 Mock Interview - ¡IMPORTANTE!

**Agenda tu mock interview LO ANTES POSIBLE** (idealmente para el Día 10-11):

```
Email: gustavohar@google.com
Asunto: Mock Interview Request

Hola,

Me gustaría programar un mock interview de práctica.

Detalles:
- Tipo: Coding (Tech Only)
- Formato: Video via Google Meet
- Lenguaje de programación: Python
- Idioma de la entrevista: Inglés (default)
- Zona horaria: [TU ZONA HORARIA]
- Ciudad: [TU CIUDAD]
- Disponibilidad: [TUS HORARIOS PREFERIDOS]

Gracias,
[Tu nombre]
```

---

## 💡 Tips para Maximizar tu Preparación

### ⏰ Gestión del Tiempo
```
Por día (6-8 horas total):
├── 1-1.5h → Lectura teórica
├── 3-4h   → Resolución de problemas
├── 1-2h   → Implementaciones
├── 0.5-1h → Notas y revisión
└── 0.5h   → Google Warmup + descansos
```

### 🧠 Estrategia de Problemas
1. **Leer problema** → Entender requirements
2. **Intentar 30 min** → Pensar en solución
3. **Ver pista** (si estancado)
4. **Intentar 20 min más**
5. **Ver solución** → Entender el enfoque
6. **Re-implementar** → Sin mirar código
7. **Anotar patrón** → En tus notas

### 📝 Sistema de Notas
Crear un archivo por día:
```markdown
# Día 1 - Arrays y Big O

## Problemas Resueltos
- [x] Two Sum ✅ (25 min) - Hash table pattern
- [ ] Contains Duplicate ❌ (necesito revisar sets)

## Conceptos Aprendidos
- Big O: O(n) vs O(n²) en nested loops
- Hash tables reducen lookup de O(n) a O(1)

## Errores Comunes
- Olvidé manejar edge case: array vacío
- Confundí `in` vs `not in` en Python

## Para Revisar
- Repasar hash table collisions
- Practicar más dos punteros
```

---

## 🎯 Meta Diaria

Para cada día de tu plan:
- [ ] ✅ Completar lectura asignada
- [ ] ✅ Resolver N problemas (según día)
- [ ] ✅ Implementar estructuras/algoritmos clave
- [ ] ✅ Tomar notas de patrones y errores
- [ ] ✅ 1 sesión de Google Warmup
- [ ] ✅ Actualizar `docs/checklist.md`

---

## 📊 Tracking de Progreso

Actualizar diariamente en `docs/checklist.md`:
- Problemas resueltos (Easy/Medium/Hard)
- Horas de estudio
- Nivel de confianza por tópico (1-5)

---

## ⚠️ Recordatorios Importantes

### Durante la Práctica
1. **Pensar en voz alta** - Practica explicar tu razonamiento
2. **Sin IDE** - Usa Google Docs o editor simple ocasionalmente
3. **Verificar código manualmente** - No hay compilador en la entrevista
4. **Tiempo límite** - No más de 50 min por problema

### Antes de la Entrevista (Día 12)
- [ ] Probar cámara y micrófono
- [ ] Verificar internet estable
- [ ] Repasar 5 problemas favoritos
- [ ] Dormir 8 horas
- [ ] **NO estudiar** intensivamente el día de la entrevista

---

## 🆘 Si Te Atrasas

### Prioridades Absolutas (70% del tiempo):
1. ✅ Big O Notation
2. ✅ Arrays/Strings (Two pointers, Sliding window)
3. ✅ Hash Tables
4. ✅ Trees (Binary Trees, BST, Traversals)
5. ✅ Graphs (BFS, DFS básico)

### Opcional si el tiempo es corto:
- Advanced DP
- Dijkstra/A*
- AVL/Red-Black trees
- System Design (a menos que sea para senior role)

---

## 📞 Contactos Importantes

- **Recruiter de Google**: [Tu recruiter]
- **Mock Interview**: gustavohar@google.com
- **Emergencias técnicas**: Contactar a tu recruiter

---

## 🚦 Checklist de Inicio

Antes de empezar tu preparación HOY:

- [ ] Leer este documento completo
- [ ] Instalar dependencias (`poetry install`)
- [ ] Leer `docs/study_plan.md`
- [ ] Abrir `docs/checklist.md` en otro tab
- [ ] Crear cuenta LeetCode/NeetCode
- [ ] Agendar mock interview (email a gustavohar@google.com)
- [ ] Empezar con primer problema (Two Sum)
- [ ] Crear `resources/notes/day1.md`

---

## 🎉 ¡Estás Listo!

Tu repositorio está completamente preparado. Ahora es momento de ejecutar el plan.

**Recuerda**:
- Google busca **problem solvers**, no memorizadores
- La comunicación es **tan importante** como el código
- **Disfruta el proceso** - es una gran oportunidad de aprender

### 💪 ¡Mucha suerte en tu preparación!

---

## 📝 Siguiente Paso AHORA

1. Cerrar este archivo
2. Abrir `docs/study_plan.md`
3. Empezar con **Día 1** ⬇️

**Let's go! 🚀**
