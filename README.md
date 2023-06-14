# How to run this project

```powershell
    set-executionpolicy remotesigned

    poetry env use C:\Python311\python.exe

    python -m uvicorn app.main:app --reload

    # or activate the poetry shell and run the demo
    poetry shell
    uvicorn app.main:app --reload
```
