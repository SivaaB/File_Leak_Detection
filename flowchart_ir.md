```mermaid
graph TD
A [Dataset Collection] -> B [Dataset PreProcessing]
B -> C [Splitting Dataset into Training & Test Sets]
C -> D [Select ML Model]
D -> E [Train ML Model]
E -> F [Evaluate Model]
F -> G [Hyperparameter Tuning]
G -> H [Retrain and Reevaluate Model]
H -> I [Final Output]
 ```
