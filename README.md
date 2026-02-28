# Bit.ly Search

Project ini dipisah ke struktur yang lebih standar agar mudah dikembangkan dan dirawat.

## Struktur

```
.
|-- bitly.py
|-- data/
|   `-- found.txt
|-- requirements.txt
|-- scripts/
|   |-- generator_demo.py
|   |-- progress_demo.py
|   `-- request_library_demo.py
|-- src/
|   `-- bitly_search/
|       |-- __init__.py
|       `-- main.py
`-- tests/
```

## Menjalankan

1. Buat virtual environment.
2. Install dependency:

```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:

```bash
python bitly.py
```

