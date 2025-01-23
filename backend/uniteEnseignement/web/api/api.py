from datetime import date
from typing import Optional, List , Dict
from uuid import UUID

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from web.app import app
from web.api.schema import (
    UniteEnseignementItemSchema,
    CreateUniteEnseignementSchema,
    GetUniteEnseignementSchema,
    GetUniteEnseignementsSchema,
    GroupeSchema,
    SemestreSchema
)

##################################
# APIs POUR UNITE ENSEIGNEMENT
##################################

uEs : List[dict] = [
    {
       'id': "38400000-8cf0-11bd-b003-0800200c9a66",
        'code': 'EPS231'
    },
    {
        'id': "710b9629-9b1d-484e-95cf-96545bf40015",
        'code': 'EPS232'
    },
    {
        'id': "c08fa148-3edd-4b89-970a-15f75d1d0400",
        'code': 'EPS233'
    }
]

@app.get('/unite-enseignements', response_model=GetUniteEnseignementsSchema)
def get_unite_enseignement(limit: Optional[int] = None,  
                          is_tronc_commun: Optional[bool] = None
                          ,semestre: Optional[int] = None
                          ,volume_horaire: Optional[float] = None
                        ):
    """ 
        Cette API renvoie la liste des Unites d'enseignement
        filtrée suivant 4 paramètres:
            * limit
            * is_tronc_commun
            * semestre
            * volume_horaire 
    """
    if limit is None and is_tronc_commun is None and semestre is None and volume_horaire is None:
        return {'unites-enseignement': uEs}
