# Photovoltaic grid malfunction detector

In this repository a exploratory analysis is made from solar energy production and ambient conditions data. <br>
Then a linear model is created to predict if the grid have a malfunction based in the error of the model. <br>
If the residual error is outside of the 95% confidence interval, probably is a unusual error that indicate malfunction in the grid or the instrumentation<br>
Flask is used to creat the app and docker to create an environment with the dependencies to run the app.
