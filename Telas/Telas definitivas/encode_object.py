import numpy as np
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(CustomEncoder, self).default(obj)
        
#data_dict_1 = json.dumps(data_dict,cls=CustomEncoder)
#data_dict_final  = json.loads(data_dict_1)