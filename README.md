# Droplet
**Droplet** lets you save and share PyTorch model weights with zero code overhead. It is dropbox for ml models.

## Install
```bash
pip install DropletML
```

## Quickstart
You can save PyTorch models to a shared store in the same manner you would save to a local filesystem.
```python
from DropletML import droplet

# save a PyTorch model to a droplet
path = droplet('foobar')  # name your droplet
torch.save(model, path)  # identical to saving a model to local file
```
Now anyone with the resulting url can access your model's weights.
```python
restored_model = torch.load(droplet('rainpuddle/foobar-89ea455e.pt'))
```