## Starte backend-server

For å starte FastAPI-serveren med Uvicorn, åpne en Linux-terminal og kjør følgende kommandoer:

```bash
cd ~/robot_backend
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

Dette starter applikasjonen på en lokal webserver tilgjengelig på port 3000.

---

## Starte ngrok (utvikling)

Åpne en ny terminal og kjør:

```bash
ngrok http 3000
```

---

## Merk

Uvicorn og ngrok brukes sammen under utvikling for å:

* kjøre backend-applikasjonen på en lokal webserver
* opprette en sikker tunnel gjennom brannmur/NAT
* generere en offentlig URL som videresender ekstern trafikk til den lokale maskinen

Dette er nødvendig for å kunne motta webhooks fra Vipps API under testing.

---
Tilgang til nettsiden

https://fragmented-georgeanna-iatric.ngrok-free.dev/

Brukergrensesnittet er enkelt og intuitivt, og gjør det lett for brukeren å forstå bestillingsprosessen og navigere i løsningen.

![Autocoffee](Autocoffee.png)
