# slugkit

A tiny string-slug utility. Turns arbitrary text into URL-safe slugs.

This repository is a disposable fixture for exercising the
workflow-template **local modality** end-to-end. It deliberately carries
no `.github/` plumbing, no issue tracker, and no project board — the
local workflow keeps all of that outside the repo.

## Usage

```python
from slugify import slugify

slugify("Hello, World!")  # -> "hello-world"
```
