# fortune
If you're looking for new fortunes for fortune, then it's fortunate that you've stumbled on this repo!

* bobross: the contents of http://www.bobrossquotes.com/quotes.shtml in fortune form
* jennyholzer: a collection of quotes from notable quotable neo-conceptualist artist Jenny Holzer, of large scrolling LED sign installation fame. If you've been through Schiphol airport in the last 22 years, you probably saw at least one of her pieces there. Collected from around the Internet.
* randomquotes: if this file exists, then it contains random quotes that I liked. If not, then I haven't gotten around to creating it yet.

Also of note in this repo is fortunefilecreator.sh
In case you couldn't guess, it creates fortune files. It's nothing special, or particularly good, but it does the job. I'm sure you can do it better: please do; I stop caring once it works. :shipit:

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

You'll probably want to install fortune so that you have 'strfile' installed, because you'll need it to create the dat file. Also, these aren't of much use to you without fortune installed.
If you're on OSX, I recommend https://github.com/johnpneumann/Fortune-OSX

Incidentally, I recommend checking the output file after you run the script just to confirm that everything is sane, i.e. no missing % (there needs to be one under each fortune) and no blank lines with a % under them (because that will result in a blank fortune).

# Thanks
Thanks to [bradthemad](http://bradthemad.org/tech/notes/fortune_makefile.php) for showing me what needed to be done.
Thanks to johnpneumann for [Fortune-OSX](https://github.com/johnpneumann/Fortune-OSX).
