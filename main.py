from asyncio import proactor_events
from operator import le


database = [
    {"name": "Homero Jay Simpson", "Hombre": True, "Familia": True, "Adulto": True, "Casado": True,     "Nuclear": True, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": True, "Lentes": False, "Bromista": True,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Marjorie \"Marge\" Bouvier", "Hombre": False, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": True, "Religioso": True, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": True,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Bartholomew \"Bart\" Jojo Simpson", "Hombre": True, "Familia": True, "Adulto": False, "Casado": False, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": True, "Lentes": False, "Bromista": True,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": True, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Lisa Marie Simpson", "Hombre": False, "Familia": True, "Adulto": False, "Casado": False, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": True, "Religioso": False, "Trenes": False, "Duff": True,
        "Calvo": False, "Lentes": False, "Bromista": False, "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False},

    {"name": "Margaret \"Maggie\" Simpson", "Hombre": False, "Familia": True, "Adulto": False, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": True, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": True, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Abraham \"Abe\" Simpson", "Hombre": True, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": True, "Maestro/Director": False, "Guerra": True, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Abbie Simpson (Media Hermana de Homero)", "Hombre": False, "Familia": True, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
     "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Mona Simpson", "Hombre": False, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": True, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": True,
        "Bebe": True, "Vivo": False, "Animal": False, "Viejo": True, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": True, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Herbert Powell", "Hombre": True, "Familia": True, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": True, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Tyrone Simpson (Hermano de Abe)", "Hombre": True, "Familia": True, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
     "Bebe": False, "Vivo": True, "Animal": False, "Viejo": True, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Cyrus Simpson (Hermano de Abe)", "Hombre": True, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
     "Bebe": False, "Vivo": True, "Animal": False, "Viejo": True, "Maestro/Director": False, "Guerra": True, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": True, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Chet Simpson (Hermano de Abe)", "Hombre": True, "Familia": True, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": True, "Lentes": False, "Bromista": False,
     "Bebe": False, "Vivo": True, "Animal": False, "Viejo": True, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": True},

    {"name": "Amber Simpson (Esposa de Las Vegas)", "Hombre": False, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
     "Bebe": False, "Vivo": False, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Eliza Simpson", "Hombre": False, "Familia": True, "Adulto": False, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": True, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": False, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": True, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Hiram Simpson", "Hombre": True, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": False, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": True, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Mabel Simpson", "Hombre": False, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": True, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": False, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": True, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": True, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Virgil Simpson", "Hombre": True, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": False, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": True, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": True, "Amarillo": False, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Carl Carlson", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": True, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": True, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Charles Montgomery Plantagenet Schicklgruber Burns", "Hombre": True, "Familia": False, "Adulto": True, "Casado": False, "Nuclear": True, "Primary": False, "Indian": False, "Rich": True, "Cantinero": False, "Genio": True, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": True, "Lentes": False,
        "Bromista": False, "Bebe": False, "Vivo": True, "Animal": False, "Viejo": True, "Maestro/Director": False, "Guerra": True, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Duffman", "Hombre": True, "Familia": False, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": True, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": True, "Bromista": False, "Bebe": False,
        "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Milhouse Van Houten", "Hombre": True, "Familia": False, "Adulto": False, "Casado": False, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": True, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": True, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Nedward \"Ned\" Flanders", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": True, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": True, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": True, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Jonathan \"John\" I.Q. Neidelbaum Frink, Jr.", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": True, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": True,
        "Bromista": False, "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": True, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Apu Nahasapeemapetilon", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": True, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": True, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": False, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Bernard \"Barney\" Arnold Gomez", "Hombre": True, "Familia": False, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Robert \"Bob Patiño\" Underdunk Terwilliger Jr.", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": True, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False,
        "Bromista": False, "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": True, "Doctor": False, "ShowKrusty": True, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Clancy Górgory", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": True, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Cleto Del Roy Spuckler", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": True, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Edna Krabappel", "Hombre": False, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": False, "Animal": False, "Viejo": False, "Maestro/Director": True, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Jeffrey \"Jeff\" Albertson", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": True, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Julio Hibbert", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": True, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": True, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": False, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Kent Brockman", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": True, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": True, "HijoGorgory": False, "Calamares": False},

    {"name": "Kirk Van Houten", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": True, "Lentes": True, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Maurice \"Moe\" Lester Szyslak", "Hombre": True, "Familia": False, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": True, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Nelson Mandela Muntz", "Hombre": True, "Familia": False, "Adulto": False, "Casado": False, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": True,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": True, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Otto Mann", "Hombre": True, "Familia": False, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Patricia \"Patty\" Alvarine Bouvier", "Hombre": False, "Familia": True, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Rafa Gorgory", "Hombre": True, "Familia": False, "Adulto": False, "Casado": False, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": True, "Calamares": False},


    {"name": "Selma Bouvier", "Hombre": False, "Familia": True, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Seymour Skinner (Armando Barrera)", "Hombre": True, "Familia": False, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": True, "Guerra": True, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Wuándulo/Acasio Josephine Smithers Jr.", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": True, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": False, "Calvo": False, "Lentes": True, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "\"Willie\" K. MacDougal", "Hombre": True, "Familia": False, "Adulto": True, "Casado": False, "Nuclear": False, "Primary": True, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": True, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Reverendo Alegría", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": False, "Cantinero": False, "Genio": False, "Religioso": True, "Trenes": True, "Duff": False, "Calvo": False, "Lentes": False, "Bromista": False,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},

    {"name": "Krysty el Payaso", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": True, "Cantinero": False, "Genio": False, "Religioso": True, "Trenes": False, "Duff": False, "Calvo": True, "Lentes": False, "Bromista": True,
        "Bebe": False, "Vivo": True, "Animal": False, "Viejo": False, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": False, "Doctor": False, "ShowKrusty": True, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": True, "HijoGorgory": False, "Calamares": False},

    {"name": "Don Marion Anthony \"Gordo Tony\" D'Amico", "Hombre": True, "Familia": False, "Adulto": True, "Casado": True, "Nuclear": False, "Primary": False, "Indian": False, "Rich": True, "Cantinero": False, "Genio": False, "Religioso": False, "Trenes": False, "Duff": True, "Calvo": False, "Lentes": False, "Bromista": False,
     "Bebe": False, "Vivo": False, "Animal": False, "Viejo": True, "Maestro/Director": False, "Guerra": False, "Policia": False, "Criminal": True, "Doctor": False, "ShowKrusty": False, "Gato": False, "Haiti": False, "Campirano": False, "Amarillo": True, "Comics": False, "Television": False, "HijoGorgory": False, "Calamares": False},


]


def verificar(answer, property):
    if answer == "y":
        ans = True
    elif answer == "n":
        ans = False
    else:
        answer1 = input(
            "Respuesta invalida, ingresa otra vez la respuesta (y|n): ")
        verificar(answer1, property)

    removedOnes = []
    for d in database:
        if d[property] != ans:
            removedOnes.append(d)

    for i in removedOnes:
        database.remove(i)

    if len(database) == 1:
        print("Tu personaje es "+database[0]["name"])
        quit()


ans = input("¿Tu personaje es hombre? (y|n): ")
verificar(ans, "Hombre")

ans = input(
    "¿Tu personaje está relacionado a la familia directa de Los Simpson? (y|n): ")
verificar(ans, "Familia")

ans = input("¿Tu personaje es un adulto? (y|n):")
verificar(ans, "Adulto")

ans = input("¿Tu personaje está o estuvo casado? (y|n): ")
verificar(ans, "Casado")

ans = input("¿Tu personaje trabaja en la planta de energia nuclear? (y|n): ")
verificar(ans, "Nuclear")

ans = input("¿Tu personaje asiste a la escuela primaria de Springfield (y|n): ")
verificar(ans, "Primary")

ans = input("¿Tu personaje es indio? (y|n): ")
verificar(ans, "Indian")

ans = input("¿Tu personaje es rico/adinerado? (y|n): ")
verificar(ans, "Rich")

ans = input("¿Tu personaje es cantinero? (y|n): ")
verificar(ans, "Cantinero")

ans = input("¿Tu personaje es genio? (y|n): ")
verificar(ans, "Genio")

ans = input("¿Tu personaje es fanatico religioso? (y|n): ")
verificar(ans, "Religioso")

ans = input("¿A tu personaje le gustan los trenes? (y|n): ")
verificar(ans, "Trenes")

ans = input("¿Tu personaje es consumidor frecuente de la cerveza Duff? (y|n): ")
verificar(ans, "Duff")

ans = input("¿Tu personaje es calvo? (y|n): ")
verificar(ans, "Calvo")

ans = input("¿Tu personaje usa lentes? (y|n): ")
verificar(ans, "Lentes")

ans = input("¿Tu personaje es bromista? (y|n): ")
verificar(ans, "Bromista")

ans = input("¿Tu personaje es un bebé? (y|n): ")
verificar(ans, "Bebe")

ans = input("¿Tu personaje está vivo? (y|n): ")
verificar(ans, "Vivo")

ans = input("¿Tu personaje es viejo (mayor de 60)? (y|n): ")
verificar(ans, "Viejo")

ans = input(
    "¿Tu personaje es maestro o director de la primaria de Springfield (y|n): ")
verificar(ans, "Maestro/Director")

ans = input("¿Tu personaje estuvo en la guerra? (y|n): ")
verificar(ans, "Guerra")

ans = input("¿Tu personaje pertenece al departamento de policia? (y|n): ")
verificar(ans, "Policia")

ans = input("¿Tu personaje es un criminal? (y|n): ")
verificar(ans, "Criminal")

ans = input("¿Tu personaje es un Doctor? (y|n): ")
verificar(ans, "Doctor")

ans = input("¿Tu personaje pertenece o perteneció al Show de Krusty? (y|n): ")
verificar(ans, "ShowKrusty")

ans = input("¿Tu personaje es de vida campirana? (y|n): ")
verificar(ans, "Campirano")

ans = input("¿Tu personaje es amarillo? (y|n): ")
verificar(ans, "Amarillo")

ans = input("¿A su personaje le gustan los comics? (y|n): ")
verificar(ans, "Comics")

ans = input("¿Su personaje sale en television? (y|n): ")
verificar(ans, "Television")

ans = input("¿Su personaje es hijo del jefe Gorgory? (y|n): ")
verificar(ans, "HijoGorgory")
