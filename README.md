# LupaBot :robot:
### A simple tool to make a bot 
## :mailbox_with_mail: Description
LupaBot is a tool to configure a chatbot to use on my website
## :computer: Usage
### Download
``` sh
 git clone https://github.com/lks2007/LupaBot.git
```

### Config
Open bot.py, you must change the token:
```python
self.token = 'YOUR TOKEN HERE'
```

Then, you can change the prefix:
```python
prefix = add_prefix('YOUR PREFIX') 
```

After that, you can add command:
```python
self.NAME_COMMAND = addCommand(['NAME_COMMAND'], ['YOUR RESPONSE'])
```

You can also add arg:
```python
 self.NAME_COMMAND = addCommand(['NAME_COMMAND', 'ARG_COMMAND'], ['YOUR RESPONSE', 'RESPONSE_ARG']) 
```