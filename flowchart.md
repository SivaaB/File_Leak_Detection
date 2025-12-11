```mermaid
graph TD
    A["Scene Description<br/>'Child + hot pot'"] --> B["PlanningOrchestrator<br/>Algorithm 1"]
    
    B --> C["Step 1: SceneAnalyzer<br/>Entity + Hazard"]
    C --> D["Step 2: PlanGenerator<br/>Initial FSM<br/>9 states"]
    D --> E["Step 3: PlanEvaluator<br/>7 Dimensions<br/>Score: 6.2/10"]
    
    E --> F{"6.2 < 6.5<br/>Benchmark?"}
    F -->|YES| G["ITERATION 1<br/>Feedback:<br/>'Add ENSURE_SAFETY'"]
    G --> H["Regenerate +<br/>Synthetic Fix<br/>safety_priority=True"]
    H --> I["Re-evaluate<br/>Score: 7.8/10<br/>Δ +1.6"]
    
    I --> J{"7.8 > 6.5?"}
    J -->|YES| K["✓ PLANNING COMPLETE<br/>Final Score: 7.8/10<br/>1 iteration"]
    J -->|NO| L["ITERATION 2..."]
    
    F -->|NO| K
    
    style B fill:#e8f5e8
    style E fill:#f3e5f5
    style I fill:#c8e6c9
    style K fill:#e8f5e8
    style G fill:#ffebee
    style H fill:#fff3e0
    
    classDef success fill:#c8e6c9
    classDef feedback fill:#ffebee
 ```
