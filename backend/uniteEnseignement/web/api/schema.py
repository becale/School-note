from typing import List, Optional
from uuid import UUID
from datetime import date

from pydantic import Basemodel, Extra, conintn, conlist, validator

################################
#    UNITE-ENSEIGNEMENT SCHEMA
################################
class UniteEnseignementItemSchema(Basemodel):
    id:UUID
    code: str
    intitule: str
    isTroncCommun: bool = False
    nombreCredit: int
    coefficient: int
    
    volumeHoraireTD: int
    volumeHoraireCM: int
    volumeHoraireTP: int
    volumeHoraireTPE: int
    
    groupe_id:UUID
    semestre_id:UUID
    
    class Config:
        extra = Extra.forbid

class CreateUniteEnseignementSchema(Basemodel):
    id: UUID
    code: str
    intitule: str
    isTroncCommun: bool = False
    nombreCredit: int
    coefficient: int
    
    volumeHoraireTD: int
    volumeHoraireCM: int
    volumeHoraireTP: int
    volumeHoraireTPE: int
    
    groupe_id:UUID
    semestre_id:UUID
  
class GetUniteEnseignementSchema(Basemodel):
    id: UUID
    code: str
    intitule: str
    isTroncCommun: bool = False
    nombreCredit: int
    coefficient: int
    
    volumeHoraireTD: int
    volumeHoraireCM: int
    volumeHoraireTP: int
    volumeHoraireTPE: int
    
    groupe_id:UUID
    semestre_id:UUID

class GetUniteEnseignementsSchema(Basemodel):
    unites_enseignement: List[UniteEnseignementItemSchema]
    
    

################################
#    GROUPE SCHEMA
################################
class GroupeSchema(Basemodel):
    intitule: str
    credit_groupe: int
    coef_groupe: int
    
    
################################
#    SEMESTRE SCHEMA
################################
class SemestreSchema(Basemodel):
    intitule: str
    date_debut: date
    date_fin: date

