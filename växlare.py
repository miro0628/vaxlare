def exChangeNow(belopp, sedel):
    return int(belopp) // sedel


def get_exchange_dirt(enbetalning, priset):
    antal_mynt = 0
    pengar_tillbaka = 0