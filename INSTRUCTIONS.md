

# Assignment 1 - Benchmarking and Extrapolation


In this assignment you will deduce the asymptotic complexity (average-case) of a number of programs by running experiments, and write a report.


## Academic Integrity

This is a reminder that you are expected to complete this assignment without assistance from anyone, except perhaps your instructor.  Don't look at the code, or results, or report, of other students, nor show other students your code or results or report.  If you need to ask someone something, the person to ask is your instructor, during office hours.  If you don't understand this policy, ask your instructor, during class, or office hours.



## What you get

In addition to this file of Instructions, you have received five Python files, with names like `routine_1.py` to `routine_5.py`.  Each contains an implementation of an algorithm that I want you to measure, referred to in these instructions as "the routine".

Each file contains two things:

* A function called `fut` (stands for "function under test").
    * This `fut` **is the routine that you are going to measure, and estimate its asymptotic complexity**
    * This function accepts one parameter, a "case".
        * You can ignore what the case is, as long as you pass it in.
    * You can ignore what the `fut` returns.
* A function to make cases to input to the `fut`, called `casemaker`.
    * This function accepts one parameter, a `size`, which should be a non-negative integer.
    * This function returns a "case", i.e. it's the sort of thing you would pass to `fut`



## What you need to do

You must generate data by running experiments, then analyze this data to determine an estimate of the asymptotic speed of the routine, and then organize and present your analysis in a PDF.


### Gather data

To generate appropriate measurements, you will need to figure out what are suitable sizes for the cases, so that is your first problem.  Try running each routine with inputs of different sizes.  You need to find sizes that are small enough that they don't take *forever*, but large enough that they generate useful data.  Play around until you have an idea, for each routine, what size of `n` would let you run your tests in an hour.

Also, think about how many cases you will do at each size.  Remember the explorations of statistics that we did in Lab 2.  Make sure to output some statistics so that you can tell if you're not running enough cases.

Once you've decided on what experiments to run, make it happen.  You'll probably write some code so that a whole bunch of data is collected overnight.  Run it overnight, so that you get lots of data.

Notes and exceptions:

* I expect to see some reasonable-quality measurements for *at least 10 different sizes*
    * though in some cases, doing low-quality measurements for many different sizes and then plotting it could help you avoid mistakes
* In the past I have seen some students think that running the whole test in a minute or so is getting them data that's good enough, and while that works out fine sometimes, some of the time they have been *quite wrong*.  I suggest that you allocate something like an hour per routine, or more, for your final data gathering.  Set it up to run while you sleep.

### Do analysis

Our goal in this section is to figure out a formula that predicts how long the routine will take to run at different sizes.

Tidy up your data, into tables.  Also make a plot.

For each routine, you need to figure out, is it:
* constant time
* logarithmic time
* linear time
* polynomial time
* exponential time

If more than one answer applies, use the most specific, of course.

Then, you need to find an equation that matches the data (also called fitting a curve to it).  Use whatever tool you like.  The goal is to find a mathematical function that is a pretty good fit for your data.  You can, and should, check that if you put your values of `n` into it, it generally is relatively accurate at "predicting" values pretty close to the data you actually got.

Finally, make a prediction (an extrapolation): if you had to do a single case, on your computer, in one week, what is the largest `n` that would complete in a week?



## Presentation

You are going to hand in a PDF, via an Assignment dropbox in D2L.

The PDF will have the following sections, explained in detail below, in the following order.

1. cover page
2. optional: message to grader
3. analysis (5 sections)
4. code
5. terminal output
6. anything else


### 1. Cover Page

The Cover Page should include your name, student number, your set, and something like "ACIT 3896 Assignment 1".

### 2. Message to Grader (optional)

If there is anything about your assignment that you would like me to know before I grade it, you should put that on a page immediately after your cover page.

Otherwise, skip this, and get on with the Analysis.

Seriously, if you don't have anything special to say, skip this.

### 3: Analysis

This analysis section should come right after the cover page (or after any note you include).

For each Routine, you should have one to two pages of analysis.  This page(s) should basically contain five things:

1. clearly state which Routine it's for (and it'd be nice if the pages are in order, please)
2. clearly state your theory about the performance of the routine (see below)
3. a table (see below)
4. a plot (see below)
5. an extrapolation (see below)

#### 3.2: The Theory

You should have an equation that is your best guess about how the running time of this function (on your machine) varies with the size of the input.  That's a function with `n` (size) as its independent variable, and `t` (time) as its dependent variable.

So your deduction about asymptotic complexity will be something like `t = 14 * n^2` or maybe `t = 14 * n^2 + 117`.

Please specify the units, too (seconds, ns, ms, whatever).  Don't make me guess.


#### 3.3: The Table 

The table should include all of your test data, with at least the following columns (with labelled columns):

* size
* how many samples you took at that size
* raw mean time of performance at that size
* the prediction you would expect at that size, given your overall asymptotic analysis (your "theory", the equation)
* the ratio of prediction over observed
    * that means, take the "prediction according to theory" column and divide by the "raw mean time" column


#### 3.4: The Plot

The plot should include both your test data, and also the plot of your theory (your equation).  For the data, I should see dots for the actual data points.  Your equation should be a smooth line, that hopefully passes pretty near your dots.

Don't do dots for your theory.  Don't do a line for your actual data.  Make sure I can tell which is which; annotate them if necessary.

You can do this plot by hand, on paper, and photograph or scan.  (If you do it by hand, be neat!)  You can do this with software, like spreadsheet software, or something else.

Make sure that your axes start at 0, and are either linear or logarithmic (that is, you must use uniform axes of some kind), and are labelled with numeric values (so that I can see the domain and range, and so that I can tell if they're linear or logarithmic).

Your plot and your table must be consistent with each other.


#### 3.5: The Extrapolation

Now that you have gathered data, come up with a theory, and checked that the theory acceptably fits the data that you gathered, you could make an extrapolation.  You can't afford to just run this test for a whole month, but you can make an educated guess what would happen if you did.

So for each routine, as part of the analysis for that routine, you should make an extrapolation.  At the bottom of each routine's page-or-two, complete the following sentence:

> If this routine was given a month (30.5 days, or 5124 hours, or 18.5 million seconds) to run on my machine, the largest `n` that I would expect to complete a single case within a full week would be n = ______.

### 4, 5, and 6: Code and Terminal Output

This is your measurement code, and your raw terminal output.

I do expect you to include these.  But I will probably not read these.  So if you are writing notes here that you expect me to read, they might not get read.  You're including these so that if your answers are all wrong, I can look at these and maybe give you part marks.  Also I'll probably read half a dozen across the whole class, to learn how students work, so that I can improve the instructions next term.

## Grades


The assignment will be out of 20 marks.

For each of the 5 routines, 4 marks will be given.  To achieve full marks on a given routine, you should have:

* enough data to justify faith in the theory and extrapolation
* a clear and correct table, as described above
* a clear and correct plot, as described above
* a clearly stated and reasonably correct theory about asymptotic complexity, in the form of an equation
* a clearly stated and reasonably correct extrapolation for what value of `n` would take about 1 month to run, on average, on your machine


Students who go above and beyond, typically with unusually careful or thoughtful or insightful analysis, may get marks to make up for deficiencies elsewhere.

Conversely, if students ignore my instructions on layout, I may dock up to 3 marks.

