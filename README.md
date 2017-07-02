Make gradients between 2 files unique to overcome an annoying Inkscape bug
which can make gradients change aspect when you copy an object between two
files, just because there is another gradient in the destination file with
the same stop colours.

# NAME

inkgrad - Make gradients between 2 files unique

# SYNOPSIS

`inkgrad [-h] INSVGFILE INSVGFILE OUTSVGFILE`

# OPTIONS

`-h, --help`
:   Show help message and exit.

# USAGE

In some circumstances I don't really understand, the Inkscape bug still
tampers with the gradient and you may want to make a group of the object
you're importing to be on the safe side.
