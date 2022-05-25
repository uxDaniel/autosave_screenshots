# WinSnip - Autosave screenshots
Automatically save to disk screenshots taken with the *Snipping Tool* in Windows.

## How to use it
* Just download the latest release and run the `winsnip.exe` executable.

* Continue using `⊞ Win` + `Shift` + `S` to take screenshots. They now will appear in
  > `C:\Users\<USERNAME>\Pictures\Screenshots`

*Please notice: previous screenshots will be moved to the same folder during the first run.*


## Runing on startup
* Simply create a shortcut to `winsnip.exe` in the Startup folder
  > `C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`


## Stopping the process
* Run `taskkill /F /IM "winsnip.exe"` from the command line, or execute the `stop.bat` script provided.

---

## Building from source
Using Python 3.x:

* Install the build requirements (`pyinstaller`)
  * `pip install -r requirements.txt`
* Create the executable
  * `pyinstaller --onefile --noconsole --specpath .\src\ --name 'winsnip' .\src\main.py`

You will now find the `winsnip.exe` in the `dist` folder.