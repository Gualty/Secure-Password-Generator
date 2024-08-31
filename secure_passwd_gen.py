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
LUN_MIN_PASSWD = 8  # Lunghezza minima della password
LUN_MAX_PASSWD = 1000  # Lunghezza massima della password


def genera_password(lung_passwd, special=True, numbers=True, uppercase=True):
    """
    Genera una password sicura rispettando i criteri di sicurezza specificati.

    Args:
        lung_passwd (int): La lunghezza della password da generare.
        special (bool): Se True, include caratteri speciali nella password.
        numbers (bool): Se True, include numeri nella password.
        uppercase (bool): Se True, include lettere maiuscole nella password.

    Returns:
        str: La password generata che soddisfa i criteri di sicurezza.
    """
    caratteri_speciali = "!@#%&/()=?"
    caratteri = string.ascii_lowercase

    if uppercase:
        caratteri += string.ascii_uppercase
    if numbers:
        caratteri += string.digits
    if special:
        caratteri += caratteri_speciali

    if len(caratteri) == 0:
        raise ValueError("Devi scegliere almeno un tipo di carattere per generare la password.")

    while True:
        password = random.choices(caratteri, k=lung_passwd)

        # Garantisce la presenza di almeno un carattere di ciascun tipo se richiesto
        if uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if numbers:
            password.append(random.choice(string.digits))
        if special:
            password.append(random.choice(caratteri_speciali))

        # Assicurati che la password non abbia più di tre caratteri uguali consecutivi
        if not contiene_caratteri_uguali_consecutivi(password):
            random.shuffle(password)
            password = ''.join(password[:lung_passwd])
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

def mostra_aiuto():
    """
    Mostra il messaggio di aiuto con la descrizione delle opzioni disponibili.
    """
    help_message = """
    Utilizzo: python3 secure_passwd_gen.py [LUNGHEZZA] [OPZIONI]

    Genera una password sicura con le seguenti opzioni:

    LUNGHEZZA
        Specifica la lunghezza della password da generare (minimo 8 caratteri).

    OPZIONI:
        --no-special    Esclude i caratteri speciali dalla password.
        --no-numbers    Esclude i numeri dalla password.
        --no-uppercase  Esclude le lettere maiuscole dalla password.
        -h, --help      Mostra questo messaggio di aiuto.

    Esempio:
        python python3 secure_passwd_gen.py 12 --no-special --no-numbers
        Questo comando genera una password di 12 caratteri contenente solo lettere minuscole e maiuscole.
    """
    print(help_message)


def main():
    """
    Funzione principale che gestisce l'input dell'utente e genera la password.
    """
    if len(sys.argv) > 1:
        if '-h' in sys.argv or '--help' in sys.argv:
            mostra_aiuto()
            return

        try:
            lung_passwd = int(sys.argv[1])
            if lung_passwd < LUN_MIN_PASSWD or lung_passwd > LUN_MAX_PASSWD:
                raise ValueError

            special = '--no-special' not in sys.argv
            numbers = '--no-numbers' not in sys.argv
            uppercase = '--no-uppercase' not in sys.argv

            password = genera_password(lung_passwd, special, numbers, uppercase)
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

                special = input("Vuoi usare caratteri speciali? (sì/no, predefinito: sì): ").strip().lower() != 'no'
                numbers = input("Vuoi usare numeri? (sì/no, predefinito: sì): ").strip().lower() != 'no'
                uppercase = input("Vuoi usare lettere maiuscole? (sì/no, predefinito: sì): ").strip().lower() != 'no'

                break
            except ValueError:
                print(
                    f"La password deve essere di almeno {LUN_MIN_PASSWD} caratteri e massimo {LUN_MAX_PASSWD}. Inserisci solo valori numerici validi.")

        password = genera_password(lung_passwd, special, numbers, uppercase)
        print(f"La password generata è: \033[1m{password}\033[0m")


# Questo blocco permette di eseguire il codice come script standalone
if __name__ == "__main__":
    main()
