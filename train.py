import os
import arcpy
from torch.testing._internal.distributed.rpc.examples.parameter_server_test import in_features

print(os.getcwd())
import datetime

print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

import arcpy
arcpy.env.workspace = "C:/data/data/gdb"
arcpy.analysis.Union(["well_buff50", "stream_buff200", "waterbody_buff500"],
                     "water_buffers", "NO_FID", 0.0003)
arcpy.analysis.Union([["counties", 2], ["parcels", 1], ["state", 2]],
                     "state_landinfo")