# ContourEstimator

Program to calculate the contour length using different estimators. The contour is usually described using chaincode. Chaincode is describing the direction of the contour. This is usually done with the numbers 0 till 7, as seen in the table below. The x denotes the current position.

|   |   |   |
| - |:-:| -:|
| 3 | 2 | 1 |
| 4 | x | 0 |
| 5 | 6 | 7 |

The program uses the chaincode to calculate the length of the contour using different estimators. These are:

* Simple                  ''' L = '''
* Freeman
* Groen-Verbeek
* Profitt-Rosen
* Vossepoel-Smeulders
