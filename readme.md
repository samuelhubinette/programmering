
24 03 11
-------------
hej idag har jag satt upp loggboken och git

### lista med mål för Black Jack:

1. att man ska kunna få en score med två kort
2. att man ska kunna välja om man vill ta eller skippa ett kort
3. att dealerna ska stanna på 17 och över
4. att det ska stå om jag vunnit eller dealarn vunnit
5. att jag eller dealern förlorar om vi skrider över 21

24 04 18
-------------
Vad jag gjorde:
Jag började med att skapa funktionen deal_card(), som simulerar utdelningen av ett kort i spelet blackjack. Denna funktion returnerar ett kort slumpmässigt från en lista över möjliga kortvärden.

Vad koden betyder:
Funktionen deal_card() använder random.choice() för att välja ett kort från en lista innehållande alla kortvärden som används i blackjack: "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", och "A".

24 04 25
-------------
Idag skapade jag funktionen calculate_hand_value(), som beräknar värdet på en hand med kort. Detta inkluderar speciella regler för ess (A) som kan vara antingen 11 eller 1.

Funktionen calculate_hand_value() tar en lista med kort (hand) som argument och beräknar dess totala värde. Först används en dictionary för att mappa varje kort till dess värde. Funktionen summerar värdena på alla kort i handen. Om handen innehåller ess och totalvärdet överstiger 21, justeras värdet av ess från 11 till 1 tills värdet är 21 eller lägre.

Jag implementerade funktionen player_turn(), som hanterar spelarens val att ta ett kort eller stanna under spelets gång.

Funktionen player_turn() frågar spelaren om de vill ta ett kort ("T") eller stanna ("S"). Om spelaren väljer att ta ett kort, delas ett nytt kort ut och handen uppdateras. Handens värde beräknas och visas för spelaren. Om spelarens hand överstiger 21, förlorar spelaren direkt och spelet avslutas. Om spelaren väljer att stanna, avslutas deras tur.

24 05 16
-------------
Idag implementerade jagfunktionen dealer_turn(), som automatiserar dealerns tur enligt blackjack-regler.

Funktionen dealer_turn() fortsätter att dela ut kort till dealern tills deras handvärde är 17 eller högre. Detta är en standardregel i blackjack.

Jag skapade main()-funktionen som sätter samman spelets flöde: utdelning av initiala kort, spelarnas tur, dealerns tur och avgörande av vinnaren.

Funktionen main() börjar med att dela ut två kort till både spelaren och dealern. Spelarens hand och ett av dealerns kort visas. Spelarens tur hanteras av player_turn() och dealerns tur av dealer_turn(). Slutligen jämförs spelarens och dealerns händer för att avgöra vem som vinner.
