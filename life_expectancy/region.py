"""Region ENUM."""

from enum import Enum


class Region(str, Enum):
    """Type of Entity."""

    AT = "AT"
    BE = "BE"
    BG = "BG"
    CH = "CH"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    EE = "EE"
    EL = "EL"
    ES = "ES"
    EU27_2020 = "EU27_2020"
    FI = "FI"
    FR = "FR"
    HR = "HR"
    HU = "HU"
    IS = "IS"
    IT = "IT"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    MT = "MT"
    NL = "NL"
    NO = "NO"
    PL = "PL"
    PT = "PT"
    RO = "RO"
    SE = "SE"
    SI = "SI"
    SK = "SK"
    DE = "DE"
    DE_TOT = "DE_TOT"
    AL = "AL"
    EA18 = "EA18"
    EA19 = "EA19"
    EFTA = "EFTA"
    IE = "IE"
    ME = "ME"
    MK = "MK"
    RS = "RS"
    AM = "AM"
    AZ = "AZ"
    GE = "GE"
    TR = "TR"
    UA = "UA"
    BY = "BY"
    EEA30_2007 = "EEA30_2007"
    EEA31 = "EEA31"
    EU27_2007 = "EU27_2007"
    EU28 = "EU28"
    UK = "UK"
    XK = "XK"
    FX = "FX"
    MD = "MD"
    SM = "SM"
    RU = "RU"

    def __repr__(self) -> str:
        return str(self.value)

    @classmethod
    def actual_countries(cls):
        """Returns list of actual countries, filtering out non-country."""
        non_countries = {
            "EU27_2020",
            "DE_TOT",
            "EA18",
            "EA19",
            "EFTA",
            "EEA30_2007",
            "EEA31",
            "EU27_2007",
            "EU28",
        }
        return [
            region.value for region in cls if region.value not in non_countries
        ]

    @classmethod
    def get(cls, name: str) -> "Region":
        """
        Returns the Region corresponding to the given string.
        Args:
            name (str): The name of the region.

        Returns:
            Region: The corresponding Region enum value.

        Raises:
            ValueError: If the name is not a valid Region.
        """
        try:
            return cls[name]
        except KeyError:
            raise ValueError(f"'{name}' is not a valid Region")
