# Multimodal CodeGen Evaluation

This repository provides a benchmark for evaluating multimodal models in the task of code generation from graphical representations. The dataset was built by selecting problems from Human-Eval and PSB2, specifically:

- 10 problems from Human-Eval
- 5 problems from PSB2

For each problem, various graphical representations have been created:

- Flowcharts with 3 levels of detail
- Block diagrams (Work in progress)
- BPMN (Work in progress)

Additionally, the "Others" folder contains graphical representations created by external contributors to the project. Details can be found in the following tables.

### Human Eval Selected Problems

The Code LLama and GPT-4 evaluation are reported [here](https://github.com/jamesmurdza/humaneval-results/tree/main).

<table>
	<tr>
		<th>Task</th>
		<th width="100">Code Llama</th>
		<th width="100">GPT-4</th>
		<th>Description</th>
		<th>Flowcharts</th>
		<th>BPMN</th>
		<th>Others</th>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p84.md">HumanEval/84</a></td>
		<td>$$\Large\mathbf{\color{orange}20\%}$$</td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>Return the total sum of the digits of a positive integer in binary form.</td>
		<td><a href="data/diagrams/human eval/p84/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p84/bpmn">BPMN</a></td>
		<td><a href="data/diagrams/human eval/p84/others">Others</a></td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p106.md">HumanEval/106</a></td>
		<td>$$\Large\mathbf{\color{yellow}80\%}$$</td>
		<td>$$\Large\mathbf{\color{orange}30\%}$$</td>
		<td>Calculate and return a list of size n, where each element at index i is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise.</td>
		<td><a href="data/diagrams/human eval/p106/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p106/bpmn">BPMN</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p108.md">HumanEval/108</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{orange}10\%}$$</td>
		<td>Count the number of elements in the array that have a sum of digits greater than 0.</td>
		<td><a href="data/diagrams/human eval/p108/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p108/bpmn">BPMN</a></td>
		<td><a href="data/diagrams/human eval/p108/others">Others</a></td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p119.md">HumanEval/119</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{orange}40\%}$$</td>
		<td>Check if it is possible to concatenate two strings of parentheses in some order to create a balanced string.</td>
		<td><a href="data/diagrams/human eval/p119/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p119/bpmn">BPMN</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p120.md">HumanEval/120</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>Return a sorted list of the maximum k numbers in the given array.</td>
		<td><a href="data/diagrams/human eval/p120/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p120/bpmn">BPMN</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p126.md">HumanEval/126</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{yellow}50\%}$$</td>
		<td>Check if a given list of numbers is sorted in ascending order and does not contain more than one duplicate of the same number.</td>
		<td><a href="data/diagrams/human eval/p126/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p126/bpmn">BPMN</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p131.md">HumanEval/p131</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{green}100\%}$$</td>
		<td>Return the product of the odd digits in a given positive integer, or 0 if all digits are even.</td>
		<td><a href="data/diagrams/human eval/p131/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p131/bpmn">BPMN</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p147.md">HumanEval/147</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>Calculate the number of triples in an array where the sum of the elements is a multiple of 3.</td>
		<td><a href="data/diagrams/human eval/p147/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p147/bpmn">BPMN</a></td>
		<td>N/A</td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p150.md">HumanEval/150</a></td>
		<td>$$\Large\mathbf{\color{green}100\%}$$</td>
		<td>$$\Large\mathbf{\color{green}100\%}$$</td>
		<td>Return the value of x if n is a prime number and return the value of y otherwise.</td>
		<td><a href="data/diagrams/human eval/p150/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p150/bpmn">BPMN</a></td>
		<td><a href="data/diagrams/human eval/p150/others">Others</a></td>
	</tr>
	<tr>
		<td><a href="./data/problems/human eval/p155.md">HumanEval/155</a></td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>$$\Large\mathbf{\color{red}0\%}$$</td>
		<td>Return a tuple containing the count of even and odd digits in the given integer.</td>
		<td><a href="data/diagrams/human eval/p155/fc">Flowcharts</a></td>
		<td><a href="data/diagrams/human eval/p155/bpmn">BPMN</a></td>
		<td><a href="data/diagrams/human eval/p155/others">Others</a></td>
	</tr>
</table>

### PSB2 Selected Problems

The Push-GP evaluation are reported in the paper [PSB2: The Second Program Synthesis Benchmark Suite](https://arxiv.org/abs/2106.06086).

<table>
	<tr>
		<th>Problem</th>
		<th width="100">Solved by Push-GP</th>
		<th>Description</th>
		<th>Diagram</th>
	</tr>
	<tr>
		<td><a href="https://www.codewars.com/kata/5a0b72484bebaefe60001867">Vector Distance</a></td>
		<td>0/100</td>
		<td>Given two 𝑛-dimensional vectors of ﬂoats, return the Euclidean distance between the two vectors in 𝑛-dimensional space.</td>
		<td><a href="./data/diagrams/psb2/vector distance/fc">Flowcharts</a></td>
	</tr>
	<tr>
		<td><a href="https://www.codewars.com/kata/546e2562b03326a88e000020">Square Digits</a></td>
		<td>0/100</td>
		<td>Given a positive integer, square each digit and concatenate the squares into a returned string.</td>
		<td><a href="./data/diagrams/psb2/square digits/fc">Flowcharts</a></td>
	</tr>
	<tr>
		<td><a href="https://www.codewars.com/kata/5264d2b162488dc400000001">Spin Words</a></td>
		<td>0/100</td>
		<td>Given a string of one or more words (separated by spaces), reverse all of the words that are ﬁve or more letters long and return the resulting string. </td>
		<td><a href="./data/diagrams/psb2/spin words/fc">Flowcharts</a></td>
	</tr>
	<tr>
		<td><a href="https://www.codewars.com/kata/5a651865fd56cb55760000e0">Leaders</a></td>
		<td>0/100</td>
		<td>Given a vector of positive integers, return a vector of the leaders in that vector. A leader is deﬁned as a number that is greater than or equal to all the numbers to the right of it. The rightmost element is always a leader. </td>
		<td>Work in progress</td>
	</tr>
	<tr>
		<td><a href="https://adventofcode.com/2020/day/1">Find Pairs</a></td>
		<td>4/100</td>
		<td>Given a vector of integers, return the two elements that sum to a target integer.</td>
		<td>Work in progress</td>
	</tr>
</table>
