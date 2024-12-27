# Password Manager 🔒
A Python program to help you easly register, manage, and even generate passwords for your online accounts.

---

## 📘 How Does It Work?

- When you run the program, a new non-resizable window will open.  
- The application provides three main functionalities:  
  1. Add a new website-password entry.
  2. Search for an existing website-password entry.  
  3. Generate a secure random password.  
- The `Email/Username` input field is pre-filled with a random example, but you can modify it.  

  ![App Interface Example](https://github.com/user-attachments/assets/8e8835ca-6c8a-4ccc-8bb6-03865024167d)  

---

## 🛠️ Aplication Functionalities

### Add a New Website-Password  

To register a new entry, follow these steps:  
1. **Fill in the three input fields:**  
   - `Website`: Enter the name of the website for which you're saving credentials.  
   - `Email/Username`: Provide the email or username you use for the website.  
   - `Password`: Type the password you use for the website.  
     - *Note: The password is visible to avoid typing errors.*  

2. **Save the Entry:**  
   - After filling all inputs, click the **"Add"** button.  
   - A confirmation prompt will appear to verify the entered information.  

     ![Confirmation Prompt](https://github.com/user-attachments/assets/f8e5d859-5764-42cc-8ca9-c58e053831d0)  
   - If everything looks correct, click **"Accept"** to save the entry.  
   - If any input is missing, a warning message will appear, and the entry won't be saved.  

     ![Warning Message](https://github.com/user-attachments/assets/a808e1c2-84a9-41ef-9ef4-1002e6ba4112)  

3. Once saved, all inputs will be cleared for the next entry or set back to the default values.  

### Search for a Website-Password

To retrieve saved credentials:  
1. Enter the website name in the `Website` input field.  
2. Click the **"Search"** button:  
   - If the website is found, the saved email/username and password will be displayed.  

     ![Search Success Example](https://github.com/user-attachments/assets/527e74c6-c788-4321-b45f-f8671fbb2ea5)  
   - If the website isn't found, a warning message will appear.  

     ![Search Failure Example](https://github.com/user-attachments/assets/60ae6f69-e0fa-435f-8648-693aac441ece)  

### Generate a Secure Password  

To generate a random password:  
1. Click the **"Generate Password"** button.  
2. A new password will appear in the `Password` input field.  
   - Generated passwords will always follow this pattern:  
     - 8 letters, 4 numbers, and 4 special characters.  
   
   ![Password Generation Example](https://github.com/user-attachments/assets/eb5b188c-9a9a-45bd-8e4d-665496d4605d)  

### Saving the Information 

- All added entries are stored in a file named `passwords.json`.  
- This file is created in the same directory as the program.  
- The file is in JSON format, making it easy to read or manually edit if necessary.  
- Example of the JSON structure:  

  ![JSON File Example](https://github.com/user-attachments/assets/29064ac5-e157-4534-acc4-41b26a11af85)  

---

## 💡 Notes

- Ensure Python and the necessary libraries are properly installed.  
- The program is intended for personal use only and easier password management.  
- Always keep your `passwords.json` file in a secure location, because the program does not offer any actual security.

Start easly managing your digital life!
