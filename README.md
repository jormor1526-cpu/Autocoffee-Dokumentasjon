# Automatic coffee machine 

## Prosjektbeskrivelse

Dette prosjektet er et digitalt bestillingssystem for kaffesmaking. Kunder kan legge inn bestilling via en nettside og gjennomføre betaling med Vipps. Når betalingen er bekreftet, mottar backend-serveren en webhook fra Vipps API og sender videre informasjon til en ESP32-enhet.

Kommunikasjonen mellom server og maskinvare skjer via MQTT ved bruk av Mosquitto.

---

## Systemarkitektur

1. Kunde legger inn bestilling via nettsiden.
2. Betaling gjennomføres gjennom Vipps.
3. Vipps sender betalingsbekreftelse via webhook til backend.
4. Backend behandler forespørselen.
5. Serveren publiserer en melding via MQTT.
6. ESP32 mottar meldingen og utfører tilhørende handling.

---

## Teknologi

* Frontend: HTML
* Backend: Python og FastAPI
* Server: Uvicorn
* Betalingsintegrasjon: Vipps API (webhooks)
* Meldingsprotokoll: MQTT (Mosquitto)
* Maskinvare: ESP32

---

## Prosjektstatus

| Oppgave                    | Status       |
| -------------------------- | ------------ |
| Nettside (HTML)            | Ferdig       |
| Backend-oppsett            | Ferdig       |
| Logo                       | Ferdig       |
| Bankkonto                  | Ferdig       |
| Vipps-konto og integrasjon | Pågående     |
| Testing                    | Ikke startet |


