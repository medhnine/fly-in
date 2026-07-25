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
        if self.max_drones is None:
            self.max_drones = 1
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
        visited: set["Zone"] = set()
        parent: dict["Zone", "Zone | None"] = {}
        for zone in self.zones.values():
            dist[zone] = float("inf")
            parent[zone] = None
        dist[self.start] = 0
        while True:
            lowest = float("inf")
            current = None
            for cheap in self.zones.values():
                if cheap not in visited and dist[cheap] < lowest:
                    lowest = dist[cheap]
                    current = cheap
            if current == self.end:
                path = []
                while current is not None:
                    print(current.name)
                    path.append(current.name)
                    current = parent[current]
                return path[::-1]
            elif current is None:
                return None
            neighbors = current.neighbors
            visited.add(current)
            for n in neighbors:
                if n not in visited:
                    new_cost = dist[current] + n.cost
                    if new_cost < dist[n]:
                        dist[n] = new_cost
                        parent[n] = current
























        # dist[self.start] = 0
        # current = None
        # best = float("inf")
        # parent[self.start] = None
        # while True:
        #     for cheap in self.zones.values():
        #         if cheap not in visited and dist[cheap] < best:
        #             best = dist[cheap]
        #             current = cheap
        #     if current is None:
        #         return None
        #     print(f"cheap {current.name}")
        #     neighbors = current.neighbors
        #     visited.add(current)
        #     for n in neighbors:
        #         if n not in visited:
        #             print(f"neighbor {n.name}")
        #             new_cost = dist[current] + n.cost
        #             print(f"new cost {new_cost}")
        #             print(f"dist {dist[n]}")
        #             if new_cost < dist[n]:
        #                 dist[n] = new_cost
        #                 parent[n] = current
        #                 if parent[current] is not None:
        #                     print(f"in {parent[current].name} came from {parent[n].name}")
        #         if n.name == self.end.name:
        #             # parent[self.end] = n
        #             print(f"in {parent[current].name} came from {parent[self.end].name}")
        #             x = self.end
        #             path = []
        #             # while parent[x] != None:
        #             #     x = parent[x]
        #             #     print(x.name)
        #             #     path.append(x)
        #             return path[:-1]

            

def main():
    from parsing import Parse
    obj = Parse('/home/mohhnine/Desktop/fly-in/maps/easy/02_simple_fork.txt')
    graph = Graph(2)
    zones = obj.parse(graph)
    s = "#  start_hub: start 0 0 [color=green]"
    s = s.strip()
    print(s)
    # print('fly-in')

if __name__ == '__main__':
    main()