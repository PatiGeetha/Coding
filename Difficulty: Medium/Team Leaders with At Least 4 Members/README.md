<h2><a href="https://www.geeksforgeeks.org/problems/team-leaders-with-at-least-4-members/1?page=2&category=python&sortBy=submissions">Team Leaders with At Least 4 Members</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p data-start="25" data-end="198"><span style="font-size: 18.6667px;">Given a DataFrame <strong>employee</strong> containing information about employees and their team leaders, find the names of all team leaders who have at least 4 direct reports. An employee is considered a direct report of a team leader if the employee's leaderId is equal to that team leader's id.</span></p>
<p data-start="25" data-end="198"><span style="font-size: 18.6667px;">Return a DataFrame containing the names of all such team leaders.</span></p>
<p><strong>Pandas Schema:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid2_1746785537.png" width="304" height="222"></strong></p>
<ul>
<li>
<p><strong>id</strong>: Unique ID for each employee (Primary key).</p>
</li>
<li>
<p><strong>name</strong>: Name of the employee.</p>
</li>
<li>
<p><strong>department</strong>: The department where the employee works.</p>
</li>
<li>
<p><strong>leaderId</strong>: ID of the employee's team leader (null if the employee has no leader).</p>
</li>
</ul>
<h3>Example :</h3>
<p><strong>Input table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1746785491.png" width="500" height="379"></strong></p>
<p><strong>Output table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1746785460.png" width="123" height="155"></strong></p>
<p><strong>Explanation</strong>:</p>
<ul>
<li>
<p><strong>Sarah</strong> is the team leader of <strong>John, Jack, Emma, Olivia, James, Thomas, David</strong>, and <strong>Lily</strong> (8 direct reports).</p>
</li>
<li>
<p>Therefore, <strong>Sarah</strong> is included in the result.</p>
</li>
</ul></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python</code>&nbsp;