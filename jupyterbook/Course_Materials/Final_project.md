# Final Project

## Goals

The only way to truly master data-enabled science and engineering is to implement a workflow. This will expose you to problems that you will encounter in the real world. The goal of this project is to develop a software package that can be used to solve a problem in your field of study. This project will follow the timeline of the course. Many of the homework assignments will have you complete specific subtasks with your dataset. The final result will be a complete well-documented package. At the conclusion of the course, you will present your project to the class highlighting the impact on your subfield.

---

## Assignment Components

### GitHub Repository (40%)

For your assignment, you are required to create and manage your software development using version control on GitHub. Your repository does not have to be public but will need to be shared for grading. 

#### GitHub Repository Rubric

<!DOCTYPE html>
<html>
<head>
    <style>
        /*Apply global styles to table, th, td, and tr*/
        table, th, td, tr {
            border: 1px solid black;
            border-collapse: collapse;
        }
        /*Center the table*/
        table.center {
            margin-left: auto;
            margin-right: auto;
        }
        /*Style the header*/
        th {
            background-color: #f2f2f2;
            text-align: center;
            padding: 15px;
        }
        /*Style the cells*/
        td {
            text-align: center;
            padding: 10px;
        }
        /*Apply zebra-striping*/
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <table class="center" style="width: auto"> <!-- Changed width to auto -->
        <tr>
            <th>Topic</th>
            <th>Percentage</th>
            <th>Points Scored</th>
        </tr>
        <tr>
            <td>Code Functionality - <i>How much functionality is included in the code?</i></td>
            <td>40</td>
            <td></td>
        </tr>
        <tr>
            <td>In-code Documentation - <i>How readable is your code?</i></td>
            <td>15</td>
            <td></td>
        </tr>
        <tr>
            <td>Code Reusability - <i>How easy is it for someone to reuse and extend your code?</i></td>
            <td>25</td>
            <td></td>
        </tr>
        <tr>
            <td>Usage Documentation - <i>How easy is it for someone new to your code to use it?</i></td>
            <td>20</td>
            <td></td>
        </tr>
    </table>
</body>
</html>

#### Hints

* Make sure to comment on most lines of code
* Functions can be documented using a standard format for autodoc string
* Try to follow python conventions PEP8 or Black
* Make tutorial notebooks that users can explore
* Create `readthedocs`
* Add environment configuration file
* Serve your package in a Docker container
* Add a license file for reuse
* Add continuous integration


### Presentation (40%)

You will be required to prepare a 12-minute presentation describing your final project. The project will be graded using a combination of peer reviews and Prof. Agar's evaluation. At Prof. Agar's discretion, he can exclude any peer evaluation, which he feels is unfair.

#### Topics to Cover

1. The problem that your project addresses
1. Computational tools which are developed
1. Demonstration of how your tool works
1. Future development roadmap and impact

#### Presentation Rubric

<table class="center" style=100 width="100%">
    <style>
    tr:nth-child(even) {
    background-color: #FFFFFF;}
    border: 1px solid black;
    border-collapse: collapse;
    </style>
    <colgroup>
       <col span="1" style="width: 15%;">
       <col span="1" style="width: 75%;">
       <col span="1" style="width: 5%;">
       <col span="1" style="width: 5%;">
    </colgroup>
  <tr>
    <th style = "text-align:center">Category</th>
    <th style = "text-align:center">Scoring Criteria</th>
    <th style = "text-align:center">Total Points</th>
    <th style = "text-align:center">Points Scored</th>
  </tr>
  <tr>
    <td rowspan="3" style = "text-align:center"> <b>Organization (15 points)</b></td>
    <td style = "text-align:center">The type of presentation is appropriate for the topic and audience. </td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td style = "text-align:center">Information is presented in a logical sequence.</td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td style = "text-align:center">Presentation includes appropriate citations </td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td rowspan="6" style = "text-align:center"><b>Content (45 points) </b></td>
    <td style = "text-align:center">Introduction is attention-getting, establishes the problem well, and establishes a framework for the rest of the presentation.</td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
    <tr>
    <td style = "text-align:center"> Technical terms are well-defined in language appropriate for the target audience. </td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
    <tr>
    <td style = "text-align:center"> Presentation contains accurate information.  </td>
    <td style = "text-align:center">10</td>
    <td>&nbsp;</td>
  </tr>
    <tr>
    <td style = "text-align:center"> Material included is relevant to the overall message/purpose.
    </td>
    <td style = "text-align:center">10</td>
    <td>&nbsp;</td>
  </tr>
      <tr>
    <td style = "text-align:center"> Appropriate amount of material is prepared, and points made reflect well their relative importance.
    </td>
    <td style = "text-align:center">10</td>
    <td>&nbsp;</td>
  </tr>
    <tr>
    <td style = "text-align:center"> There is an obvious conclusion summarizing the presentation.
    </td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
    <tr>
    <td rowspan="6" style = "text-align:center"> <b>Presentation (40 points)</b>
    </td>
    <td style = "text-align:center"> Speakers maintains good eye contact with the
audience and is appropriately animated (e.g.,
gestures, moving around, etc.)</td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
      <tr>
    <td style = "text-align:center"> Speaker uses a clear, audible voice.
    </td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
    </tr>
      <tr>
    <td style = "text-align:center"> Delivery is poised, controlled, and smooth.
    </td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
    <tr>
    <td style = "text-align:center"> Visual aids are well prepared, informative,
effective, and not distracting
    </td>
    <td style = "text-align:center">10</td>
    <td>&nbsp;</td>
  </tr>
      <tr>
    <td style = "text-align:center"> Length of presentation is within the assigned
time limits.
    </td>
    <td style = "text-align:center">5</td>
    <td>&nbsp;</td>
  </tr>
        <tr>
    <td style = "text-align:center"> Information was well communicated.
    </td>
    <td style = "text-align:center">10</td>
    <td>&nbsp;</td>
  </tr>
    <tr>
    <td style = "text-align:center"> <b> Score </b>
    </td>
    <td style = "text-align:center"> <b> Total </b>
    </td>
    <td style = "text-align:center"> <b> 100 </b>
    </td>
    <td>&nbsp;</td>
  </tr>
</table>

### Peer Reviews (20%)

Your participation in the peer review process is essential for your fellow classmates and your experience in the course. Many students will continue their project beyond the timeline of the course. Your peer reviews will provide essential feedback. Prof. Agar will evaluate the quality of your reviews. 
