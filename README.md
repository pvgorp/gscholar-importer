# gscholar-importer
Quick hack to pull from Google Scholar the author pages/pictures and basic citation/h-index data.

Use case: you are organizing a scientific workshop and you have received only basic information from the last year's programme committee. You want to pull more information from Google Scholar to analyze efficiently the academic track record of the PC members.

## Assumed input

First name | Last name | Email | Invited 2023? | Affiliation | Role
---|---|---|---|---|---
Pieter | Van Gorp | p.m.e.v.gorp@tue.nl | n | Eindhoven University of Technology | Main Track
Raoul | Nuijten | r.c.y.nuijten@tue.nl | n | Eindhoven University of Technology | Main Track
Serge | Demeyer | serge.demeyer@uantwerpen.be | y | University of Antwerp | Keynote

Note: this MD table was generated by applying csv2md (installed from npm) on in.csv from this repository.

## Example output

First name | Last name | affiliation | citations | scholar_page | url_pic | citationsAll | citations5Y | hIndexAll | hIndex5Y | keywords
---|---|---|---|---|---|---|---|---|---|---
Pieter | Van Gorp | Eindhoven University of Technology | 3363 | https://scholar.google.com/citations?user=uMc_GTcAAAAJ | https://scholar.google.com/citations?view_op=medium_photo&user=uMc_GTcAAAAJ | 3363 | 830 | 22 | 14 | Model Driven Engineering;Health Data Platforms;Workflow Management;mHealth;
Raoul | Nuijten | Eindhoven University of Technology | 62 | https://scholar.google.com/citations?user=vGLIFCsAAAAJ | https://scholar.google.com/citations?view_op=medium_photo&user=vGLIFCsAAAAJ | 62 | 62 | 5 | 5 | health;behavior change;persuasive technology;
Serge | Demeyer | University of Antwerp | 10764 | https://scholar.google.com/citations?user=YWYJU9MAAAAJ | https://scholar.google.com/citations?view_op=medium_photo&user=YWYJU9MAAAAJ | 10764 | 2788 | 51 | 25 | Software Engineering;Software Evolution;

## Installation on OSX:
* sudo python3 -m pip install jupyter notebook -U
* sudo pip3 install ipykernel
* Restart vscode

