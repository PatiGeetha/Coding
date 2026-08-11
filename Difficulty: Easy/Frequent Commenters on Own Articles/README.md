<h2><a href="https://www.geeksforgeeks.org/problems/frequent-commenters-on-own-articles/1?page=2&category=python&sortBy=submissions">Frequent Commenters on Own Articles</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><div class="z-0 flex min-h-[46px] justify-start"><span style="font-size: 14pt;">Given a DataFrame containing information about comments made on articles, where:</span></div>
<div class="flex max-w-full flex-col gap-4 grow">
<div class="min-h-8 text-message relative flex w-full flex-col items-end gap-2 text-start break-words whitespace-normal outline-none keyboard-focused:focus-ring [.text-message+&amp;]:mt-1" dir="auto" tabindex="0" data-message-author-role="assistant" data-message-id="a5cb2212-ef24-46c2-a43b-1efc420c3925" data-message-model-slug="gpt-5-5" data-turn-start-message="true">
<div class="flex w-full flex-col gap-1 empty:hidden">
<div class="markdown prose dark:prose-invert wrap-break-word w-full light markdown-new-styling">
<ul data-start="94" data-end="301">
<li data-section-id="cgr12a" data-start="94" data-end="132"><span style="font-size: 14pt;"><strong>article_id </strong>represents the article.</span></li>
<li data-section-id="1yiia6u" data-start="133" data-end="184"><span style="font-size: 14pt;"><strong>author_id&nbsp;&nbsp;</strong>represents the author of the article.</span></li>
<li data-section-id="mu7jsn" data-start="185" data-end="248"><span style="font-size: 14pt;"><strong>viewer_id </strong>represents the user who commented on the article.</span></li>
<li data-section-id="29u37j" data-start="249" data-end="301"><span style="font-size: 14pt;"><strong><span style="font-family: monospace;"><span style="font-size: 18.6667px;">comment_date </span></span></strong><span style="font-size: 14pt;">represents the date of the comment.</span></span></li>
</ul>
<p data-start="303" data-end="376"><span style="font-size: 14pt;">Find all authors who have commented on their own articles more than once.<br></span><span style="font-size: 14pt;">Return a DataFrame containing the <strong>author_id</strong>&nbsp; of such authors, renamed as <strong>id</strong>, sorted in ascending order.</span></p>
</div>
</div>
</div>
</div>
<h3>Pandas Schema<strong>:</strong></h3>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1747029156.png" width="353" height="258"></strong></p>
<ul>
<li>
<p><span style="font-size: 14pt;"><strong>article_id</strong>: Unique ID for each article.</span></p>
<span style="font-size: 14pt;"> </span></li>
<li><span style="font-size: 14pt;"> </span>
<p><span style="font-size: 14pt;"><strong>author_id</strong>: The unique ID of the article's author.</span></p>
<span style="font-size: 14pt;"> </span></li>
<li><span style="font-size: 14pt;"> </span>
<p><span style="font-size: 14pt;"><strong>viewer_id</strong>: The unique ID of the person who commented on the article.</span></p>
<span style="font-size: 14pt;"> </span></li>
<li><span style="font-size: 14pt;"> </span>
<p><span style="font-size: 14pt;"><strong>comment_date</strong>: The date when the comment was made</span>.</p>
</li>
</ul>
<h2>Example :</h2>
<h3>Input table<strong>:</strong></h3>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1747029167.png" width="608" height="373"></strong></p>
<h3>Output table<strong>:</strong></h3>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895028/Web/Other/blobid3_1747029567.png" width="119" height="233"></strong></p>
<h3>Explanation:</h3>
<ul>
<li>
<p><span style="font-size: 14pt;"><strong>Author 3</strong>: Commented twice on their own article (article 1).</span></p>
<span style="font-size: 14pt;"> </span></li>
<li><span style="font-size: 14pt;"> </span>
<p><span style="font-size: 14pt;"><strong>Author 7</strong>: Commented twice on their own article (article 2).</span></p>
<span style="font-size: 14pt;"> </span></li>
<li><span style="font-size: 14pt;"> </span>
<p><span style="font-size: 14pt;"><strong>Author 5</strong>: Commented twice on their own article (article 5).</span></p>
</li>
</ul></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python</code>&nbsp;