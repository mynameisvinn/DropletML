# DropletML
**DropletML** lets you save and share PyTorch model weights on the cloud with minimal code overhead. If you know `torch.save`, then you'll know Droplet.

## Why Droplet?
* No size limitation. Droplet can tolerate up to 5TB models.
* Minimal code overhead. You don't need to write additional code.
* Single API to learn. There is a single function 'droplet'. That's it.
* Easy to share. You can share your model with anyone.

## Install
```bash
pip install DropletML
```

## Quickstart
You can save PyTorch models to s3 in the same manner you would save to a local filesystem.
```python
from DropletML import droplet

path = droplet('foobar')  # give your droplet a name
torch.save(model, path)  # identical to saving a model to local file
# prints rainpuddle/foobar-89ea455e.pt
```
Afterwards, anyone who knows your tag can access your model.
```python
path = droplet('rainpuddle/foobar-89ea455e.pt')
restored_model = torch.load(path)
```
Of course, you can retrieve model weights without a droplet.
```python
import boto3

client = boto3.client('s3')
client.download_file('rainpuddle', 'foobar-89ea455e.pt','./foobar-89ea455e.pt')
```