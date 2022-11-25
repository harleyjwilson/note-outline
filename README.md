# Note Outline

This is a tool to help create an outline from notes in your zettelkasten. 

Let's say you have three notes, stored as individual markdown files.

```202211250910 First Note.md
# 202211250910 First Note

This is the text of my first note.
```

```202211251045 Second Note.md
# 202211251045 Second Note

This is the second note made.
```

```202211251152 Third Note.md
# 202211251152 Third Note

And finally, this is my third note.
```

I create an outline of what I want to write (essay, blog post etc) which links to these notes in the wiki link format.

```202211251217 Outline.md
# 202211251217 Outline

This is the outline of my blog post.

I started here [[202211250910]] first.

I let that sit a little.

Then I wrote my second [[202211251045]] and third [[202211251152]] note.

We are now at the end.
```

To being those notes into my outline for quick reference I can use note_outline to give the following result

```202211251378 Draft.md
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