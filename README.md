# Atividade Banco

Database course assignment: a PostgreSQL schema for a university's students, courses and enrollments, plus a Python script that fills it with random data.

## Files

| File | Content |
|------|---------|
| `tabelas` | SQL that creates the `Aluno` (student), `Disciplina` (course) and `Matricula` (enrollment, with grades and attendance) tables, followed by a `drop table` statement that removes them (run only the part you need) |
| `popula_banco.py` | Generates 1864 random students (name, RA, birth date, mother's name, city/state, degree), the course list, and per-semester enrollments with random grades up to 2022, then inserts them with `psycopg2` |

## Usage

1. Create the tables in a PostgreSQL database by running the SQL in `tabelas`.
2. Install the dependencies: `pip install psycopg2-binary python-dotenv`.
3. `cp .env.example .env` and set `PG_USER`, `PG_PASSWORD`, `PG_HOST` (optional `PG_PORT`, `PG_DATABASE`). `.env` is gitignored.
4. Run `python3 popula_banco.py`.

The script opens a new connection for every insert, so it is slow on large data sets.
