# diabetes-regression
<h3>Methodology</h3>
<p>The releveant libraries are imported at the top of run.py, and a built in dataset from sklearn is imported and partitioned into testing and training sets(80/20)</p><br>
<p>There are 10 columns in the X matrix, so a weight vector of length 10 is predicted using sklearn's built in regression tools. The figure below shows the predicted y values against the actual y values. This allows one to visually inspect how accurate the weight vector and y intercept (the regression model) is for the data set. A perfect prediction would follow the function y=x exactly. As we can see here, although not perfect, the model is considerably accurate:</p>
<a href="https://ibb.co/kK9kDNT"><img src="https://i.ibb.co/b12qvcV/Figure-1.png" alt="Figure-1" border="0"></a>

<p>Thanks to Data Professor's YouTube video for the instructions: </p>
<a href="https://www.youtube.com/watch?v=R15LjD8aCzc">