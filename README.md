# ContourEstimator

Program to calculate the contour length using different estimators. The contour is usually described using chaincode. Chaincode is describing the direction of the contour. This is usually done with the numbers 0 till 7, as seen in the table below. The x denotes the current position.

|   |   |   |
| - |:-:| -:|
| 3 | 2 | 1 |
| 4 | x | 0 |
| 5 | 6 | 7 |

The program uses the chaincode to calculate the length of the contour using different estimators. These are:

* Simple    L = N<sub>e</sub> + N<sub>o</sub>
* Freeman   L = N<sub>e</sub> + sqrt(2) \* N<sub>o</sub>
* Groen-Verbeek   L = 1.059 \* N<sub>e</sub> + 1.183 \* N<sub>o</sub>
* Profitt-Rosen   L = 0.984 \* N<sub>e</sub> + 1.340 \* N<sub>o</sub>
* Vossepoel-Smeulders    L = 0.980 \* N<sub>e</sub> + 1.406 \* N<sub>o</sub> - 0.091 \* N<sub>c</sub>
