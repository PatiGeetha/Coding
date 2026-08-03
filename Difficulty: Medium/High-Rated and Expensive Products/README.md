<h2><a href="https://www.geeksforgeeks.org/problems/high-rated-and-expensive-products/1?page=2&category=python&sortBy=submissions">High-Rated and Expensive Products</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p data-start="0" data-end="273"><span style="font-size: 14pt;">Given a Pandas DataFrame <strong>products </strong>containing information about products, return the product_id, product_name, rating, quantity_in_stock, and price </span><span style="font-size: 14pt;">of all products that are high-rated, in stock, and expensive. A product is considered high-rated and expensive if:</span></p>
<ul data-start="275" data-end="428">
<li data-section-id="xeyl9w" data-start="275" data-end="322"><span style="font-size: 14pt;"> The product has a rating of at least 4.5. </span></li>
<li data-section-id="1ad15tv" data-start="323" data-end="387"><span style="font-size: 14pt;"> The product is available in stock (quantity_in_stock &gt; 0). </span></li>
<li data-section-id="lp5tvu" data-start="388" data-end="428"><span style="font-size: 14pt;"> The product price is at least<strong> </strong>300. </span></li>
</ul>
<p><span style="font-size: 14pt;"> </span></p>
<p data-start="430" data-end="474" data-is-last-node="" data-is-only-node=""><span style="font-size: 14pt;">Return the resulting DataFrame in any order.</span></p>
<h3>Pandas Schema:</h3>
<p><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894752/Web/Other/blobid0_1746527915.png" width="564" height="348"></p>
<ul>
<li>
<p><strong>product_id</strong>: Unique ID for each product (Primary key).</p>
</li>
<li>
<p><strong>product_name</strong>: The name of the product.</p>
</li>
<li>
<p><strong>rating</strong>: The rating of the product (float, ranging from 1 to 5).</p>
</li>
<li>
<p><strong>quantity_in_stock</strong>: The number of units available in stock.</p>
</li>
<li>
<p><strong>price</strong>: The price of the product.</p>
</li>
</ul>
<h2>Example :</h2>
<h3>Input table<strong>:</strong></h3>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894752/Web/Other/blobid1_1746527951.png" width="815" height="388"></strong></p>
<h3>Expected Output<strong> :</strong></h3>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894752/Web/Other/blobid2_1746527973.png" width="818" height="331"></strong></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python</code>&nbsp;