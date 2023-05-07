class DocumentInfos:

    title = u'Algorithme Minimax'
    first_name = 'Grégoire'
    last_name = 'Geinoz'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Mai'
    seminary_title = u'Cours OC Informatique'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/donnerc/prog-dynamique"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()