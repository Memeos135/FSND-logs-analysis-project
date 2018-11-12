# Project Title

This project focuses on equipping enrolled students with excellent basic SQL query writing skills. The project requires students to perform (3) complex SQL queries to retrieve information from a ready-built database called "news".

### Prerequisites

Those who plan to undergo the project will have to install and setup a few things before starting the actual project. These include:

```
1) VirtualBox
2) Vagrant
3) Git
4) Pycodestyle
```

### Installing 1.0

In this section, a step-by-step installation guide of the prerequisite softwares mentioned above.

<b>First</b>, Git Bash will be used as our CLI (command line interface) to query and view the PostgreSQL - psql - database provided to us, "news",  from within the virtual machine environment. Find the link below to download Git Bash:

```
https://git-scm.com/downloads
```

<b>Second</b>, Oracle VirtualBox for Windows must be downloaded and installed. The following link is the webpage for downloading the software.

<center><b>Do not configure anything in the VirtualBox Manager</b>.

```
https://www.virtualbox.org/wiki/Downloads
```
<br>
<b>Third</b>, download and install Vagrant. Please find the link below:
After installation, verify functionality by launching Git Bash and typing <b>vagrant --version</b>.
```
https://www.vagrantup.com
```

<b>Fourth</b>, Pycodestyle will have to be installed to "beautify" your python code.
<center><b>(Optional)</b>

Type the following command in Git Bash:
```
pip install pycodestyle
pip install --upgrade pycodestyle
```

You might have to append the path of Pycodestyle to your $PATH environment variable. Please type in the following commands in Git Bash to do so:

```
nano .bash_profile
export PATH = "YOUR/PYCODESTYLE/PATH:$PATH"
Ctrl + O
Enter
Ctrl + X
```

In the above commands, YOUR/PYCODESTYLE/PATH refers to the path you've installed Pycodestyle in.
Verify the addition of Pycodestyle by launching Git Bash and running the following command:

```
echo $PATH
```
If the newly appended path exists, you've successfully added the pycodestyle path. Otherwise, review the steps above.
### Installing 2.0

Once you've completed the above and verified the functionality of Vagrant and Git Bash PATH appending, you'll have to set up the "news" database. Please do so by performing the following:

<b>First</b>, download the following file and unzip it to a directory you prefer:

```
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
```
<b>Second</b>, launch Git Bash and <b> cd </b> to the directory you've unzipped the file into.

<b>Third</b>, once in the designated directory, type the following command from within Git Bash:
```
vagrant up
```
<center><b> Caution </b>

Upon running the command above, you might receive a few errors. In order to avoid all errors, you'll have to disable <b>Hyper-V</b> and enable <b> Intel Virtualisation</b>.
However, enabling <b>Intel Virtualisation</b> will have to be accessed via the <b>BIOS Boot Menu</b>. <br><br>You can disable <b>Hyper-V</b> by following the link below. Additionally, <b>vagrant up</b> process can take up to 5 minutes.

```
https://ugetfix.com/ask/how-to-disable-hyper-v-in-windows-10/
```

<b>Fourth</b>, once vagrant up has been set and complete, you can log into the environment through the following command in Git Bash:
```
vagrant ssh
```

<b>Lastly</b>, once logged in, you'll have to create the news table by running the following command Git Bash @ Vagrant:

```
psql -d news -newsdata.sql
```

<b>Once completed</b>, the following commands can be used to view the properties of each table defined in the news database:

```
\d
\dt
```

## Completing the Project

The project asks students to find information regarding (3) questions by querying the database tables.

<b> (1) </b> What are the most popular three articles of all time? <br>
<b> Sample Output: </b>
<br>
* "Princess Shellfish Marries Prince Handsome" — 1201 views
* "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
* "Political Scandal Ends In Political Scandal" — 553 views

<b> (2) </b> Who are the most popular article authors of all time? <br>
<b> Sample Output: </b>
<br>
* Ursula La Multa — 2304 views
* Rudolf von Treppenwitz — 1985 views
* Markoff Chaney — 1723 views
* Anonymous Contributor — 1023 views

<b> (3) </b> On which days did more than 1% of requests lead to errors? <br>
<b> Sample Output: </b>
* July 29, 2016 — 2.5% errors

## Authors

* **Mohammed Bokhari** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
