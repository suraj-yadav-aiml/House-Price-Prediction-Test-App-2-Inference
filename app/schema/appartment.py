from pydantic import BaseModel


class Apartment(BaseModel):
    """
    A Pydantic model representing the attributes of a rental apartment. 

    Attributes:
        area (int): The floor area of the apartment in square feet.
        constraction_year (int): The year the apartment was constructed.
        bedrooms (int): Number of bedrooms in the apartment.
        garden_area (int): Garden area in square feet. Use 0 if no garden is present.
        balcony_present (int): Indicates the presence of a balcony (1 for Yes, 0 for No).
        parking_present (int): Indicates if parking is available (1 for Yes, 0 for No).
        furnished (int): Indicates if the apartment is furnished (1 for Yes, 0 for No).
        garage_present (int): Indicates if there is a garage (1 for Yes, 0 for No).
        storage_present (int): Indicates if storage space is available (1 for Yes, 0 for No).
    """

    area: int
    constraction_year: int
    bedrooms: int
    garden_area: int
    balcony_present: int
    parking_present: int
    furnished: int
    garage_present: int
    storage_present: int
