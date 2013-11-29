orgmode2json
============

A simple [orgmode](http://orgmode.org/) to [JSON](http://json.org/)
converter. It is most useful to work with tagged notes, but not any other
stuff (so far).

format
------
* top level
** "self-description": a string usually containing "orgmode dump"
** "entries": an array of orgmode entries
* entry
** "content": an array of the text content/lines
** "tags": an array of tags associated with the content
** "subentries": an array of entries at a lower level