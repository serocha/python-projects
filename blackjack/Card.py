class Card:
    def __init__(self, val: int=0, suit: str="", is_face_card: bool=False, face_type: str=""):
        self._val = val  # aces are assigned 11
        self._suit = suit
        self._is_face_card = is_face_card  # could subclass
        self._face_type = face_type

    def get_val(self) -> int:           
        return self._val

    def get_suit(self) -> str:
        return self._suit

    def is_face_card(self) -> bool:
        return self._is_face_card

    def get_face_type(self) -> str:
        return self._face_type

    def set_val(self, val: int) -> None:
        self._val = val

    def set_suit(self, suit: str) -> None:
        self._suit = suit

    def set_is_face(self, face_bool: bool) -> None:
        self._is_face_card = face_bool

    def set_face_type(self, face_type: str) -> None:
        self._face_type = face_type

    