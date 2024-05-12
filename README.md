<div align="center">
  <h1>Pretty Console</h1>
</div>

<h2 align="center">Fully customizable console printing and 100% centered on every window resolution</h2>
<h3>Requirements: </h3>
<ul>
  <li>Colorama</li>
  <li>Shutil</li>
</ul>

<h2>How to use it: </h2>

```python
from console import Main as Console

def main():
  Console = ConsoleClass()
  Console.output(Console.Types.Info, "Hello world!")

# Which returns "[?] Hello world!"
```
# Full size window
![Full](https://raw.githubusercontent.com/TedyonGit/PrettyConsole/main/full.png)
# Normal size window
![Normal](https://raw.githubusercontent.com/TedyonGit/PrettyConsole/main/normal.png)


# Console Output Types:
- Success
- Error
- Warning
- Info
  
<h3>You can modify the printing by editing console.py in 'OutputTypes'</h3>

Made with ❤ by Tedy
