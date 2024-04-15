import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from enum import Enum

class BimDiscipline(str, Enum):
    plumbing = 'S - Sanitär'
    network = 'D - Datennetz'
    heating = 'H - Heizung'
    electrical = 'E - Elektro'
    ventilation = 'L - Lüftung'
    architecture = 'A - Architektur'

# Define the schema for the output.
class Metadata(BaseModel):
    title: str = Field(description='Title of the document')
    summary: str = Field(description='One sentence short summary of the document information')
    discipline: BimDiscipline
       
