Give me a Diamond
==========
Solution for the [codewars](https://www.codewars.com) challenge.
* Task description: https://www.codewars.com/kata/give-me-a-diamond/python


The Task
----------
You need to return a string that displays a diamond shape on the screen using asterisk ("*") characters. Please see provided test cases for exact output format.

The shape that will be returned from print method resembles a diamond, where the number provided as input represents the number of asterisks printed on the middle line. The line above and below will be centered and will have 2 less asterisks than the middle line. This reduction by asterisks for each line continues until a line with a single asterisk is printed at the top and bottom of the figure.

Return `None` if the input is even number or negative (as it is not possible to print diamond with an even number or negative number).

### Example
`diamond(7)` should return:
```
   *
  ***
 *****
*******
 *****
  ***
   *
```


Running Tests
----------
Tests are located in the `tests` directory. To run Diamond related tests use `python -m unittest tests.test_diamond`


Authors
----------
* **Denis Z.** &#8212; *Initial work* &#8212; [d2718nis](https://github.com/d2718nis)

See also the list of [contributors](https://github.com/d2718nis/codewars-give-me-a-diamond/contributors) who participated in this project.