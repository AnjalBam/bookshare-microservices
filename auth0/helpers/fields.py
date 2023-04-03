import datetime

from django.db.models.fields import CharField
from helpers.utils import get_uid_str


class AutoIdxField(CharField):
    def __init__(self, auto=True, primary_key=True, *args, **kwargs):
        kwargs['max_length'] = 50
        kwargs['unique'] = True
        kwargs['primary_key'] = primary_key
        self.auto = auto
        if auto:
           kwargs["editable"] = False
           kwargs["blank"] = True
        super(AutoIdxField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        idx_prefix = getattr(model_instance, "IDX_PREFIX", None)

        if not idx_prefix:
            raise ValueError("`IDX_PREFIX` is not defined in the model.")
        
        if len(idx_prefix) != 3:
            raise ValueError("`IDX_PREFIX` must have 3 characters only. e.g. 'usr' or 'txn'")

        value = super(AutoIdxField, self).pre_save(model_instance, add)

        if not value:
            value = idx_prefix + "_" + str(datetime.datetime.today().year)[2:] + "_" + get_uid_str()
            setattr(model_instance, self.attname, value)
        return value

    def formfield(self, **kwargs):
        if self.auto:
            return None
        return super(AutoIdxField, self).formfield(**kwargs)