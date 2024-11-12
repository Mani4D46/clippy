<div align="center">
<h1>clippy</h1>

> A simple cli tool to store bookmarks, links or anything (other than passwords!) to copy paste from the terminal!

</div>

## Data
The data is stored at `.config/clippy.json`.

## Installation:
1) Firstly install the modules:<br>
`pip install -r requirements.txt`<br>
If you're like me and you use arch linux you can do<br>
`sudo pacman -Sy python-pyperclip python-termcolor`<br>

2) Leave the rest to the installer
```
chmod +x install.sh
./install.sh
```

## How to use:
You can use it as a clipboard or a bookmark storage or for any other purpose! It's very flexible.<br>
The overall storing process is as `KEY: VALUE` inside a json file at `.config/clippy.json`.<br>

### Flags:
```
  -h, --help            show this help message and exit
  -d, --display         display available keys with vals in the clipboard
  -cb, --clipboard      display only available vals in the clipboard
  -n, --noquit          doesn't quit after doing the job
  -a KEY, --add KEY     Add a bookmark with key and auto recognized pasted content
  -b KEY VALUE, --bookmark KEY VALUE
                        Add a bookmark with key and self entered value
  -c KEY, --copy KEY    Copy the value of a selected key
  -r KEY, --remove KEY  Delete a selected key
  -at, --addtui         same as -a but gives an input field
  -bt, --bookmarktui    same as -b but gives input fields
  -ct, --copytui        same as -c but gives an input field
  -rt, --removetui      same as -r but gives an input field
```

The difference between `--add` and `--bookmark` is that let's say you've copied `anexamplevalue` and want to save it as `akey` you do `clippy -a akey` and it saves `anexamplevalue` with key `akey`. On the other hand if you want to input the value yourself you use `bookmark` as `clippy -b akey anexamplevalue`. Both save the same thing except that with `-b` you get more flexibility and with `-a` you get speed and convenience.
