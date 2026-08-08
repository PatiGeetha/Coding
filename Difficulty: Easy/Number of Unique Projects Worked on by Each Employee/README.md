<h2><a href="https://www.geeksforgeeks.org/problems/number-of-unique-projects-worked-on-by-each-employee/1?page=2&category=python&sortBy=submissions">Number of Unique Projects Worked on by Each Employee</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p data-start="509" data-end="553" data-is-last-node="" data-is-only-node=""><span style="font-size: 14pt;">Given a DataFrame<strong> employee_projects</strong> containing information about employees and the projects they work on, determine the number of unique projects worked on by each employee. An employee may be associated with the same project multiple times. Count only the distinct project_id values for each employee.</span></p>
<p data-start="509" data-end="553" data-is-last-node="" data-is-only-node=""><span style="font-size: 14pt;">Return a DataFrame containing the columns employee_id and cnt, where cnt is the number of distinct projects associated with the employee. The result can be returned in any order.</span></p>
<p class="" data-start="370" data-end="388"><strong data-start="370" data-end="388">Pandas Schema:</strong></p>
<p class="" data-start="370" data-end="388"><strong data-start="370" data-end="388"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1746690952.png" width="325" height="211"></strong></p>
<ul data-start="581" data-end="742">
<li class="" data-start="581" data-end="632">
<p class="" data-start="583" data-end="632"><span style="font-size: 14pt;"><strong data-start="583" data-end="598">employee_id</strong>: The unique ID for each employee.</span></p>
</li>
<li class="" data-start="633" data-end="682">
<p class="" data-start="635" data-end="682"><span style="font-size: 14pt;"><strong data-start="635" data-end="649">project_id</strong>: The unique ID for each project.</span></p>
</li>
<li class="" data-start="683" data-end="742">
<p class="" data-start="685" data-end="742"><span style="font-size: 14pt;"><strong data-start="685" data-end="696">dept_id</strong>: The department ID where the project belongs.</span></p>
</li>
</ul>
<p class="" data-start="744" data-end="866"><span style="font-size: 14pt;">The combination of <strong data-start="763" data-end="777">project_id</strong> and <strong data-start="782" data-end="793">dept_id</strong> serves as a unique identifier for each project in a specific department.</span></p>
<h3 class="" data-start="1088" data-end="1102"><span style="font-size: 14pt;">Example :</span></h3>
<p class="" data-start="1104" data-end="1120"><span style="font-size: 14pt;"><strong data-start="1104" data-end="1120">Input table:</strong></span></p>
<p class="" data-start="1104" data-end="1120"><span style="font-size: 14pt;"><strong data-start="1104" data-end="1120"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1746690968.png" width="452" height="321"></strong></span></p>
<p class="" data-start="1560" data-end="1577"><span style="font-size: 14pt;"><strong data-start="1560" data-end="1577">Output table:</strong></span></p>
<p class="" data-start="1560" data-end="1577"><span style="font-size: 14pt;"><strong data-start="1560" data-end="1577"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid2_1746690992.png" width="302" height="200"></strong></span></p>
<p class="" data-start="1720" data-end="1736"><span style="font-size: 14pt;"><strong data-start="1720" data-end="1735">Explanation</strong>: </span><span style="font-size: 14pt;">The result is a DataFrame having&nbsp;employee_id and cnt .</span></p>
<ul data-start="1737" data-end="1889">
<li class="" data-start="1737" data-end="1810">
<p class="" data-start="1739" data-end="1810"><span style="font-size: 14pt;">Employee 1: Works on project 101, 102, and 103 (3 unique projects).</span></p>
</li>
<li class="" data-start="1811" data-end="1889">
<p class="" data-start="1813" data-end="1889"><span style="font-size: 14pt;">Employee 2: Works on project 101, 102, 103, and 104 (4 unique projects).</span></p>
</li>
</ul></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python</code>&nbsp;