<!DOCTYPE html>
<html>
<head>
    <!-- 
        Prosjekt: Autocoffee – Robot Demo
        Beskrivelse: En enkel demo for å aktivere en robotarm via betaling.
        Fil: index.html
    -->

    <!-- Tittel som vises i nettleserfanen -->
    <title>Autocoffe – Robot Demo</title>

    <!-- Koble til ekstern CSS for styling -->
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <!-- Hovedoverskrift på siden -->
    <h1>Autocoffee</h1>

    <!-- Bilde av robotarm -->
    <img src="/static/bilde.png" alt="Robot Arm" height="150" width="500">

    <!-- Instruksjonstekst for brukeren -->
    <p>Trykk knappen for å aktivere robotarmen for 18kr</p>

    <!-- 
        Betalingsskjema
        Sender telefonnummer via POST til /pay
        Knappen koblet til Vipps betaling
    -->
    <form method="post" action="/pay">
        <!-- Tekstfelt for å skrive inn telefonnummer -->
        <input type="text" name="phone" placeholder="Skriv inn telefonnummer" required>

        <!-- Submit-knapp for betaling via Vipps -->
        <button type="submit">Betal 18 kr med Vipps</button>
    </form>

    <!-- Slutt på body og HTML -->
</body>
</html>
