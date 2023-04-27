# storage class for exit data, handles transitions

class Exit:
  def __init__(self, verb: str, loc_name: str, travel_str: str, req_item: str=None, fail_str: str=None):
    self._verb = verb
    self._loc_name = loc_name
    self._travel_str = travel_str
    self._req_item = req_item
    self._fail_str = fail_str

  def get_verb(self):
    return self._verb

  def get_loc_name(self):
    return self._loc_name

  def get_travel_str(self):
    return self._travel_str

  def get_fail_str(self):
    return self._fail_str

  def get_req_item(self):
    return self._req_item