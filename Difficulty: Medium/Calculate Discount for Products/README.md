<h2><a href="https://www.geeksforgeeks.org/problems/calculate-discount-for-products/1?page=2&category=python&sortBy=submissions">Calculate Discount for Products</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p data-start="25" data-end="135"><span style="font-size: 14pt;">Given a DataFrame <strong data-start="43" data-end="55">products</strong> containing information about products, determine the discount for each product. A product receives a discount equal to its price if product_id is even and category starts with 'A'; otherwise, the discount is 0.</span></p>
<p data-start="391" data-end="455"><span style="font-size: 14pt;">Return a DataFrame containing the product_id and corresponding discount for each product, ordered by product_id in ascending order.</span></p>
<p><strong>Pandas Schema:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1746698783.png" width="339" height="195"></strong></p>
<ul>
<li>
<p><strong>product_id</strong>: The unique ID for each product (Primary key).</p>
</li>
<li>
<p><strong>category</strong>: The category of the product.</p>
</li>
<li>
<p><strong>price</strong>: The price of the product.</p>
</li>
</ul>
<h3>Example :</h3>
<p><strong>Input table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1746698798.png" width="420" height="273"></strong></p>
<p><strong>Output table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894935/Web/Other/blobid0_1746706071.png" width="335" height="264"></strong></p>
<p><strong>Explanation</strong>:</p>
<p>The result is a <strong>DataFrame </strong>having <strong>product_id </strong>and <strong>discount</strong> .</p>
<ul>
<li>
<p><strong>Product 1</strong>: The product_id is odd, so no discount is applied.</p>
</li>
<li>
<p><strong>Product 2</strong>: The product_id is even, and the category starts with 'A' (Apple), so the discount is 100% of the price (800).</p>
</li>
<li>
<p><strong>Product 3</strong>: The product_id is odd, so no discount is applied.</p>
</li>
<li>
<p><strong>Product 4</strong>: The product_id is even, and the category starts with 'A' (Avocado), so the discount is 100% of the price (1000).</p>
</li>
<li>
<p><strong>Product 5</strong>: The product_id is odd, so no discount is applied.</p>
</li>
</ul></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python</code>&nbsp;