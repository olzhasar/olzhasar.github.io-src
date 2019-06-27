Title: Visual statistics
Date: 2017-11-03
Tags: python, flask, pandas, javascript, chart.js
Slug: visual-statistics
Cover: projects/img/statkz-home-0.jpg
Github: https://github.com/olzhasar/statkz-old
Summary: Website for displaying different statistical data of Kazakhstan in graphical format.

Data for this website was obtained from official governmental statistics agency's website. The raw file was in .xls format and contained a lot of "dirty" values with unexpected characters in number cells, etc. I used xlrd python library to extract data from the file row by row and applied regular expressions for cleaning. Processed data was written to a new file that was further imported to pandas for final modifications and exporting to HDF5 format to use in production. HDF format showed superior performance compared to SQL databases and served well as data wasn't modified by users of this website. Final web application was based on Flask microframework and used open source Bootstrap admin template.

This is my personal side project. I was the only developer.
