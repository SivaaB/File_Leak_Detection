```mermaid
 graph TD;
    A[Start] --> B[Background_task]
    B --> M[Save_mail]
    A --> C[Main_menu]
    
    
    C -->|Sign-in| D[Save_user]
    C -->|Login-in| E[SubMenu2]
    
    E -->|Mail| F[Submenu3]
    F -->|Send Mail| G[Save_mail]
    F -->|View Mail| H[view_mail]
    H --> I[Load_mail]
    
    C -->|Create| J[save_company]
    C -->|Open| K[Upload]
    C -->|Back to previous menu| L[Main_menu]
 ```
