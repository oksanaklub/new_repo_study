class Apple:

    def __init__(self, name="Apple Inc.", founding_year=1976, headquarters="Cupertino, California"):
        self.name = name
        self.founding_year = founding_year
        self.headquarters = headquarters

    def company_info(self):
        info = f"Company Name: {self.name}\n"
        info += f"Founding Year: {self.founding_year}\n"
        info += f"Headquarters: {self.headquarters}"
        return info
