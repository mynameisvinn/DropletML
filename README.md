# Droplet
**Droplet** lets you share PyTorch models with zero code overhead.

## Quickstart
```python
from raincloud import droplet

# replace path to local filesystem with a droplet
torch.save(model, droplet('foobar'))  

# prints a unique url mynameisvinn/foobar-8fd86dee.pt
```
Anyone with the resulting url can access your model's weights.
```python
restored_model = torch.load(droplet('mynameisvinn/foobar-8fd86dee.pt'))
```

## Why Droplet?
* Google Drive is not tightly integrated with ML frameworks like PyTorch.
* Github LFS is not intuitive.