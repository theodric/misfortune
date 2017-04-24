# fortune
fortunes for the UNIX FORTUNE program

You'll probably want to install fortune so that you have 'strfile' installed, because you'll need it to create the dat file.
If you're on OSX, I recommend https://github.com/johnpneumann/Fortune-OSX

Of note in this repo is fortunefilecreator.sh
It's nothing special, or particularly good, but it does the job. I'm sure you can do it better: please do; I stop caring once it works. :shipit:

 You feed it a text file with fortunes separated by empty lines containing linefeeds (just LF, not CRLF-- we're on UNIX, eh buddy?) and it spits out the %-delimited fortune file and runs strfile to create the requisite .dat.

Your input text file needs to look like this:

```
Alienation produces eccentrics or revolutionary.

Savor kindness because cruelty is always possible later.

In a dream you saw a way to survive and you were full of joy.
```

Running fortunefilecreator.sh with no arguments tells you what you need to know.

```
Takes a text file with blocks of text separated by whole blank lines and turns it into a %-delimited fortune file and a corresponding dat file.

Usage: ./fortunefilecreator.sh inputfile outputfile

Example:
 ./fortunefilecreator.sh brc.txt bobross
Output: bobross bobross.dat
Usage: fortune /path/to/bobross
```
