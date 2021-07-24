# Discord Screenshot Resizer
Large image resizing directly from the clipboard for easy sharing

Prefer to share your image in full quality? Check out my other macro solution [Discord Screenshot Uploader](https://github.com/danetuso/discord-screenshot-uploader).

I've always been annoyed at the file size limit when trying to send a quick screenshot to a friend while playing games or attaching large images to work emails, so I created these tools.

&nbsp;

## Windows Setup
---
## Bind the batch script to a macro key
I typically use AutoHotKey, but in this case I bound mine to my G6 key using Logitech G Hub software. The batch file must be in the same directory as the python script.
```
# Example AutoHotKey Macro Bind
# Ctrl + LShift + 6
^+6::
Run, C:\Path\To\launch_clipboardutil.bat
```

## Install Requirements
    pip3 install pillow pywin32
(or use the included pip3 install -r requirements.txt)

&nbsp;

&nbsp;

## Windows Usage
---
## Save a screenshot to your clipboard
I typically use `Alt+PrintScrn` or `Win+Shift+S` but feel free to use your own method

## Hit your macro
Your image will be resized.

## Paste
The clipboard is automatically overwritten with the newly resized image. Paste directly into Discord, Slack, Gmail, etc.
