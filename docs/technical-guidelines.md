---
title: Technical Guidelines
subtitle: Guidelines to prepare data and figures for authors of ISIpedia articles
date: 30 March, 2020
author: Editorial Team of ISIpedia
---

See the [Guidelines for authors of ISIpedia](../for-scientists/) articles for a general introduction.

### Technical guidelines to prepare data and figures

Data and code requirements for authors depend on the type of contribution to ISIpedia, and will be determined based on exchanges with the editorial team. The bottom line is, the authors need to provide us with all the necessary material to produce the figures and present quantitative data in the reports.

#### Simple article
For a simple article with static figures (i.e. not interactive), there is very little requirement, though we might ask you to edit the figure labels and fonts for editorial purposes. In some cases, we might ask you for the scripts and underlying data so that we can perform the necessary adjustments.

#### Article with interactive figures
For articles with interactive figures, the underlying data must be provided to elaborate the figures. See [Data Formats](#data-formats), [Public data policy](#public-data-policy), and [Gallery](#gallery-for-interactive-figures) sections for more details.

#### Global study with country-level articles
Global studies that wish to offer a locally detailed view of the data are encouraged to do so. We provide support to break down the data to country-level, and to generate articles with [country-dependent numbers and figures](#technical-template-jinja2-to-insert-country-dependent-data-in-the-text). The drought article is an example for this.

Depending on the nature of the data and processing steps involved, we can take over the process of aggregating the [data](#data-formats) at country level according to our [country masks](#country-masks), or the authors can provide [a script](#author-script) to generate country-level data from global data.

#### Data formats
Reports will be eventually written in markdown format, which can be readily converted to HTML and PDF.

Figures will be elaborated by us based on the data you provide. We prefer to work with `netCDF`, `json` or `csv`. Please reach out to us if you wish to use other formats. The data should precisely describe what needs to be shown.

Global data should be provided on the ISIMIP grid:
```
- lat: 90 to -90 (inverted)
- lon: -180 to 180
- resolution: 0.5 degrees
- shape: ("lat": 360, "lon": 720)
```

#### Author script
The author script is intended for global data that needs to be broken down at country level. The script takes a [country mask(s) file](#country-masks) as input, and output country-level data. The output shall preferably be web-compatible `json` or `csv` format. It can then be used directly in the corresponding country report via our [templating system](#technical-template-jinja2-to-insert-country-dependent-data-in-the-text).

Input data is generally user-provided netCDF file(s) or an ISIMIP file already present in the portal. Using raw ISIMIP data as input may be more efficient rather than providing and storing Gigabytes of data, provided the post-processing is not computationally-intensive.

We prefer python because that is the language we use and we can offer technical support there, but we can possibly accept other languages as well. Please reach out to us if you are in doubt or if you require assistance to elaborate the script.

Example `authorscript.py` in python:
```python
import os
import json
import netCDF4 as nc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('masks') # countrymasks.nc
parser.add_argument('--country') # restrict calculations for one country
parser.add_argument('--out-dir', default='out')

o = parser.parse_args()

ds = nc.Dataset(o.masks)

if o.country:
  variable = 'm_'+o.country
  if variable not in ds.variables:
      raise ValueError(o.country + ' is not present in ' + o.masks)
  variables = [variable]
else:
  variables = [v for v in ds.variables if v.startswith('m_')]

# load user-provided or ISIMIP-input data
input_data = load_input_data()

for v in variables:
    country_code = v[2:] # remove leading `m_`
    mask = ds[v][:] > 0  # for a binary mask
    country_data = ... agreggate input data on country mask

    output_dir = os.path.join(o.out_dir, country_code)
    output_file = os.path.join(output_dir, 'data.json')

    os.makedirs(output_dir, exist_ok=True)
    json.dump(country_data, open(output_file, 'w'))

ds.close()
```
Such script would be called as: `authorscript.py countrymasks.nc`

#### Country masks
Country masks exist in two forms:
- binary masks (0 or 1, integer-based): https://gitlab.pik-potsdam.de/isipedia/countrymasks/blob/master/countrymasks.nc
- fractional mask (anywhere between 0 and 1, float-based): https://gitlab.pik-potsdam.de/isipedia/countrymasks/blob/master/countrymasks_fractional.nc
It is up to the author to decide what is more relevant for the study.

You may download the file(s) for investigation. In short, the file contains the dimensions `lon` and `lat` and each country mask is a separate variable named by the country ISO3 code preceded with `m_` , such as `m_AFG` for Afghanistan. Note that latitude `lat` is inverted (see [Data Formats](#data-formats) sections).

Note the data may undergo periodical updates to solve issues. If an update affects an already published study, the author will be notified, or contacted beforehand for approval, depending on the scale of the update.

#### Technical template (jinja2) to insert country-dependent data in the text
For the authors who desire to insert country-dependent data and numbers in the text, such as in the drought example, we provide a templating system based on jinja2, to produce country-specific markdown files.

The templating system gives access to country data as generated by the [author script](#author-script), and to execute simple instruction in python within the text. For instance, if the json file `data.json` is present in the report directory, it will be made available as python variable from within the article template with double braces `{{ data }}` or `{{ data[field] }}` using typical python syntax.

A number of other functions are provided, such as figure insertion and data-access for isipedia-specific formats, which will be documented over time.

That said, please be reminded of the editorial guidelines to write article from humans to humans (see [general author guidelines](#guidelines-for-writing-an-isipedia-article)), without abusing of automatically-generated, unchecked numbers. Adding numbers this way is NOT a requirement, and one might argue that it is even a BAD idea, as it is not possible to ensure a thorough quality control of 200+ countries, and it may make it difficult to separate what is written by a human and what is generated automatically. Note that a **dedicated text box for key numbers** might be a good option to increase clarity.

#### Gallery for interactive figures

Example figures can be found by browsing existing articles.
As we are at an early stage of the public phase of the project, few example are available. Note that we are open to experimenting with interactive visualization. For inspiration, you might go and have a look at D3 gallery: [d3js.org](https://d3js.org).

#### Public data policy

The data provided to us to make the interactive figures will normally be made available for public download along with the figure in the article, unless explicit request not to do so. Note that we make no effort to hide the data so anyone technically able can retrieve them from the HTML/web requests.
