# Software per generare password sicure rispettando i criteri di sicurezza più avanzati
# Requisiti sicurezza password:
# - Almeno 8 caratteri
# - Lunghezza massima scelta dall'utente
# - Almeno una lettera maiuscola
# - Almeno una lettera minuscola
# - Almeno un numero
# - Almeno un carattere speciale
# - Non deve contenere più di tre caratteri uguali consecutivi
# Versione 1.0
# Sviluppato da Gualtiero @Gualty https://github.com/Gualty

import random
import string
import sys

# Costanti
LUN_MIN_PASSWD = 8 # Lunghezza minima della password
LUN_MAX_PASSWD = 1000 # Lunghezza massima della password

def genera_password(lung_passwd):
    """
    Genera una password sicura rispettando i criteri di sicurezza specificati.

    Args:
        lung_passwd (int): La lunghezza della password da generare.

    Returns:
        str: La password generata che soddisfa i criteri di sicurezza.
    """
    caratteri_speciali = "!@#%&/()=?"

    while True:
        # Assicurati che la password contenga almeno un carattere di ciascun tipo richiesto
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(caratteri_speciali)
        ]

        # Riempie il resto della password con caratteri casuali
        password += random.choices(string.ascii_letters + string.digits + caratteri_speciali, k=lung_passwd - 4)

        # Mescola la lista per evitare che i primi quattro caratteri siano sempre in un ordine fisso
        random.shuffle(password)

        # Converti la lista in stringa
        password = ''.join(password)

        # Verifica se la password soddisfa i criteri (niente caratteri uguali consecutivi)
        if not contiene_caratteri_uguali_consecutivi(password):
            break

    return password

def contiene_caratteri_uguali_consecutivi(password):
    """
    Verifica se la password contiene tre caratteri uguali consecutivi.

    Args:
        password (str): La password da verificare.

    Returns:
        bool: True se la password contiene tre caratteri uguali consecutivi, False altrimenti.
    """
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False

def main():
    """
    Funzione principale che gestisce l'input dell'utente e genera la password.
    """
    if len(sys.argv) > 1:
        try:
            lung_passwd = int(sys.argv[1])
            if lung_passwd < LUN_MIN_PASSWD or lung_passwd > LUN_MAX_PASSWD:
                raise ValueError
            password = genera_password(lung_passwd)
            print(f"\033[1m{password}\033[0m")
        except ValueError:
            print(f"La password deve essere di almeno {LUN_MIN_PASSWD} caratteri e massimo {LUN_MAX_PASSWD}. Inserisci solo valori numerici validi.")
    else:
        print("Generatore di Password Sicure")
        while True:
            try:
                lung_passwd = int(input("Inserisci la lunghezza della password: "))
                if lung_passwd < LUN_MIN_PASSWD or lung_passwd > LUN_MAX_PASSWD:
                    raise ValueError
                break
            except ValueError:
                print(f"La password deve essere di almeno {LUN_MIN_PASSWD} caratteri e massimo {LUN_MAX_PASSWD}. Inserisci solo valori numerici validi.")

        password = genera_password(lung_passwd)
        print(f"La password generata è: \033[1m{password}\033[0m")

if __name__ == "__main__":
    main()