# Secure Password Generator
 Generatore sicuro di password in Python

## Descrizione
Questo script Python genera password sicure di lunghezza variabile. Le password sono composte da caratteri alfanumerici e simboli speciali.

## Utilizzo
Per utilizzare lo script, eseguire il comando:
```python3 passwd_gen.py <lunghezza_password>```

## Esempio
Esempio di generazione di una password di lunghezza 12:
```python3 passwd_gen.py 12```

## Importa come modulo
Il modulo `passwd_gen` può essere importato in altri script Python. 

Per farlo, è sufficiente importare il modulo e chiamare la funzione `generate_password` specificando la lunghezza della password desiderata.

```
import passwd_gen as pg

lunghezza = 12  # O qualsiasi altro valore desiderato superiore a 8 e inferiore a 1000
password = password_generator.genera_password(lunghezza)
print(f"La password generata è: \033[1m{password}\033[0m")
```

## Responsabilità
L'autore dello script non è responsabile dell'utilizzo improprio dello stesso o della sicurezza delle password generate. 
