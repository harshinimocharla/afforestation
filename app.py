import datetime

class Crop:
    def __init__(self, name, growth_period_days, water_requirement_per_day):
        self.name = name
        self.growth_period_days = growth_period_days
        self.water_requirement_per_day = water_requirement_per_day
        self.planted_date = None
        self.harvest_date = None

    def plant(self, date):
        self.planted_date = date
        self.harvest_date = date + datetime.timedelta(days=self.growth_period_days)
        print(f"Planted {self.name} on {self.planted_date}. Harvest on {self.harvest_date}.")

    def water_needed(self):
        if self.planted_date is None:
            return 0
        days_until_harvest = (self.harvest_date - datetime.datetime.now().date()).days
        return days_until_harvest * self.water_requirement_per_day

    def status(self):
        if self.planted_date is None:
            return f"{self.name} is not planted."
        today = datetime.datetime.now().date()
        if today >= self.harvest_date:
            return f"{self.name} is ready for harvest."
        else:
            return f"{self.name} is growing. Days until harvest: {(self.harvest_date - today).days}."

def main():
    # Example crop
    mushroom = Crop(name="mushroom", growth_period_days=20, water_requirement_per_day=0.5)
    
    # Plant the crop
    plant_date = datetime.datetime.now().date()
    mushroom.plant(plant_date)
    
    # Check status
    print(mushroom.status())
    
    # Water needed
    print(f"Water needed until harvest: {mushroom.water_needed()} liters")

if __name__ == "__main__":
    main()
