# Tabu Search pro Obarvení Grafu

## 📌 Popis Algoritmu
Tabu Search (tabu vyhledávání) je heuristická optimalizační metoda, která se používá k řešení kombinatorických problémů, jako je **obarvování grafů**. Hlavním cílem je přiřadit vrcholům grafu barvy tak, aby žádné sousední vrcholy neměly stejnou barvu a zároveň se minimalizoval počet konfliktů.

Tento algoritmus implementuje **lokální prohledávání**, kde v každé iteraci vybíráme nejlepší možný tah, ale zároveň využíváme **tabu seznam**, který zabraňuje cyklení a zlepšuje průzkum prostoru řešení.

---

## 🔍 Princip Fungování
1. **Inicializace:**
   - Graf je nejprve obarven **greedy algoritmem** pro rychlé vytvoření počátečního řešení.

2. **Vyhodnocení konfliktů:**
   - Počítáme počet konfliktů, tedy kolik hran má vrcholy se stejnou barvou.

3. **Výběr vrcholu k úpravě:**
   - Zvolíme vrchol s nejvyšším počtem konfliktů.

4. **Hledání nejlepší změny barvy:**
   - Pro daný vrchol zkusíme všechny dostupné barvy a vybereme tu, která **nejvíce sníží konflikty**.
   - Pokud je tah **v tabu seznamu**, lze jej provést pouze pokud vede k novému nejlepšímu řešení.

5. **Aktualizace tabu seznamu:**
   - Přidáme tah do tabu seznamu na určitou dobu, aby se zabránilo okamžitému návratu ke starému řešení.

6. **Diversifikace:**
   - Pokud se algoritmus zasekne v lokálním minimu (po určitém počtu iterací bez zlepšení), náhodně upravíme některé barvy a restartujeme proces.

7. **Ukončení:**
   - Pokud nalezneme řešení bez konfliktů, nebo pokud dosáhneme maximálního počtu iterací.

---

## ⚙️ Použití Skriptu
### Spuštění algoritmu:
1. **Ujistěte se, že máte nainstalované potřebné knihovny:**
   ```bash
   pip install networkx matplotlib
   ```
2. **Spusťte skript:**
   ```bash
   python main.py
   ```
3. **Výstup obsahuje:**
   - Počet iterací
   - Počet konfliktů
   - Čas běhu
   - Obrázek s finálním obarvením grafu (`graph_coloring_35.png`)

---

## 📈 Výhody a Nevýhody
### ✅ Výhody:
✔ Dobře funguje pro **velké grafy**.
✔ Pomáhá **vyhnout se lokálním extrémům**.
✔ Možnost **diverzifikace**, pokud se řešení zasekne.

### ❌ Nevýhody:
✘ Není garantováno **optimální řešení**.
✘ **Výpočetně náročný** pro extrémně velké grafy.
✘ Nutnost **ladění parametrů**, jako je tabu délka či počet iterací.

---

## 🛠 Možnosti Vylepšení
🔹 Použití **hybridních metod**, například kombinace s genetickými algoritmy.
🔹 Dynamická úprava **tabu délky** podle aktuální situace.
🔹 Experimentování s jinými **heuristikami pro výběr barvy**.

---

## 📚 Další Čtení
- [Tabu Search na Wikipedii](https://en.wikipedia.org/wiki/Tabu_search)
- [Graph Coloring Problem](https://en.wikipedia.org/wiki/Graph_coloring)

---

📢 **Autor:** Tento kód implementuje Tabu Search pro obarvení grafů a je navržen tak, aby byl efektivní i pro složitější grafové instance.
