<h2><a href="https://www.geeksforgeeks.org/problems/daily-products-and-customers/1?page=2&category=python&sortBy=submissions">Daily Products and Customers</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p data-start="25" data-end="238"><span style="font-size: 18.6667px;">Given a DataFrame <strong>activities</strong> containing information about product purchases, determine the number of distinct products purchased and distinct customers for each combination of date_id and store_name.</span></p>
<p data-start="25" data-end="238"><span style="font-size: 18.6667px;">For every (date_id, store_name) pair, calculate:</span></p>
<ul>
<li data-start="25" data-end="238"><span style="font-size: 18.6667px;">unique_products: The number of distinct product_id values.</span></li>
<li data-start="25" data-end="238"><span style="font-size: 18.6667px;">unique_customers: The number of distinct customer_id values.</span></li>
</ul>
<p data-start="25" data-end="238"><span style="font-size: 14pt;">Return a DataFrame containing the columns date_id, store_name, unique_products, and unique_customers in any order.</span></p>
<p class="" data-start="501" data-end="519"><strong data-start="501" data-end="519">Pandas Schema:</strong></p>
<p class="" data-start="501" data-end="519"><strong data-start="501" data-end="519"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894891/Web/Other/blobid2_1746689478.png" width="319" height="236"></strong></p>
<ul data-start="738" data-end="1000">
<li class="" data-start="738" data-end="793">
<p class="" data-start="740" data-end="793"><strong data-start="740" data-end="751">date_id</strong>: The date when the product was purchased.</p>
</li>
<li class="" data-start="794" data-end="866">
<p class="" data-start="796" data-end="866"><strong data-start="796" data-end="810">store_name</strong>: The name of the store where the product was purchased.</p>
</li>
<li class="" data-start="867" data-end="924">
<p class="" data-start="869" data-end="924"><strong data-start="869" data-end="883">product_id</strong>: The unique ID of the product purchased.</p>
</li>
<li class="" data-start="925" data-end="1000">
<p class="" data-start="927" data-end="1000"><strong data-start="927" data-end="942">customer_id</strong>: The unique ID of the customer who purchased the product.</p>
</li>
</ul>
<h3 class="" data-start="1148" data-end="1162">Example :</h3>
<p class="" data-start="1164" data-end="1180"><strong data-start="1164" data-end="1180">Input table:</strong></p>
<p class="" data-start="1164" data-end="1180"><strong data-start="1164" data-end="1180"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894891/Web/Other/blobid1_1746689453.png" width="619" height="373"></strong></p>
<p class="" data-start="1893" data-end="1910"><strong data-start="1893" data-end="1910">Output table:</strong></p>
<p class="" data-start="1893" data-end="1910"><strong data-start="1893" data-end="1910"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894891/Web/Other/blobid0_1763205058.webp" width="684" height="222"></strong></p>
<p class="" data-start="2410" data-end="2426"><strong data-start="2410" data-end="2425">Explanation</strong>: <span style="font-size: 14pt;">The result is a DataFrame&nbsp;having&nbsp;date_id,&nbsp;store_name, unique_products&nbsp;and&nbsp;unique_customers</span></p>
<ul data-start="2427" data-end="2939">
<li class="" data-start="2427" data-end="2569">
<p class="" data-start="2429" data-end="2569"><span style="font-size: 14pt;">On 2021-05-10 at walmart, the distinct product_id values are 101, 102, 103, and the distinct customer_id values are 1 and 2.</span></p>
</li>
<li class="" data-start="2570" data-end="2659">
<p class="" data-start="2572" data-end="2659"><span style="font-size: 14pt;">On 2021-05-10 at target, only one product (104) was bought by one customer (2).</span></p>
</li>
<li class="" data-start="2660" data-end="2802">
<p class="" data-start="2662" data-end="2802"><span style="font-size: 14pt;">On 2021-05-09 at walmart, the distinct product_id values are 101, 106, 107, and the distinct customer_id values are 1, 4, 5.</span></p>
</li>
<li class="" data-start="2803" data-end="2939">
<p class="" data-start="2805" data-end="2939"><span style="font-size: 14pt;">On 2021-05-09 at target, the distinct product_id values are 105, 108, and the distinct customer_id values are 2 and 3.</span></p>
</li>
</ul></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python</code>&nbsp;