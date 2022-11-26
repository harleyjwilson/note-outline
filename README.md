# Note Outline

This command line tool will help create an outline from notes in your zettelkasten. 

Let's say you have three notes stored as individual markdown files.

- 202211250910 First Note.md
```
# 202211250910 First Note

My first note.
```

- 202211251045 Second Note.md
```
# 202211251045 Second Note

My second note.
```

- 202211251152 Third Note.md
```
# 202211251152 Third Note

And finally, this is my third note.
```

I create an outline of what I want to write (essay, blog post etc.), which links to these notes in the wiki link format.

- outline.md
```
# 202211251217 Outline

This is the outline of my blog post.

I started here [[202211250910]] first.

I let that sit a little.

Then I wrote my second [[202211251045]] and third [[202211251152]] note.

We are now at the end.
```

Using note_outline will output the following result.

```
# 202211251217 Outline

This is the outline of my blog post.

I started here [[202211250910]] first.
<!--
    202211250910 First Note.md
    # 202211250910 First Note
    
    This is the text of my first note.    
-->

I let that sit a little.

Then I wrote my second [[202211251045]] and third [[202211251152]] note.
<!--
    202211251045 Second Note.md
    # 202211251045 Second Note
    
    This is the second note made.    
-->
<!--
    202211251152 Third Note.md
    # 202211251152 Third Note
    
    And finally, this is my third note.    
-->

We are now at the end.
```

## Basic Use

To output the result to the terminal:
Run the following command, either in the same directory or using the absolute path, to output the result to the terminal: 

`note_outline outline.md`

To output the results to another file, run:

`note_outline outline.md -o output.md`

Or to save it in place (overriding the original file), run:

`note_outline outline.md -i`

## Clear Outline Comments

You can use the `-d` flag to remove the comments from a filled-out outline.

To output the result to the terminal:

`note_outline outline.md -d`

To output the results to another file, run:

`note_outline outline.md -d -o output.md`

Or to save it in place (overriding the original file), run:

`note_outline outline.md -d -i`

## Installation

Download this repo and open it in the terminal and run:

`pip3 install .`

## Acknowledgements

I references the [Zettelkasten Method](https://github.com/Zettelkasten-Method)'s [zettel-outline-renedering](https://github.com/Zettelkasten-Method/zettel-outline-rendering) repo for this tool. I made this to practice Python, but this repo helped with the command line layout and use of the HTML comments. 

In addition, my knowledge of the Zettelkasten Method is mostly thanks to [zettelkasten.de](https://www.zettelkasten.de); check them out. 