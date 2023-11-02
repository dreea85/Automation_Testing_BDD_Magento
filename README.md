Instrucțiuni de instalare
Instalarea Python și PIP

Asigurați-vă că aveți Python și PIP instalate pe sistemul dvs. Dacă nu, le puteți descărca și instala de la python.org.
După instalare verificați versiunile: python --version și pip --version.



Clonarea proiectului de pe GitHub

Deschideți terminalul și navigați la directorul în care doriți să clonați proiectul.
Executați comanda ”git clone https://github.com/dreea85/SoftwareTestingBoard.git”.

Instalarea dependențelor

Navigați în directorul proiectului clonat.
Rulați comanda pip install -r requirements.txt pentru a instala toate dependențele necesare, inclusiv Selenium și Behave.

Configurarea IDE

Deschideți proiectul în PyCharm sau orice alt IDE preferați.
Verificați setările de proiect pentru a vă asigura că sunt corecte (de exemplu, interpreter Python, setările de mediu).




Instalarea WebDriver

Descărcați WebDriver-ul corespunzător browserului pe care doriți să îl folosiți pentru testare (de exemplu, ChromeDriver pentru Google Chrome).
Plasați WebDriver într-un director recunoscut de PATH-ul sistemului sau specificați calea în scripturile de test.

Instrucțiuni de rulare
Deschiderea terminalului/liniei de comandă

Navigați în directorul rădăcină al proiectului clonat.
Rularea testelor

Executați comanda behave pentru a începe rularea testelor BDD.


Verificarea raportului

După finalizarea testelor, verificați raportul HTML generat pentru rezultate.

Analiza rezultatelor

Testele care au trecut sunt semnalate cu verde.
Testele care nu au trecut sunt semnalate cu roșu, iar în terminal sunt marcate cu ”failed”.


