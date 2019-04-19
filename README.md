Log-Analysis Project
### by Chadrapal Singh Sai Charan Singh

## Project Description:
A reporting tool that prints out reports (in plain text) based on the data in the database
### Questions to Answer:
1. **What are the most popular three articles of all time?**
2. **Who are the most popular article authors of all time?** 
3. **On which days did more than 1% of requests lead to errors?**
## Project contents
* analysis.py - main file to run this Log Analysis Reporting tool
* README.md - instructions to install this reporting tool
* Output.txt - output file that will shown on the command prompt
## Required

1. Python
2. Vagrant
3. VirtualBox


## How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/Log_analysis`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```

  3. Copy the newsdata.sql file and place inside `vagrant/Log_analysis`.

  4. In terminal Change directory to `vagrant/Log_analysis`.

  5. Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
   6. Run analysiss.py using:
  ```
    $ python analysis.py
  ```



