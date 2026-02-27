<!DOCTYPE html>
<html>
<head>
    <title>Autocoffee – Robot Demo</title>
    <!-- Link til CSS-fil som styrer styling -->
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <!-- Hovedoverskrift -->
    <h1>Autocoffee</h1>

    <!-- Bilde av robotarmen -->
    <img src="image/Autocoffee.png" alt="Robot Arm" height="150" width="500">

    <!-- Instruksjonstekst -->
    <p>Trykk knappen for å aktivere robotarmen for 18kr</p>

    <!-- Betalingsskjema med Vipps -->
    <form method="post" action="/pay">
        <!-- Inputfelt for telefonnummer -->
        <input type="text" name="phone" placeholder="Skriv inn telefonnummer" required>
        <!-- Submit-knapp -->
        <button type="submit">Betal 18 kr med Vipps</button>
    </form>
</body>
</html>
