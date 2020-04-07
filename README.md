# Author template directory

## Overview

- [template.md](template.md) for a general template focused on text structure.
- [technical-guidelines.md](technical-guidelines.md): technical guidelines to prepare data, figures and markdown text
- [examples](examples) for more diverse examples.
- [data](data): country masks (for testing)
- [authorscript.py](authorscript.py): author script template

## Metadata

Please indicate metadata (title, author) in the header of your article, such as:
```
---
title: Example Article Title
reference: https://doi.org/10.1029/2019EF001181
author:
- name: Some One
  affiliation: 1
- name: Some Two
  affiliation: 2
institution:
- Institute for Advanced Studies, Potsdam, Germany
- Another Institute, Berlin, Germany
area: world
studytype: future-projections
topics:
- water
- something-else
---
```

## Markdown syntax

The template use [pandoc markdown](https://pandoc.org/MANUAL.html#pandocs-markdown).
That is simple text with conventions for headings, hyperlinks, references and so on.

Below an overview of the most important conventions:

```markdown

## Section title

### Subsection

[link text](actual-link-address)

![caption](figures/image.png){#fig:ref}

*italic* **bold**

`code`

    Code block
    can be indented 
    using 4 spaces 
    
    ```Or 3-quoted like this even 
    without indentation```

> quote

Item list:
- first item
- second item

Numbered list:
1. One
2. Two
```
Additionally we support **bibtex references**:
```markdown

[@Gerten_2014_Cross; @Prudhomme_2013_f5wdwd; @Doell_2015_f8fjrd; @Kuzyakov_2019_gf43bp]
``` 
and **glossary links** to be included as hyperlink as 
```markdown
[climate models](/glossary/#climate-models)
```

We can also have HTML code as well as javascript code for more advanced, interactive content.

## Inject data into the articles

We use `jinja2` templates with `{{ ... }}` and `{% if ... %} ... {% else %} ... {% endif %}` syntax if we need logic in the templates, and to connect country-specific data and figures with the articles. This should be used with caution. More information in the [technical guidelines](technical-guidelines.md#technical-template-jinja2-to-insert-country-dependent-data-in-the-text).


## About the template

The [template](template.md) is intended to provide authors with a reference to draft
their ISIpedia articles, both in terms of structure and suggested texts
as well as to prepare the graphical materials. We encourage authors
planning to write text articles to contact the Editorial Team in the
first place (*Barbara Willaarts, Jens De Bruijn, Barbara Templ and Mahé
Perrette via* <isipedia.editorial.team@pik-potsdam.de>) to have a
pre-discussion on the topic, type of contributions, etc.

Following the initial discussion, and if the author would like to
prepare a text article, we recommend the author to use this template,
although its use is NOT compulsory. Authors experienced in science
communication are encouraged to develop free-format articles, under the
premises that:
1. the resulting text complies with the [guidelines for
authors](https://demo.isipedia.org/for-scientists/) as described in the
ISIpedia portal; and
2. the authors carefully read and follow the instructions on how to prepare the graphical materials (see [Technical guidelines](technical-guidelines.md).

ISIPedia articles can be divided into two broad categories: 
1. individual contributions e.g. country-based studies, and 
2. global contributions with gridded information that can be further breakdown
into national reports. 

Authors aiming to prepare the latest type of
articles should bear in mind that a given number of sections will remain
the same across all national reports, namely sections on (see [template.md](template.md)
for details):
1. How to interpret the results; 
2. limitations and knowledge gaps; 
3. data and methods, and 
4. references.

Only the key messages section, as well as the main findings, will be adjusted to each
country and global report.

*NOTE: ISIpedia contributions are not just restricted to text articles.
We also welcome other types of contributions such as infographics, video
interviews, etc. Authors willing to provide contributions other than
written articles please contact the editorial team.*
