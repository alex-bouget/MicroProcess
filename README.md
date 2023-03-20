# MicroProcess

python modules for simplify the creation of sub-process

## Downloading

`pip install -i https://test.pypi.org/simple/ micro-process`

## Usage

```python
from micro_process import MicroProcess

process = MicroProcess(["ls", "-l"])
while (t=process.read()) != None:
    print(t)
```