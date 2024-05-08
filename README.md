# VO Space API to CANFAR CAVERN
VO Space API to interact with CANFAR CAVERN

Example to import and use this package:

```
import vospaceapi
## Configure IAM token with vospaceapi.SKATOKEN = <your token>
## Configure where your CAVERN endpoint is located CAVERNSERVICE="https://spsrc25.iaa.csic.es/cavern/"
## After that you can interact with CAVERN VO Space.
## Get a file:
vospaceapi.voget("quaternion.ipynb","q.ipynb")
## Put a file:
vospaceapi.voupload("M31.fits","M31.fits")
