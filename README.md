# isipedia-author
Template for an author package, as optional helper tool for authors to write an isipedia article.

## Introduction

For an article to be published on ISIpedia, the report and associated data must be arranged according to our data cube structure, 
described in detail in the [data cube manual](#cube-manual), and briefly summarized below.
The aim of the isipedia-author repository is to help you bring your data into the required form with minimal effort, 
re-using code for data processing (e.g. country averaging) 
and providing you with a [templating system](#templating-system) to provide with country-specific 
and world numbers with a single or a few templates.
We encourage you to use this system but you may also use your own code to generate the country-specific markdown reports. 


## Technical requirements for a study: the data cube structure

Let us assume the study indicator is called 'drought', with categories 'present-days' and 'future-projections'. 
The following directory structure is required to be technically displayed on the website:

    drought/
        config.json
        future-projections/
            AFG/
                drought-AFG.md
                ranking-data_AFG.json
                other-ranking-data_AFG.json
                ... (other files that may be needed by drought-AFG.md, such as figures to be inserted)
            world/
                drought-world.md
                ... 
            ... (other countries)
        present-days/
            ... (same structure as future-projections)

The [config.json file](#config-file) contains information such as indicator name, categories (here future projections and present-days) and [ranking](#ranking).
The reports themselves (drought-AFG.md and drought-world.md in the example above) are written in [markdown format](#markdown-format) as described below. 
The directories contain other data files that may be invoked by the markdown files to render into valid HTML report pages.

"drought" on this example is one of multiple indicators on the isipedia [data cube](#cube-manual).


### Config file

- The configuration file config.json has the following structure:
 
    ```
    {
      "name": "Drought",
      "topics": [ "Extreme events", "Water" ],
      "study-types": [
        {
          "directory": "future-projections",
          "description": "projections of Earth's possible futures under climate change",
          "ranking-files": {
            "land-abs-temp": {
                "direction": "desc"
            },
            "land-abs-time": {
              "direction":"desc"
            },
            "pop-abs-temp": {
              "direction": "desc"
            },
            "pop-abs-time": {
              "direction": "desc"
            }
          }
        }
      ]
    }
    ```

TODO: Note that could be written in a more concise manner in equivalemnt yaml format:

    name: Drought
    topics: 
        - Extreme events
        - Water
    study-types:
      - directory: future-projections
      - name: Future Projections
      - description: projections of Earth's possible futures under climate change
      - ranking-files: 
        - land-abs-temp: 
            - direction: desc
        - land-abs-time:
            - direction: desc
        - pop-abs-temp:
            - direction: desc
        - pop-abs-time:
            - direction: desc

## Markdown format

They may include typical markdown commands (e.g. insert figure) and 
custom-markdown-commands (e.g. make a [line plot](#line-plot) and [country ranking](#country-ranking)).

Markdown commands are things like `(link: glossary/climate-change text: Climate Change)`.
Markdown commands are described in the [cube manual](#cube-manual).

### Line-plots

Line plots require 1-d data to be arranged into a specific [cube json format](#cube-json-format)
See details in the [cube manual](#cube-manual).

### Country ranking

TODO: Provide some explanation about country ranking.

Country ranking are accessed via a special [markdown command](#markdown-commands), for instance:

 - `(ranking-value: temp-var_PAK value: position temperature:2)` : get position of `PAK` country for `temp_var` variable (`temp-var_PAK.json` file), for 2 degrees warming.
 - `(ranking-value: time-var_PAK value: position time:2041-2060 scenario: rcp26)` : idem, for `2041-2060` time slice under `rcp26` scenario
 - `(ranking-area: time-var order: 1 value: name temperature:2)`: inverse operation: country name that comes in first position (`order:1`) for `time_var` variable (`time-var_AREA.json` files) under 2 degrees warming.
 
See details in the [cube manual](#cube-manual).


### Cube json format

This is a special json format recognized by custom markdown commands for line plot and country ranking.
If you do not use these features, you do not need to follow this syntax.

See details in the [cube manual](#cube-manual).


## Cube manual

Most of what is described here can be found in greater details in the [cube manual](https://github.com/ISI-MIP/isipedia-author/raw/master/docs/data-cube-manual-3.1.0.pdf).

## Templating system 

This system is based on jinja2 and allows you to generate country-specific reports from one generic template.
Following this system, markdown files for country reports are the result of a multi-step process.

* Markdown [templates](templates) are edited by authors, which contain [jinja2 patterns](#template-patterns), as well as [markdown commands](##Markdown-commands).

* A [python script](textgenerator.py) transform the templates:
  - check for the presence of relevant [template files](#template-files) 
  - process the templates and fill in the [jinja2 patterns](#template-patterns), 
based on `json` files such as present in [test-data](test-data), and produce a markdown file for each region. 
At this stage the regional markdown file still contains [markdown commands](#markdown-commands). 

* The javascript engine processes the [markdown commands](#markdown-commands) and renders each report in HTML format on the website.

### Template files

Template files are present under `templates/`. 
Any area-specific template is used in priority (e.g. `PAK` or `world`).
For example, taking `drought` in Pakistan, 
- `templates/drought_PAK.md` is used if present
- otherwise `templates/drought.md` is used.

This also applies for the `world` region.


### Template patterns

These are variables in double curly braces `{{...}}`. Here are some of the most common patterns:
- `{{time_var.get('2041-2060', "rcp26")}}` : `time_var` variable for `2041-2060` time slice under `rcp26` scenario 
- `{{temp_var.get(4)-temp_var.get(2)}}` : `temp_var` variable, difference between 4 degree and 2 degree warming
- `{{temp_var.getall(4)|max}` : get a list of all climate and impact model results for 4 degree warming, and keep the maximum
- `{{temp_var.get(4)|round(0)|int}` : get standard (median) value, then use jinja filters to round to 0 decimals and convert to integers 
- `{{rel_var_pct.get(4)/100 + 1}` : transform a variable expressed as relative change (%) into a factor
- `{{world.temp_var.get(4)}` : access to `temp_var` variable from the `world` folder
- `{{time_var.climate_model_list | length}}` : length of climate model list for that variable

`time_var` and `temp_var` variables are examples of template variables, assuming the files `time_var.json` (or `time-var.json` or `time-var_AREA.json`) and `temp_var.json` are present in the country (or world) directory, but any variable name is valid. For instance, if a file `pop-abs-time_PAK.json` is present in the `PAK` directory, 
then the corresponding variable is available to the author as `pop_abs_time` (`-` becomes `_`), 
so that `{{pop_abs_time.get("2041-2060", "rcp26")}}` is valid syntax. 

Note that in order to use [country ranking](#country-ranking), the file name must end with `_AREA.json` where `AREA` is the country code name (or `_world`).

Additionally, country information are available through the special variable `country`, e.g.
- `{{country.name}}` : country name
- `{{country.nameS}}` : Pakistan's or Wales' (handle the final s)

See below for [more advanced information](#variable-methods-definition-advanced) on variable methods. 
 
### Variable methods definition (advanced)

- `variable.get(x, scenario=None, climate_model=None, impact_model=None, field=None)`: single numbers, where `scenario` is required when `x` is a timeslice, and `climate_model` and `impact_model` default to `median` 

- `variable.getall(x, scenario=None, climate_model=None, impact_model=None, field=None)` to return a list. In that syntax `climate_model` and `impact_model` are only necessary to filter the listing.  By default all climate and impact models are provided. The list can then be modified with `jinja2`'s pipe `|` syntax, like `| max` or `| min`. One could certaintly add `median` to calculate it on the fly, but I am not sure how the overall `median` is calculated exactly. If it is a two-step calculation such as 1) the median of all impact models for every climate model, and 2) median of medians, then the flat `list | median` approach will differ from the *nested median*.

### jinja2 (advanced)

The syntax is based on [jinja2 templates](http://jinja.palletsprojects.com/en/2.10.x/templates), but you do not need to understand all of it to create an ISIPEDIA indicator template. 

One useful pattern might be the `{%if ...%}...{%else%}...{%endif%}` clause, for instance:

   The variable is projected to `{%if temp_var.get(4) > temp_var.get(2) %}`increase`{%else%}`decrease`{%endif%}` as global mean temperature raises from 2 to 4 degrees Celsius.

## Pre-rendering

The markdown reports can be pre-rendered locally before there are moved onto the ISIpedia server.
