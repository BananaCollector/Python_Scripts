# Python_Scripts

Krótkie demo prostych skryptów Python:
- `src/example_calculator.py` — przykładowy kalkulator z dzieleniem i średnią
- `src/cli_demo.py` — prosty CLI do obliczania średniej z przekazanych liczb
- `src/text_tools.py` — narzędzia tekstowe: normalizacja spacji i zliczanie słów

## Wymagania

- Python 3.10+
- system Linux / macOS / Windows
- opcjonalnie: wirtualne środowisko `venv`

> W tej wersji repozytorium nie ma dodatkowych zależności poza standardową biblioteką Pythona.

## Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/BananaCollector/Python_Scripts.git
   cd Python_Scripts
   ```

2. Utwórz i aktywuj wirtualne środowisko:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

## Uruchamianie

### `src/cli_demo.py`

Uruchomienie CLI do obliczania średniej:
```bash
python -m src.cli_demo --numbers 1 2 3 4
```

### `src/example_calculator.py`

Skrypt uruchamiany interaktywnie:
```bash
python src/example_calculator.py
```

Przykładowa interakcja:
- wpisz `d` dla wartości domyślnych
- lub wpisz dwie liczby, np. `8 2`
- następnie wpisz listę liczb oddzielonych spacją, np. `5 7 10`

### `src/text_tools.py`

Uruchomienie narzędzia do zliczania słów:
```bash
python src/text_tools.py
```

Przykład:
- wpisz `d` dla przykładowego tekstu
- lub wpisz własny tekst, np. `Ala ma kota i Ala lubi kota`

## Przykłady

### Przykład 1 — `cli_demo`
```bash
python -m src.cli_demo --numbers 2 5 10
```

Wyjście:
```text
5.666666666666667
```

### Przykład 2 — `example_calculator.py`
```text
Enter two numbers to divide, separated by a space (or 'd' for default): d
Your division for 4 / 10: 0.4
Enter a list of numbers separated by spaces (or 'd' for default): d
Your average for [10, 5, 7, 4]: 6.5
```

### Przykład 3 — `text_tools.py`
```text
Enter string (or 'd' for default): d
{'ala': 2, 'have': 1, 'cat': 1, 'named': 1}
```

## Struktura repozytorium

- `src/`
  - `example_calculator.py`
  - `cli_demo.py`
  - `text_tools.py`
- `tests/`
- `README.md`


