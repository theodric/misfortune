# misfortune
If you're looking for new fortunes for fortune, then it's fortunate that you've stumbled on this repo!

![fortune | cowsay | lolcat](https://github.com/theodric/misfortune/raw/master/misfortune.png)

* bobross: the contents of http://www.bobrossquotes.com/quotes.shtml in fortune form
* jennyholzer: a collection of quotes from [notable quotable neo-conceptualist artist Jenny Holzer](https://en.wikipedia.org/wiki/Jenny_Holzer), of large scrolling LED sign installation fame. These quips were found in various places around the Internet, and are presented here for your confusion. If you've been through Amsterdam Schiphol airport in the last 22 years, you probably saw at least [one of her pieces](https://www.youtube.com/watch?v=6IGEoVJG39Y) there.
* randomquotes: if this directory exists, then it contains random quotes that I like. If not, then I haven't gotten around to creating it yet.

Also of note in this repo is ```fortunefilecreator.sh```.
In case you couldn't guess, it creates fortune files. It's nothing special, or particularly good, but it does the job. I'm sure you can do it better: please do; I stop caring once it works. :shipit:

You feed it a text file with fortunes separated by empty lines containing linefeeds (just LF, not CRLF-- we're on UNIX, eh buddy?) and it spits out the %-delimited fortune file and runs strfile to create the requisite .dat.

Your input text file needs to look like this:

```
Alienation produces eccentrics or revolutionary.

Savor kindness because cruelty is always possible later.

In a dream you saw a way to survive and you were full of joy.
```

Running ```fortunefilecreator.sh``` with no arguments will also tell you what you need to know.

```
Takes a text file with blocks of text separated by whole blank lines and turns it into a %-delimited fortune file and a corresponding dat file.

Usage: ./fortunefilecreator.sh inputfile outputfile

Example:
 ./fortunefilecreator.sh brc.txt bobross
Output: bobross bobross.dat
Usage: fortune /path/to/bobross
```

You'll probably want to install ```fortune``` so that you have ```strfile``` installed, because you'll need it to create the dat file. Also because none of this is of much use to you without ```fortune``` installed to, you know, display the fortunes.
If you're on OSX, I recommend https://github.com/johnpneumann/Fortune-OSX

Additionally, you'll need GNU ```sed```, and not that BSD :poop: that OS X ships with. Linux users will be fine; for Macs, ```brew install gnu-sed --with-default-names``` will sort you out. BSD people are on their own, but you're probably used to that by now. :neckbeard:

Incidentally, I recommend checking the output file after you run the script just to confirm that everything is sane, i.e. no missing % (there needs to be one under each fortune) and no blank lines with a % under them (because that will result in a blank fortune). You can clean this up in a text editor, then run e.g. ```strfile bobross bobross.dat``` to regenerate the dat file.

# Thanks
Thanks to bradthemad for [his page](http://bradthemad.org/tech/notes/fortune_makefile.php) showing me what needed to be done.

Thanks to johnpneumann for [Fortune-OSX](https://github.com/johnpneumann/Fortune-OSX).

