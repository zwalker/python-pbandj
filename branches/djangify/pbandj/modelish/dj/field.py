from django.db import models as dj_models

from model import Model, find_recursion


def create_field(dj_field, **kwargs):
    """Factory method for creating Field instance based on Django type
    
    Args:
    dj_field - (django field) - a django model field instance
    """
    if isinstance(dj_field, dj_models.ForeignKey):
        return ForeignKey.from_dj_field(dj_field, **kwargs)
    elif isinstance(dj_field, dj_models.ManyToManyField):
        return ManyToMany.from_dj_field(dj_field, **kwargs)
    else:
        return Field.from_dj_field(dj_field, **kwargs)
        


class Field(object):
    
    def __init__(self, name, dj_type):
        self.name = name
        self.dj_type = dj_type
        self.choices = None
    
    @staticmethod    
    def from_dj_field(dj_field, **kwargs):
        field = Field(dj_field.name, type(dj_field))
                        # Add an enumeration for each django field with choices set
        if(dj_field.choices):
            self.choices = field.choices
        return field
        

class ForeignKey(Field):
    
    def __init__(self, name, dj_type):
        Field.__init__(self, name, dj_type)
    
    @staticmethod    
    def from_dj_field(dj_field, **kwargs): 
#        if no_follow_fields is None:
#            no_follow_fields = []
#        if  no_follow_models is None:
#            no_follow_models = []
        
        follow_related = kwargs.get('follow_related', True)    
        no_follow_fields = kwargs.get('no_follow_fields', [])
        no_follow_models = kwargs.get('no_follow_models', [])
            
        if isinstance(dj_field, dj_models.ForeignKey):
            # By default leave type as a ForeignKey
            field = ForeignKey(dj_field.name, type(dj_field))
        else:
            raise PbandjFieldException("Supplied field is not a ForeignKey")
            
        # If foreign key recrusion is active.
        dj_fk_model = dj_field.rel.to
        if follow_related and not dj_field.name in no_follow_fields and not dj_fk_model in no_follow_models:
            if isinstance(dj_fk_model, str):
                # TODO: Handle ForeignKey supplied as a str
                raise NotImplemented('Unable to handle Django ForeignKey fields declared with a string passed for related model')
                #fk_dj_model = models.__dict__[fk_dj_model]
               
            pbandj_fk_model = Model.from_django_model(dj_fk_model, **kwargs)
            field.dj_type = pbandj_fk_model
        return field
    
    
class ManyToMany(Field):
    
    def __init__(self, name, dj_type):
        Field.__init__(self, name, dj_type)
        self.through = None
        
    @staticmethod
    def from_dj_field(dj_field, **kwargs): 
#        if no_follow_fields is None:
#            no_follow_fields = []
#        if  no_follow_models is None:
#            no_follow_models = []
            
        follow_related = kwargs.get('follow_related', True)    
        no_follow_fields = kwargs.get('no_follow_fields', [])
        no_follow_models = kwargs.get('no_follow_models', [])
            
        if isinstance(dj_field, dj_models.ManyToManyField):
            # By default leave type as a ManyToMany
            field = ManyToMany(dj_field.name, type(dj_field))
        else:
            raise PbandjFieldException("Supplied field is not a ManyToManyField")
        
        if follow_related and not dj_field.name in no_follow_fields:
            
            # If there is a 'through' model, capture it.
            # If there are only 3 fields than there is only an id and a fk to each
            # side of the relation so this is probably not a user defined assoc class
            if (not dj_field.rel.through is None and
                len(dj_field.rel.through._meta.fields) > 3):
                # There is data associated with the relation
                if follow_related and not dj_field.rel.through in no_follow_models:
                    field.through = Model.from_django_model(dj_field.rel.through, **kwargs) 

            # NOTE THE SIDE EFFECT OF CALLING Model.from_django_model ON
            # THROUGH MODEL IS THAT THE TO MODEL GETS ADDED TO no_follow_models
            # IN kwargs on the way.
            else:
                # Just like a foreign key but repeated
                dj_m2m_model = dj_field.rel.to
                if not dj_m2m_model in no_follow_models:
                    if isinstance(dj_m2m_model, str):
                        # TODO: Handle ManyToManyField supplied as a str
                        raise NotImplemented('Unable to handle Django ManyToManyField declared with a string passed for related model')
                        #fk_dj_model = models.__dict__[fk_dj_model]
                    pbandj_m2m_model = Model.from_django_model(dj_m2m_model, **kwargs)
                    field.dj_type = pbandj_m2m_model
            
        return field            