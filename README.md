# Job Board API

REST API za pretragu i upravljanje oglasima za posao, izgrađen sa FastAPI i SQLite.

## Tech Stack

- **Python** + **FastAPI**
- **SQLAlchemy** ORM
- **SQLite** (development) / **PostgreSQL** (production)
- **JWT** autentifikacija
- **Docker** (coming soon)

## Funkcionalnosti

- CRUD operacije za oglase
- Pretraga oglasa po tech stacku i lokaciji
- Registracija i login korisnika
- JWT zaštićeni endpointi
- Automatska Swagger dokumentacija

## Pokretanje

### 1. Kloniraj repozitorijum
git clone https://github.com/Lanmimilanmmm/job-board-api

### 2. Instaliraj zavisnosti
pip install -r requirements.txt

### 3. Pokreni server
uvicorn main:app --reload

### 4. Otvori dokumentaciju
http://localhost:8000/docs

## API Endpointi

| Method | Endpoint | Opis | Auth |
|--------|----------|------|------|
| GET | /jobs/ | Lista svih oglasa | ❌ |
| GET | /jobs/?tech=Python | Pretraga po stacku | ❌ |
| GET | /jobs/{id} | Jedan oglas | ❌ |
| POST | /jobs/ | Dodaj oglas | ✅ |
| PUT | /jobs/{id} | Izmeni oglas | ❌ |
| DELETE | /jobs/{id} | Obriši oglas | ❌ |
| POST | /auth/register | Registracija | ❌ |
| POST | /auth/login | Login → JWT token | ❌ |