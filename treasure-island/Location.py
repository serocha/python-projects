# storage class for location data

class Location:
  def __init__(self, name: str, desc: str, item: str=None, item_desc: str=None, exits: list=[]):
    self._name = name
    self._desc = desc
    self._item = item
    self._item_desc = item_desc
    self._exits = exits

  def get_name(self):
    return self._name

  def get_desc(self):
    return self._desc

  def get_item(self):
    return self._item

  def get_item_desc(self):
    return self._item_desc

  def get_exits(self):
    return self._exits

  def take_item(self):
    item = self.get_item()
    self._item = None
    return item