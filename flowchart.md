```mermaid
graph TD
    A["Scene Analysis<br/>thermal + child"] --> B["PlanGenerator<br/>LLMgen Simulation"]
    
    B --> C["INITIAL<br/>assess_situation"]
    C --> D["ASSESS_HAZARD ⭐<br/>safety_priority=True<br/>check_proximity"]
    
    D -->|high_risk| E["URGENT_ACTION<br/>grab, lift, lower"]
    D -->|medium_risk| F["PREVENTIVE_ACTION<br/>distract ⭐, move_away"]
    
    E --> G["ENSURE_SAFETY ⭐<br/>verify_safety, monitor"]
    F --> H["MONITOR_SITUATION<br/>monitor, check_proximity"]
    
    G --> H
    H -->|hazard_persists| D
    H -->|stable| I["TERMINAL"]
    
    J["CALL_FOR_HELP ⭐<br/>call_for_help"] --> I
    
    style B fill:#e8f5e8
    style D fill:#ffccbc
    style E fill:#ffcdd2
    style F fill:#c8e6c9
    style G fill:#ffccbc
    style H fill:#e0f2f1
    style I fill:#f5f5f5
    style J fill:#ffccbc
    
    classDef safety fill:#ffccbc
    classDef cognitive fill:#c8e6c9
    classDef urgent fill:#ffcdd2
 ```
