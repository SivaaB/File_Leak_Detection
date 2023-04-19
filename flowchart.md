```mermaid
 graph TD;
    A[Main Menu]-->B[Sign up or log in]
    B -->|New User| C[Create Account]
    B -->|Existing User| D[Login]
    D --> E[SubMenu 2]
    E -->|Create File| F[Create]
    E -->|Open File| G[Open]
    E -->|Upload File| H[Upload]
    D --> I[SubMenu 3]
    I -->|Send Email| J[Send]
    I -->|View Inbox| K[View]
    L[Background Task - Daemon Thread] --> M[Compares Web and File Dictionary]
    M -->|If match, file leak has been detected| N[Sends an email to admin]
 ```
