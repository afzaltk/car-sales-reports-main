# car-sales-reports

Car sale sample report project

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://gitlab.com/-/experiment/new_project_readme_content:9c73c2e1aaef63e4451ef6727c8d7f00?https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://gitlab.com/-/experiment/new_project_readme_content:9c73c2e1aaef63e4451ef6727c8d7f00?https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://gitlab.com/-/experiment/new_project_readme_content:9c73c2e1aaef63e4451ef6727c8d7f00?https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/Assiduz/car-sales-reports.git
git branch -M main
git push -uf origin main
```

## Use Case:
To generate reports to measure and track conversions metrcis of the products.

### Reports:
1. Report Number of page views aggregated by day
2. Report Number of purchases by day
3. % Report conversions by the day. Conversion = Number of purchases / page views 
4. % Revenue Conversion by the day. Revenue Conversion =  Total Purchase Amount / pageviews 

#### Source data: 
The location of the source data is in resource folder. However this has to be modified in future to include various data sources such as S3, HDFS etc...

1. weblog.txt_ : 
   1. Web log for page views
   2. Location : /resources/input/weblog.txt
2. transactions.csv : export of transactions events
   1. Transaction data from database
   2. Location : /resources/input/transactions.csv

#### Output data: 
The location of the output data is in resource folder as csv file. However this has to be modified in future to include various data sources such as S3, HDFS etc...

1. revenue_report.csv : 
    1. Location : /resources/output/revenue_report.csv


## License
Proprietary Software License
