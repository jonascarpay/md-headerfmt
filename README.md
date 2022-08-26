# md-headerfmt

Formatter for markdown headers to make reading and writing markdown in your editor less painful.

Automatically styles all level 1 and 2 headers using = and - underlines of the correct length.

```markdown
# Hello
## World
```
becomes
```markdown
Hello
=====
World
-----
```

Additionally, the first headers of their respective type indicate the desired padding.

```markdown
  Hello
===
# World
Foo
---
  Bar
------
```
becomes
```markdown
  Hello
=========
  World
=========
Foo
---
Bar
---
```

## Usage

Reads a file either from `stdin` or as a command line argument.
Results are printed to `stdout`.
