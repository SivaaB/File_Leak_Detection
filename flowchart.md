```mermaid
graph TD
    A["Input: Child reaching for hot pot on stove"] --> B["PERCEPTION MODULE<br/>SceneAnalyzer"]
    
    B --> C["Entities"]
    B --> D["Hazards"]
    B --> E["Relationships"]
    
    C --> C1["child 👶<br/>age=toddler<br/>near stove"]
    C --> C2["hot_pot 🪣<br/>temp=high<br/>on stove"]
    
    D --> D1["thermal 🔥<br/>severity=high<br/>affects=child<br/>desc='scald risk'"]
    
    E --> E1["child → near → stove"]
    E --> E2["child → reaching → hot_pot"]
    E --> E3["hot_pot → on → stove"]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style C1 fill:#c8e6c9
    style C2 fill:#c8e6c9
    style D1 fill:#ffccbc
    style E1 fill:#f8bbd9
    style E2 fill:#f8bbd9
    style E3 fill:#f8bbd9
 ```
