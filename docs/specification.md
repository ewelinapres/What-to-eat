# What-to-Eat – Specyfikacja projektu

**Nazwa projektu:** What-to-Eat  
**Typ projektu:** Aplikacja okienkowa 
**Status:** Specyfikacja wstępna

---

## 1. Opis projektu

**What-to-Eat** to aplikacja, której głównym celem jest ułatwienie użytkownikowi podjęcia decyzji dotyczącej wyboru posiłku.

Aplikacja skierowana jest do osób, które często zastanawiają się, co przygotować lub zjeść, ale nie mają konkretnego pomysłu. Zamiast samodzielnie przeglądać setki przepisów, użytkownik przechodzi przez krótki, dynamiczny quiz, odpowiadając na pytania dotyczące swoich aktualnych preferencji kulinarnych.

Na podstawie udzielonych odpowiedzi aplikacja analizuje preferencje użytkownika i proponuje dania najlepiej odpowiadające jego oczekiwaniom.

Kluczowym założeniem projektu jest **prostota** oraz **personalizacja rekomendacji**.

## 2. Cel projektu

Głównym celem projektu jest stworzenie intuicyjnej aplikacji, która pomaga użytkownikowi wybrać odpowiedni posiłek na podstawie jego bieżących preferencji.

### Cele szczegółowe

- Ograniczenie czasu potrzebnego na podjęcie decyzji dotyczącej wyboru posiłku.
- Stworzenie interaktywnego quizu dopasowującego pytania do wcześniejszych odpowiedzi.
- Opracowanie mechanizmu rekomendacji dań na podstawie preferencji użytkownika.
- Udostępnianie podstawowych informacji o rekomendowanym posiłku.
- Zapewnienie prostego i estetycznego interfejsu użytkownika.
- Umożliwienie ponownego losowania propozycji bez konieczności przechodzenia całego quizu.

## 3. Grupa docelowa

Aplikacja jest przeznaczona dla szerokiego grona użytkowników, w szczególności:

- Osób, które często nie wiedzą, co sobie przygotować do jedzenia.
- Osób chcących poznawać nowe dania i eksperymentować w kuchni.

## 4. Zakres projektu

Projekt obejmuje stworzenie aplikacji umożliwiającej przeprowadzenie quizu kulinarnego oraz wygenerowanie rekomendacji dań.

### Funkcjonalności podstawowe 

- Rozpoczęcie i przejście interaktywnego quizu.
- Dynamiczne wyświetlanie pytań zależnych od wcześniejszych odpowiedzi.
- Możliwość wyboru jednej lub kilku odpowiedzi, zależnie od pytania.
- Analiza preferencji na podstawie udzielonych odpowiedzi.
- Dopasowanie potraw z dostępnej bazy przepisów.
- Wyświetlenie rekomendowanego dania wraz z jego opisem.
- Możliwość wygenerowania alternatywnej propozycji.
- Możliwość powrotu do poprzedniego pytania.
- Możliwość rozpoczęcia quizu od nowa.

### Funkcjonalności dodatkowe (opcjonalne)

- Tworzenie kont użytkowników.
- Zapisywanie ulubionych potraw.
- Historia otrzymanych rekomendacji.
- Ocena zaproponowanych dań.
- Filtrowanie potraw według posiadanych składników.
- Tryb „Zaskocz mnie”, proponujący losowe danie.

## 5. Scenariusz działania aplikacji

### 5.1. Przebieg standardowy

1. Użytkownik otwiera stronę główną What-to-Eat.
2. Klika przycisk **„Rozpocznij quiz”**.
3. Aplikacja rozpoczyna quiz i wyświetla pierwsze pytanie.
4. Użytkownik wybiera odpowiedzi opisujące jego preferencje.
5. Kolejne pytania są dobierane na podstawie wcześniejszych odpowiedzi.
6. Po zakończeniu quizu aplikacja analizuje zebrane informacje.
7. System wybiera najlepiej dopasowane propozycje z bazy przepisów.
8. Użytkownik otrzymuje rekomendację potrawy.
9. Może zobaczyć szczegóły przepisu, wybrać inną propozycję lub rozpocząć quiz ponownie.

### 5.2. Przykładowy przebieg quizu

| Pytanie | Przykładowe odpowiedzi |
|---|---|
| Na jaki posiłek masz ochotę? | Śniadanie / Obiad / Kolacja / Przekąska |
| Wolisz coś słodkiego czy słonego? | Na słodko / Na słono / Bez znaczenia |
| Ile czasu chcesz poświęcić na przygotowanie? | Do 15 min / 15–30 min / Powyżej 30 min |
| Jak bardzo jesteś głodny? | Trochę / Średnio / Bardzo |
| Na jaki rodzaj potrawy masz ochotę? | Makaron / Kanapka / Sałatka / Danie na ciepło |
| Jakie warzywa lubisz? | Pomidory / Papryka / Brokuły / Szpinak / Inne |
| Czy chcesz zjeść mięso? | Tak / Nie / Bez znaczenia |
| Jaki poziom trudności preferujesz? | Łatwy / Średni / Dowolny |

Pytania nie muszą pojawiać się w stałej kolejności. Ich zestaw będzie zależał od wybranych wcześniej odpowiedzi.

### 5.3. Przykładowy wynik

Na podstawie odpowiedzi:

- Posiłek: obiad
- Smak: słony
- Czas przygotowania: do 30 minut
- Preferowane składniki: pomidory, szpinak
- Dieta: bezmięsna

Aplikacja może zaproponować:

**Makaron ze szpinakiem i suszonymi pomidorami**

## 6. Wymagania 

| ID | Wymaganie | Priorytet |
|---|---|---|
| F01 | System umożliwia rozpoczęcie quizu bez rejestracji. | Wysoki |
| F02 | System wyświetla pytania wraz z możliwymi odpowiedziami. | Wysoki |
| F03 | Użytkownik może wybierać odpowiedzi pojedyncze lub wielokrotne. | Wysoki |
| F04 | System dostosowuje kolejne pytania do wcześniejszych odpowiedzi. | Wysoki |
| F05 | System zapamiętuje odpowiedzi w ramach bieżącej sesji quizu. | Wysoki |
| F06 | Użytkownik może wrócić do poprzedniego pytania i zmienić odpowiedź. | Średni |
| F07 | System dobiera przepisy na podstawie odpowiedzi użytkownika. | Wysoki |
| F08 | System prezentuje rekomendowane danie wraz ze szczegółami. | Wysoki |
| F09 | Użytkownik może otrzymać alternatywną rekomendację. | Wysoki |
| F10 | Użytkownik może zresetować quiz i rozpocząć go ponownie. | Wysoki |
| F11 | System prezentuje postęp wypełniania quizu. | Średni |
| F12 | Użytkownik może wykluczyć składniki, których nie chce spożywać. | Wysoki |
| F13 | Użytkownik może zapisywać ulubione przepisy. | Niski |
| F14 | System może przechowywać historię rekomendacji. | Niski |

## 7. Mechanizm rekomendacji

Kluczowym elementem projektu będzie algorytm dopasowujący potrawy do odpowiedzi użytkownika.

W pierwszej wersji aplikacji planowane jest wykorzystanie **systemu rekomendacji opartego na regułach oraz punktowej ocenie dopasowania**.

### 7.1. Reprezentacja potraw

Każda potrawa w bazie danych będzie posiadała zestaw cech, takich jak:

- Typ posiłku.
- Rodzaj smaku (słodki/słony).
- Czas przygotowania.
- Poziom trudności.
- Składniki.
- Typ kuchni.
- Itp.

### 7.2. Filtrowanie

Na podstawie odpowiedzi użytkownika system odrzuci przepisy niespełniające najważniejszych wymagań.

Przykładowo, jeżeli użytkownik zadeklaruje dietę wegetariańską, potrawy zawierające mięso zostaną wykluczone.

Podobnie potraktowane zostaną składniki oznaczone przez użytkownika jako niedozwolone.

### 7.3. Ocena dopasowania

Pozostałe potrawy otrzymają punkty za zgodność z preferencjami użytkownika.

Przykładowa punktacja:

| Kryterium | Punkty |
|---|---:|
| Zgodny rodzaj posiłku | +5 |
| Zgodny preferowany smak | +4 |
| Zgodny czas przygotowania | +3 |
| Każdy preferowany składnik | +2 |
| Zgodny rodzaj potrawy | +3 |
| Zgodny poziom trudności | +1 |

Rekomendowane będą przepisy o najwyższej liczbie punktów.

W przypadku kilku przepisów o zbliżonym wyniku aplikacja może losować propozycję spośród najlepiej dopasowanych, zwiększając różnorodność rekomendacji.

### 7.4. Brak dopasowania

Jeśli żaden przepis nie spełni wszystkich wymagań, system wyświetli odpowiedni komunikat i zaproponuje użytkownikowi zmianę wybranych preferencji.
