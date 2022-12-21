class DocumentInfos:

    title = u'Programmation dynamique'
    first_name = 'Grégoire'
    last_name = 'Geinoz'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'Décembre'
    seminary_title = u'Algorithmes et structures de données II'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/donnerc/prog-dynamique"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()