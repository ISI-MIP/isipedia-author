---
title:  'This is the title: it contains a colon'
author:
- name: Author One
  affiliation: University of Somewhere
- name: Author Two
  affiliation: University of Nowhere
keywords: [nothing, nothingness]
abstract: |
  This is the abstract.

  It consists of two paragraphs.
---

# Hurricanes

## Global overview

This is a minimalistic template for an hypothetical hurricane indicator.
Hurricanes will have a number of effect throughout the world. 
In average, worldwide, they are projected to increase by {{world.time_var.get("2081-2100", "rcp85") | round(1)}} by the end of the century.

In that scenario, the three most affected countries will be:
- 1st: (ranking-area: time_var order: 1 value: name time: 2081-2100 scenario: rcp85)
- 2nd: (ranking-area: time_var order: 2 value: name time: 2081-2100 scenario: rcp85)
- 3rd: (ranking-area: time_var order: 3 value: name time: 2081-2100 scenario: rcp85)

## Detailed results

`{%if country.name != world %}`
{{country.name}} is the (ranking-value: time_var value: position time: 2081-2100 scenario: rcp85) most-affected country out of the (ranking-value: time_var value: total time: 2081-2100 scenario: rcp85) countries considered.
`{%endif%}`

Results:
<table>
  <tr>
    <th>Variable</th>
    <th>2041-2060</th>
    <th>2081-2100</th>
    <th>2 degrees</th>
    <th>4 degrees</th>
  </tr>
  <tr>
    <th>time_var.name</th>
    <th>time_var.get("2041-2060", "rcp85")</th>
    <th>time_var.get("2081-2100", "rcp85")</th>
    <th>temp_var.get(2)</th>
    <th>temp_var.get(4)</th>
  </tr>
</table>

    (line-plot: time_var,temp_var first-time: 2041-2060 2 first-scenario: rcp60 second-temperature: 2)

## Authors 

The data presented here was originally published by bla bla bla, literature reference and adapted to the isipedia platform by bla bla bla.

Note that although the methods and main results were presented in a peer-reviewed journal, the original publication focused on a global analysis, so that not all 200+ countries have been reviewed individually. 
ISIpedia provides data on country level for convenience, but cannot be held responsible for any issues with the data. Please contact the authors (author@contact) for more information.
