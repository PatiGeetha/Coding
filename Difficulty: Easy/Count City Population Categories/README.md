<h2><a href="https://www.geeksforgeeks.org/problems/count-city-population-categories/1?page=2&category=python&sortBy=submissions">Count City Population Categories</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p data-start="661" data-end="779"><span style="font-size: 14pt;">Given a DataFrame <strong>cities</strong> containing information about cities and their populations, determine the number of cities that belong to each population category. The population categories are defined as follows:</span></p>
<ul>
<li data-start="661" data-end="779"><span style="font-size: 14pt;">Small City: Population strictly less than 100000.</span></li>
<li data-start="661" data-end="779"><span style="font-size: 14pt;">Medium City: Population in the inclusive range [100000, 1000000].</span></li>
<li data-start="661" data-end="779"><span style="font-size: 14pt;">Large City: Population strictly greater than 1000000.</span></li>
</ul>
<p data-start="661" data-end="779"><span style="font-size: 14pt;">Return a DataFrame with the following columns:</span></p>
<ul>
<li data-start="661" data-end="779"><span style="font-size: 14pt;">category: The population category.</span></li>
<li data-start="661" data-end="779"><span style="font-size: 14pt;">cities_count: The number of cities belonging to that category.</span></li>
</ul>
<p data-start="661" data-end="779"><span style="font-size: 14pt;">The result must always contain all three categories. If no city belongs to a category, return 0 for that category.</span></p>
<h3 class="" data-start="766" data-end="784">Pandas Schema:</h3>
<p><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894782/Web/Other/blobid1_1746687221.png" width="354" height="211"></p>
<ul data-start="939" data-end="1034">
<li class="" data-start="939" data-end="992">
<p class="" data-start="941" data-end="992"><strong data-start="941" data-end="952">city_id</strong>: Unique ID for each city (Primary key).</p>
</li>
<li class="" data-start="993" data-end="1034">
<p class="" data-start="995" data-end="1034"><strong data-start="995" data-end="1009">population</strong>: Population of the city.</p>
</li>
</ul>
<h3 class="" data-start="1041" data-end="1055">Example :</h3>
<p class="" data-start="1057" data-end="1073"><strong data-start="1057" data-end="1073">Input table:</strong></p>
<p class="" data-start="1057" data-end="1073"><strong data-start="1057" data-end="1073"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894782/Web/Other/blobid2_1746687237.png" width="300" height="291"></strong></p>
<p class="" data-start="1334" data-end="1351"><strong data-start="1334" data-end="1351">Output table:</strong></p>
<p class="" data-start="1334" data-end="1351"><strong data-start="1334" data-end="1351"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894782/Web/Other/blobid3_1746687251.png" width="434" height="218"></strong></p>
<p data-start="1619" data-end="1635"><span style="font-size: 14pt;"><strong>Explanation: </strong>The result is a DataFrame with two columns: category and cities_count.</span></p>
<ul>
<li data-start="1619" data-end="1635"><span style="font-size: 14pt;">Small City contains cities with city_id 1 and 5, so the count is 2.</span></li>
<li data-start="1619" data-end="1635"><span style="font-size: 14pt;">Medium City contains cities with city_id 2 and 4, so the count is 2.</span></li>
<li data-start="1619" data-end="1635"><span style="font-size: 14pt;">Large City contains cities with city_id 3 and 6, so the count is 2.</span></li>
</ul>
<p data-start="1619" data-end="1635"><span style="font-size: 14pt;">Hence, the output shows the number of cities in each population category.</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python</code>&nbsp;