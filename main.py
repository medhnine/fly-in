class Zone:
    def __init__(self, name: str, x: int, y: int, color: str, zone_type: str, max_drones: int):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.zone_type = zone_type
        self.max_drones = max_drones
        self.neighbors = []

    @property
    def cost(self) -> int:
        if self.zone_type == "restricted":
            return 2
        return 1
    def set_default(self):
        if self.color is None:
            self.color = "yellow"
        if self.max_drone is None:
            self.max_drone = 1
        if self.zone_type is None:
            self.zone_type = "normal"

class Graph:
    def __init__(self, nb_drones: int):
        self.nb_drones = nb_drones
        self.zones : dict[str, Zone] = {}
        self.start: Zone | None = None
        self.end: Zone | None = None

    def add_zone(self, zone):
        if zone.name in self.zones:
            raise ValueError("duplicated zone name")
        else:
            self.zones[zone.name] = zone

    def get_zone(self, z_name):
        return self.zones.get(z_name)

    def connect(self, name1, name2):
        zone1 = self.zones[name1]
        zone2 = self.zones[name2]
        zone1.neighbors.append(zone2)
        zone2.neighbors.append(zone1)
    def find_path(self):
        if self.start is None or self.end is None:
            raise ValueError("start or end missing")
        dist: dict["Zone", float] = {}
        visited: set["Zone"] = {}
        parent: dict["Zone", "Zone | None"] = {}
        for zone in self.zones.values():
            dist[zone] = float("inf")
        dist[self.start] = 0
        for z in self.start.neighbors:
            z
            

def main():
    s = "#  start_hub: start 0 0 [color=green]"
    s = s.strip()
    print(s)
    # print('fly-in')

if __name__ == '__main__':
    main()