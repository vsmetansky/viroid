class Diseases:
    def __init__(self, db, *diseases):
        for d in diseases:
            d._r = db
