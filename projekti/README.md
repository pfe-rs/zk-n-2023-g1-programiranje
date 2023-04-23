# ZK-N 2023 projekti (Grupa 1)
Ovde se čuvaju projekti pravljeni od strane polaznika u prvoj grupi sa zimskog kampa 2023. godine. Projekti su pravljeni u [Pygame](https://pygame.org/) i svaki polaznik je dobijao svoj projekat. Više detalja o svakom projektu pojedinačno možete pronaći u njihovim direktorijumima.

## Uputstvo za polaznike
Ukoliko se rešite da sami dodate fajlove u repozitorijum, to možete uraditi na sledeći način:

1. Instalirajte [Git](https://git-scm.com/) (ako ga već nemate)
2. Otvorite Git Bash u nekom direktorijumu
3. Klonirajte repozitorijum:
    1. Ukoliko nemate SSH ključ (ukoliko ne znate šta je SSH ključ najverovatnije ga nemate), pokrenite `git clone https://github.com/pfe-rs/zk-n-2023-g1-programiranje.git`
    2. Ukoliko imate SSH ključ, pokrenite `git clone git@github.com:pfe-rs/zk-n-2023-g1-programiranje.git`
4. Promenite trenutni direktorijum na repozitorijum: `cd zk-n-2023-g1-programiranje`
5. **Napravite svoju granu:** `git checkout -b [projekat]` (zamenite `[projekat]` sa nazivom svog projekta)
    - Ukoliko ne napravite svoju granu, dobićete grešku kako nemate dozvolu za guranje koda na tu granu
6. Dodajte fajlove svog projekta u direktorijum namenjen za projekat (po mogućstvu bez đubre fajlova poput `__pycache__`)
7. Napišite nešto o svom projektu u README.md fajlu koji se pre toga nalazio u tom direktorijumu, poput koje su dodatne biblioteke potrebne i koje su kontrole
8. Uradite *stage*: `git add .`
9. Uradite *commit*: `git commit -m "Ovde ide commit poruka."`
10. Sačekajte da dobijete mejl od GitHub sa pozivnicom u repozitorijum
11. Prihvatite poziv
12. Pokrenite `git push --set-upstream origin [projekat]` (gde je `[projekat]` isto kao ime vaše prethodno napravljene grane)
13. Osvežite stranicu sa repozitorijumom (sa koje verovatno čitate ovo uputstvo) i pritisnite dugme kako biste napravili *pull request*

Ukoliko se rešite da ipak ne dodajete sami fajlove u repozitorijum, možete ih podeliti preko alternativnih načina čija su uputstva prethodno poslata. Ukoliko želite da svoj projekat čuvate kao odvojen Git repozitorijum pod svojim nalogom, obavestite saradnike kako bi rukovodili ovom vanrednom situacijom.
