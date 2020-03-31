---
title: Example Ice Cream Article
author:
- name: Some One
  affiliation: 1
- name: Some Two
  affiliation: 2
institution:
- Nowhere Institute for Advanced Icecream Studies, Potsdam, Germany
- Somewhere Institute, Berlin, Germany
area:
  code: EUU
  name: European Union
studytype:
  code: example-studytype
  name: New Example Studytype
indicator:
  code: example-icecream
  name: Ice-Cream
topics:
- code: water
  name: Water
- code: biodiversity
  name: Biodiversity
ranking:
published: 29 February 2020
doi:
panflute-verbose: true
beta: true
---

### Introduction

This is not actually an article about ice-cream, but a demo of available features.

### Embedded figures

This is ice-cream production in the EU.

![Ice-cream production in the EU in 2018](figures/icecreamproduction.vl.png){#fig:icecreamproduction}


Another figure of Potsdam temperatures (Source: [DWD](https://www.dwd.de/DE/leistungen/klimadatendeutschland/klimadatendeutschland.html))

![Temperature measurements in Potsdam](figures/temp_potsdam.vl.png){#fig:temp_potsdam}


### Key findings

A list of scoops we want

- strawberry
- oat milk chocolate
- banana-peanut-butter

A formula can describe a mathematical relationship:

$$ \textrm{Price}_{total} = p \times \sum_1^n\textrm{Scoops} $$

Inline math, like $H_n^3$, is also possible.

Formulas can also be numbered:

$$ \textrm{Price}_{total} = p \times \sum_1^n\textrm{Scoops} $${#eq:ice-price}

As you can see, in equation @eq:ice-price, three scoops are enough.

Below a regular figure from a PNG-file.

![This is a regular PNG](figures/plot.png){#fig:regular-png}

### Data sources

We can also write tables in Pandoc's [table syntax](https://pandoc.org/MANUAL.html#tables).

Date     TMM   RND
------ ----- -----
201909  14.9  14.1
201908  21.0  20.0
201810  11.2  12.5
201809  16.7  16.2
201808  21.4  23.1
------ ----- -----

Table: Selected Temperature Data for station 10379 from DWD {#tbl:temp_data}

### Embedding a video

Embedding a video is isi, it's isi mobisi!

<https://www.youtube.com/watch?v=Wf0Z4sZe0_E>

### Extensions

If desired it is also possible to experiment with extending the linear article format with elements e.g. available in the Bootstrap framework used in the site, like tabs:

<ul class="nav nav-tabs">
<li class="nav-item"><a class="nav-link active" data-toggle="tab" href="#simple">Simple</a></li>
<li class="nav-item"><a class="nav-link" data-toggle="tab" href="#advanced">Advanced</a></li>
</ul>

<div class="tab-content">
<div id="simple" class="tab-pane active">

##### Simple Content

Adding two numbers:

$$ 1 + 1 = 2 $$

</div>
<div id="advanced" class="tab-pane">

##### Advanced Content

And now multiplying two numbers:

$$ 1 \times 1 = 1 $$

</div>
</div>

In the PDF these tabs will be rendered one below the other and could be used to display multiple figures.


### D3 Figures

D3 is also readily available (though might require considerations for the PDF where the D3 visualisation would not appear).

<div id="d3-test"></div>

### Web-only

It might be desirable to have some content only in the web-version.

<div class="d-print-none">
This paragraph will not appear in the PDF (or when using Bootstrap's print template, as it is wrapped in a div and has the class `.d-print-none`).
All elements with this class are removed in the `update-latex-pdfs.py` filter.
</div>

This sentence will appear again both in the web as well as the PDF version.

### Conclusions

What is [anthropogenic climate change](/glossary/#anthropogenic-climate-change)?

There are many terms which we can look up in the glossary or see a preview with mouseover.
There is [climate variability](/glossary/#climate-variability) and there is something about [ISIMIP2b](/glossary/#isimip2b).

And we cite a paper [@Wartenburger_2018_gd8vft] and another [@Doell_2015_f8fjrd].

We can also show that @Wartenburger_2018_gd8vft wrote a paper.

In figure @fig:icecreamproduction you can clearly see that we can reference figures.
In figure @fig:temp_potsdam you can see data from table @tbl:temp_data
and figure @fig:regular-png you can see something else.

### References
