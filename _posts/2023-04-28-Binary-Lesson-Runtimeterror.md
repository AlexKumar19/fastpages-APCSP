---
keywords: fastai
description: Learn the basics of binary including truth tables, boolean expressions, binary conversions, and binary searches.
title: P4-M 4/28 Binary Lesson HACKS
toc: true
permalink: /binary/lesson
comments: true
categories: [week 31, binary, lesson]
nb_path: _notebooks/2023-04-28-Binary-Lesson-Runtimeterror.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2023-04-28-Binary-Lesson-Runtimeterror.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Lesson-Note-Taker">Lesson Note Taker<a class="anchor-link" href="#Lesson-Note-Taker"> </a></h1><blockquote><p>Fill in the blanks below during the binary presentation. You can visit our <a href="https://theoh32.github.io/Runtime_Terror/2023-3-30-mainlesson.html">website here!</a>^ Due to last minute deployment issues, may need to run a local server</p>
</blockquote>
<ol>
<li>git clone <a href="https://github.com/TheoH32/Runtime_Terror.git">https://github.com/TheoH32/Runtime_Terror.git</a></li>
<li>run: </li>
</ol>
<ul>
<li>bundle install</li>
<li>bundle exec jekyll serve</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Binary">Binary<a class="anchor-link" href="#Binary"> </a></h2><ol>
<li>Binary is a base 2 number system.</li>
<li>0 represents off and 1 represents on</li>
<li>A bit is the minimum unit of binary information stored in a computer system.</li>
</ol>
<h2 id="Boolean-Expressions">Boolean Expressions<a class="anchor-link" href="#Boolean-Expressions"> </a></h2><ol>
<li>A boolean expression is a logical statement that is either TRUE or FALSE and compares data.</li>
</ol>
<h2 id="Truth-Tables">Truth Tables<a class="anchor-link" href="#Truth-Tables"> </a></h2><ol>
<li>The logical operations shown in truth tables are and, or, not, and XOR.</li>
</ol>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># AND</span>
<span class="mi">5</span> <span class="o">&gt;</span> <span class="mi">3</span> <span class="ow">and</span> <span class="mi">5</span> <span class="o">==</span> <span class="mi">3</span> <span class="o">+</span> <span class="mi">2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>True</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="mi">5</span> <span class="o">&lt;</span> <span class="mi">3</span> <span class="ow">and</span> <span class="mi">5</span> <span class="o">==</span> <span class="mi">5</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>False</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="mi">5</span> <span class="o">==</span> <span class="mi">5</span> <span class="ow">or</span> <span class="mi">5</span> <span class="o">!=</span> <span class="mi">5</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>True</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="mi">5</span> <span class="o">&lt;</span> <span class="mi">3</span> <span class="ow">or</span> <span class="mi">5</span> <span class="o">!=</span> <span class="mi">5</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>False</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Real-Life-Example-using-Boolean-Expressions">Real Life Example using Boolean Expressions<a class="anchor-link" href="#Real-Life-Example-using-Boolean-Expressions"> </a></h3><p>Try changing the conditions and/or the logical operation below! Run the code to see if you are eligible to vote.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">age</span> <span class="o">=</span> <span class="mi">19</span>
<span class="n">citizen</span> <span class="o">=</span> <span class="p">(</span><span class="kc">True</span><span class="p">)</span>

<span class="k">if</span> <span class="n">age</span> <span class="o">&gt;=</span> <span class="mi">18</span> <span class="ow">and</span> <span class="n">citizen</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;You are eligible to vote.&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;You are not eligible to vote.&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>You are eligible to vote.
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I went to the refinery met this girl she a 1010 so finery it made me think about binary turns out she non binary</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Binary-Conversions">Binary Conversions<a class="anchor-link" href="#Binary-Conversions"> </a></h2><h3 id="Binary-to-Decimal">Binary to Decimal<a class="anchor-link" href="#Binary-to-Decimal"> </a></h3><ol>
<li>We can count in binary by using powers of 2.</li>
<li>In binary, we read from right to left.</li>
<li>0111 has a value of 7.</li>
</ol>
<h3 id="Binary-Search">Binary Search<a class="anchor-link" href="#Binary-Search"> </a></h3><ol>
<li>For a binary search, the list must be sorted. </li>
<li>In a binary search, computers start at the middle (front,middle,end)/</li>
<li>The number of steps required in a binary search follows the equation:  log2(n)+1.</li>
<li>Binary searches also work with a list of strings. We can sort them alphabetically.</li>
<li>Binary searches can be represented in tree diagrams.</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Hacks">Hacks<a class="anchor-link" href="#Hacks"> </a></h1><blockquote><p>You will NOT be awarded any points for sections that are INCOMPLETE</p>
</blockquote>
<h3 id="Note-Taker">Note Taker<a class="anchor-link" href="#Note-Taker"> </a></h3><ol>
<li>Fill in all of the blanks above.</li>
</ol>
<h3 id="Lesson-Quiz">Lesson Quiz<a class="anchor-link" href="#Lesson-Quiz"> </a></h3><ol>
<li>Complete the lesson quiz</li>
<li>SCREENSHOT SCORE and paste it here (or paste screenshot with submission)</li>
</ol>
<h3 id="Binary-Game">Binary Game<a class="anchor-link" href="#Binary-Game"> </a></h3><ol>
<li>Complete the Binary game and reach a minimum score of 10! </li>
<li>SCREENSHOT SCORE and paste it here (or with submission)</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Binary-Conversions-Practice">Binary Conversions Practice<a class="anchor-link" href="#Binary-Conversions-Practice"> </a></h3><ol>
<li>Convert the decimal number "17" into binary.<ol>
<li>10001</li>
</ol>
</li>
<li>Convert the binary number 1010 into decimal.<ol>
<li>10</li>
</ol>
</li>
<li>Convert the decimal number "122" into hexadecimal.<ol>
<li>7A</li>
</ol>
</li>
<li>Convert the hexadecimal number "09" into binary.<ol>
<li>1001</li>
</ol>
</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Binary-Search-Questions">Binary Search Questions<a class="anchor-link" href="#Binary-Search-Questions"> </a></h3><ol>
<li>Make a binary search tree of different the list [1,2,4,15,25,30,31]<ol>
<li>31 / \ 25 30 / \ / \ 15 20 31 / \ / \ 4 18 27 / 2</li>
</ol>
</li>
<li>Put this list of strings in a order that can be used for binary search ["Donut”,"Cake”,"Soda”,"Banana”,"Fruit”]<ol>
<li>Here is the list in alphabetical order: ["Banana", "Cake", "Donut", "Fruit", "Soda"].</li>
</ol>
</li>
<li>Explain why Binary Search is more efficient than Sequential Search.<ol>
<li>Binary search is a more efficient algorithm than sequential search for finding a target value in a sorted list. Binary search works by repeatedly dividing the list in half until the target value is found. This means that binary search only needs to make a logarithmic number of comparisons, while sequential search needs to make a linear number of comparisons.</li>
</ol>
</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Extra-Credit:">Extra Credit:<a class="anchor-link" href="#Extra-Credit:"> </a></h3><ul>
<li>Translate the binary number, 1001010, into octal (base 8). <mark>SHOW YOUR WORK AND EXPLAIN YOUR THINKING.</mark>
OR</li>
<li>write the best rap line (determined during the lesson by group)</li>
</ul>
<p>Octal is a number system that is based on the number 8, using the digits 0 to 7. In contrast, binary is a number system based on the number 2, using only the digits 0 and 1. To convert a binary number to octal, we can split the binary digits into groups of three digits each, starting from the right. Next, we can replace each group of three binary digits with the corresponding octal digit.</p>
<p>Here are the steps to convert a binary number to octal:</p>
<p>Start with a binary number, for example: 1001010.
Group the binary digits into groups of three, starting from the right: 1 001 010.
Replace each group of three binary digits with the corresponding octal digit: 1 1 2.
Write the resulting octal digits together to get the octal equivalent of the binary number: 112.
Therefore, to convert a binary number to octal, we need to group the binary digits into sets of three, then replace each set with the corresponding octal digit. This process helps us to quickly convert between binary and octal representations.</p>
<p>I went to the refinery met this girl she a 1010 so finery it made me think about binary turns out she non binary</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Hacks-Scoring">Hacks Scoring<a class="anchor-link" href="#Hacks-Scoring"> </a></h1><table>
<thead><tr>
<th>Hack</th>
<th>Comments</th>
<th>Grade</th>
</tr>
</thead>
<tbody>
<tr>
<td>Note Taker</td>
<td>fill in the blanks above</td>
<td>0.1</td>
</tr>
<tr>
<td>Lesson Quiz</td>
<td>under 100% = 0.1 only</td>
<td>0.2</td>
</tr>
<tr>
<td>Binary Game</td>
<td>must score at least 10 points</td>
<td>0.2</td>
</tr>
<tr>
<td>Binary Conversions Practice</td>
<td>if incorrect= 0.2 awarded</td>
<td>0.2</td>
</tr>
<tr>
<td>Binary Search Questions</td>
<td>if incorrect= 0.2 awarded</td>
<td>0.2</td>
</tr>
<tr>
<td>Extra Credit</td>
<td>MUST SHOW WORK</td>
<td>0.1</td>
</tr>
<tr>
<td>Total</td>
<td>expected= 0.9/1</td>
<td>1/1</td>
</tr>
</tbody>
</table>

</div>
</div>
</div>
</div>
 

