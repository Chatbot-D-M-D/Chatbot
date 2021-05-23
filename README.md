# Chatbot
Proiect LP2
Cum functioneaza un chatbot?
	Un chatbot nu e nimic mai mult decat un soft inteligent care poate comunica cu noi la fel ca un om.
  
Structura proiectului
Pasul 1 – Import de librarii si a datelor de care avem nevoie (Deaconu)
	Am facut un fisier Python in care am inceput codul cu toate uneltele de care avem nevoie.
	Am creat si un fisier cu extensia .json in care vom crea baza de date a bot-ului.
Pasul 2 – Preprocesarea datelor (Maria)
	Bot-ul inca nu poate intelege mai nimic, trebuie sa trecem cu el printr-o serie de preprocesare de date pentru a il ajuta. Tehnicile folosite de noi pentru asta sunt: “Tokenizing” si “Lemmatization”.
	Tokenizing = spargem propozitiile in cuvinte pentru a face bot ul sa inteleaga mai usor
	Lemmatization = convertim cuvintele in forma lemma pentru a reduce cuvintele canonice, adica ca exemplu cuvintele ca si: “playing, plays, played, etc” vor fi inlocuite cu “play”. 
	Scapam si de cuvintele care se repeta.
Si salvam / sortam clasele si cuvintele in doua fisiere numite wods si classes cu extensia .pkl (incriptat)
Pasul 3 – Crearea spatiului de antrenament pentru bot (TOTI 3)
	Pentru a realiza acest pas vom converti toate modelele de intrare in numere, adica folosim din nou tehnica Lemmatize pentru fiecare cuvant si facem o lista cu zerouri de aceeasi lungime cu numarul total de cuvinte. Setam valoarea 1 doar la indicii care contin cuvantul din modele. La fel vom face cu iesirea pe care o setam pe 1 la intrarea clasei de care apartine modelul.
Pasul 4 – Antrenarea lui (TOTI 3)
	Il vom antrena 200 de “ere” si salvam modelul intr-un fisier numit “chatbot_model.h5” (cu extensia fisierului h5), folosind Keras, si la sfarsitul acestei etape vom primi acuratetea bot-ului pentru fiecare era in parte. Acest pas este necesar de fiecare data cand schimbam ceva in baza lui de date.
Pasul 5 – Interactionarea cu bot-ul si crearea GUI-ului (interfata) (Darius)
	Modelul nostru este aproape gata de actiune, mai are nevoie doar de o interfata. Interfata este facuta cu Tkinter. Vom receptiona mesajul si vom efectua din nou o preprocesare inainte de a introduce mesajul propriu-zis de la utilizator. Pe urma modelul nostru v-a vedea la ce vrea utilizatorul sa se refere si v-a alege un raspuns aleator pentru unele intrebari, si prestabilit pentru altele.
Pasul 6 – Rularea programului ! 
