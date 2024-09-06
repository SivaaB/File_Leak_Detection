```mermaid
graph TD
A [Dataset Collection] --> B 
B [Dataset PreProcessing] --> C 
C [Splitting Dataset into Training & Test Sets] --> D 
D [Select ML Model] --> E 
E [Train ML Model] -> F
F [Evaluate Model] --> G 
G [Hyperparameter Tuning] --> H 
H [Retrain and Reevaluate Model] -> I [Final Output]
 ```
