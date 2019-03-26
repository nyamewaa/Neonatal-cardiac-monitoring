Ziva ECG
========

Initial Questions
-----------------
1. Calculate Ziva's HR
2. What is the ECG signal SNR?
3. What is the ECG signal bandwidth?
4. How much can you decimate the data without losing signal content?

Task: Write a Python program to answer the questions above based on the data in
[ziva.csv](ziva.csv).

Learning Git
------------
* https://try.github.io/
* http://gitimmersion.com/index.html
* http://pcottle.github.io/learnGitBranching/
* http://git-scm.com/book

Get Your Project in a Git Repository
------------------------------------
1. Setup an SSH key pair to communicate with GitLab from your personal
   computer: https://gitlab.oit.duke.edu/help/ssh/README
2. Fork this repository in GitLab into a personal repository, and add Dr.
   Palmeri and your partner as repository members.
3. Clone (```git clone```) your repository to your local computer.
4. Add (```git add```) and commit (```git commit```) your code, ipython
   notebook, plots, etc. into your version of the repository.
5. Push (```git push```) your commit(s) to GitLab.
6. Create an Issue on GitLab when you are ready to have your code reviewed, and
   assign it to Dr. Palmeri.

Expanding Your Heart Rate Monitor
--------------------------------
1. Create a python module that will contain all of your algorithms, and a
   "main" script.  (see
   https://gitlab.oit.duke.edu/mlp6/fem/blob/master/mesh/fem_mesh.py as an
   example)
2. Write a HR algorithm that will be tolerant of a floating DC offset and
   variable voltage magnitude in the ECG signal.
3. Write an algorithm that will detect tachycardia and report the time
   interval(s) when it occurs.
4. Make sure all functions have docstrings
   (https://www.python.org/dev/peps/pep-0257/).  (see
   https://gitlab.oit.duke.edu/mlp6/fem/blob/master/post/create_res_sim_mat.py
   as an example)
5. Create an annotated git tag (```git tag -a```) indicating that all of the
   above functionality and code structure has been implemented.

*Be sure to frequently commit changes with this expanded functionality, with at
least one commit for each of the enumerated items above.  Also make sure that
both group members make at least one commit during the process (even if just a
test commit).*


Looking Ahead
-------------
1. Write unit tests for your algorithms using ```py.test``` or ```nose```.
2. Expand code to accept input arguments for ECG data file and algorithm choice
   (```argparse```).
3. Streaming long ECG data traces that cannot be loaded into memory all at
   once.
4. Exanding the HR monitor to detect heart block, atrial fibrillation and PVCs.