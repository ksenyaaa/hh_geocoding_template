from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def tree(self, node: TreeNode, address: str):
        self.dict[node.id] = address
        for areas in node.areas:
            self.tree(areas, address + ", " + areas.name)

    def _apply_geocoding(self, area_id: str) -> str:
        if not self.dict:
            for node in self.__data:
                self.tree(node, node.name)

        return self.dict.get(area_id, "")

