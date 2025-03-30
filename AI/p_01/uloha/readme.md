# 🧬 Game of Life – 1D

Tento projekt je jednoduchou implementací jednorozměrného celulárního automatu inspirovaného **Conwayovou Hrou života**. Simulace probíhá na jednom řádku buněk, kde každá buňka může být buď **živá**, nebo **mrtvá**. V průběhu několika iterací se stav každé buňky aktualizuje podle předem definovaných pravidel.

---

## 🔍 Přehled

### 🧱 Stavy buněk
- **MRTVÁ**: reprezentována znakem ` ` (mezera), zobrazuje se **modře**.
- **ŽIVÁ**: reprezentována znakem `█`, zobrazuje se **zeleně**.

### 🎨 Barevný výstup
Výstup je barevně odlišen pomocí ANSI escape kódů:
- 🟩 Zelená pro živé buňky
- ⬜ Šedá pro mrtvé buňky

### 🧮 Počítání sousedů
Používá se funkce `count_neighbors`, která počítá **4 okolní buňky** (2 vlevo, 2 vpravo). Buňka sama sebe nezapočítává. Pole není kruhové (necyklí se).

---

## ⚙️ Pravidla evoluce

- **Živá buňka (`█`)**:
  - Přežívá, pokud má **2 nebo 4 mrtvé** sousedy.
  - Jinak **umírá**.

- **Mrtvá buňka (` `)**:
  - Ožívá, pokud má **2 nebo 3 mrtvé** sousedy.
  - Jinak **zůstává mrtvá**.

> 💡 V tomto modelu se sousedé počítají jako **mrtví**, nikoliv živí – pravidla jsou tedy trochu obrácená, ale výsledek působí podobně.

---

## ▶️ Jak to funguje

1. **Inicializace**
   - Program definuje seznam testovacích případů – každý představuje jeden řádek buněk.

2. **Zobrazení řádku**
   - Pomocí funkce `print_row` se stav vykresluje s barevným rozlišením.

3. **Evoluce**
   - Funkce `update` aktualizuje buňky podle pravidel a vytváří nový stav.

4. **Iterace**
   - Funkce `main()` spouští evoluci na 20 kroků a zobrazuje každý krok.

---

## 🧪 Ukázka vstupu

```python
["█", " ", " ", " ", " ", "█", "█", " "]
