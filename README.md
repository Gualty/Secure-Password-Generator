# Secure Password Generator
 Generatore sicuro di password in Python

## Descrizione
Questo script Python genera password sicure di lunghezza variabile e può essere integrato in altri progetti come modulo. 

## Requisiti della password
Le password generate rispettano i seguenti requisiti:
- Almeno 8 caratteri
- Lunghezza massima scelta dall'utente
- Almeno una lettera maiuscola
- Almeno una lettera minuscola
- Almeno un numero
- Almeno un carattere speciale
- Non deve contenere più di tre caratteri uguali consecutivi

## Utilizzo
Per utilizzare lo script, eseguire il comando:
```python3 secure_passwd_gen.py <lunghezza_password>```

## Esempio
Esempio di generazione di una password di lunghezza 12:
```python3 secure_passwd_gen.py 12```

## Importa come modulo
Il modulo `secure_passwd_gen` può essere importato in altri script Python. 

Per farlo, è sufficiente importare il modulo e chiamare la funzione `generate_password` specificando la lunghezza della password desiderata.

```
import secure_passwd_gen.py as spg

lunghezza = 12  # O qualsiasi altro valore desiderato superiore a 8 e inferiore a 1000
password = spg.genera_password(lunghezza)
print(f"La password generata è: \033[1m{password}\033[0m")
```

## Responsabilità
L'autore dello script non è responsabile dell'utilizzo improprio dello stesso o della sicurezza delle password generate. 
