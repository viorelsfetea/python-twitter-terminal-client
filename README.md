# Twitter terminal client
An extendable terminal Twitter client written in Python
 
##Demo
_(on Youtube)_

[![Twitter terminal client](http://img.youtube.com/vi/hUdFmAVoKtY/hqdefault.jpg)](http://www.youtube.com/watch?v=hUdFmAVoKtY)

##Running it
Create a virtual environment and pull the files into it

Do `pip install -r dev_requirements.txt` and `pip install -r requirements.txt` if you want to extend the client.

Do `pip install -r requirements.txt` if you want just want to run it.

Run the client with `python -m twitterclient.main`

Use `fab test` to run the unit tests

##Extending the command list
To add a new command, you have to create a class for it. All commands extend the CommandAbstract class and are loaded via the CommandFactory factory.

Basic command class structure:

```python
from CommandAbstract import CommandAbstract


class CommandName(CommandAbstract):
    def run(self):
        pass
```

##TODO
* Complete list of commands, including but not limited to: search, retweet, reply
* Emoji support
