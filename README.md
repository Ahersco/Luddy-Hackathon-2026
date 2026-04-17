# Luddy-Hackathon-2026
●
Dynamic Leaderboard/Ranking System
A. Case Overview: Teams must develop a leaderboard and ranking system in which a
user can submit a score or statistic, upon which a remote server updates the
leaderboard accordingly. The leaderboard must be accessible via a remote procedure
call. The project must adhere to REST API standards (see Section II).
Note: AI-assisted code generation is strongly advised against and will be
factored into evaluation
B. Problem Definition: The specific tasks for this case involves the following:
●
●
Writing a remote server framework (Preferred Language w/ .yaml or JSON)
Expose a REST API that contains the following endpoints:
●
/add - adds an entry to the leaderboard
●
/remove - removes an entry to the leaderboard
●
/ leaderboard - returns the top 10 leaderboard positions in any graphical
format (e.g., pretty print, graphic, table)
/ info - Returns basic quantitative statistics for all entries (e.g., mean,
median, quartiles)
●
/ performance - returns average endpoint execution time.
●
Create a client-side webpage to interact with the server.
●
Presentation for judges ( 3 minute presentation/video )
The following are optional for Undergraduate teams, and are REQUIRED FOR GRADUATE
TEAMS. Undergraduate teams that effectively implement the following may also receive
better judgment on evaluation.
●
/history - endpoint that logs all score submissions with timestamps and
supports basic query filtering (e.g., by date range or user)
The server must be containerized (e.g., Docker) for reproducible deployment
/info endpoint must go beyond basic statistics to include additional metrics
such as standard deviation, percentile ranks, and score distribution
C. Learning Objectives/Key Goals: Teams will practice critical skills used in nearly all
back-end web development and DevOps. Teams will also leverage various data
structures and implement data automation to effectively deploy a web-hosted service.
Teams should be able to submit a working prototype within the 24hr time limit.
●
●
II. Background and Resources
A. Contextual Information: A REST API is a programming interface that conforms to the
design principles of the representational state transfer (REST) architectural style, a style
used to connect distributed hypermedia systems. REST APIs adhere to the following
standards (IBM):
●
●
●
●
●
●
Uniform interface
Client-server decoupling
Statelessness
Cacheability
Layered system architecture
Code on demand (optional)
More detailed information can be found at https://www.ibm.com/think/topics/rest-apis
B. Tools/Data/API Access:
●
●
●
●
API Editing tools
●
Swagger Editor (Recommended)
●
Scalar
●
Alternatives: Postman, Redoc, Stoplight Elements
■
Judges may not be as well versed in these.
Server Hosting
●
Virtual Machine, separate physical machine, or virtual environment
●
Local hosting is acceptable as a fallback
Data Format
●
Any REST API-compliant hypermedia or file type
●
Any graphical format for the leaderboard (e.g., .png , .jpeg , pretty-printed
text, HTML table)
Resources
●
●
■
Participants may choose to use any server hosting provider of their
choice, including IU’s silo, if they have previous access.
Participants may choose to use a server hosted by the Luddy Hacks team.
Request the login credentials by sending an email to
iuhacks@iu.edu .
■
The server is RISC-V Architecture, Linux, Oracle Cloud Developer 8
Distribution. The user will not have root access and should prepare
to download and/or compile binaries out of the home directory.
Users will be assigned non-standard ports.
■
Code of conduct applies. No abusive behavior.
C. Constraints and Scope:
●
●
●
Time: 24 Hrs
Technology Stack:
●
Team's choice (see tool recommendations above)
Deliverables:
●
Webpage for user interaction for server (URL)
●
Github Repository with the following:
■
Server and RPC definitions Source Code
■
.yaml file containing the following endpoints:
●
/add
●
/remove
●
/leaderboard
●
/info
■
Webpage files (.html, .java, .css, etc)
III. Judging Criteria and Rubric
Teams will be judged on the following
A. 10% - Innovation and Creativity: How unique and novel is the solution?
B. 50% - Technical Feasibility and Execution: Quality of code, functionality of the
prototype, and use of technology. (Usage of Libraries may affect judgment)
C. 10% - Impact and Viability: Potential real-world impact and sustainability of the
solution.
D. 30% - Presentation and Communication: Clarity of the pitch, demonstration, and
documentation.
IV. Submission Details
A. Final Deliverables Checklist:
Webpage for user interaction for server (URL)
Github Repository with the following:
Server and RPC definitions Source Code
.yaml file containing the following endpoints:
/add
/remove
/leaderboard
/info
Webpage files (.html, .java, .css, etc)
3-minute judge presentation
B. Submission Process: Submit the GitHub repository link and hosted URL via the
hackathon submission portal before the deadline.
C. Intellectual Property (IP) Policy: All teams retain full ownership of their
submitted code.