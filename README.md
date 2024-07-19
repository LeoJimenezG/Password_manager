# Password_manager
Python program to help you register and manage your passwords, even generate new ones for you.

-- How does it work --
- Once you run the program a new window will be open (not resizable).
- There are three options: Add a new website-password, search a website-password and generate a password.
- Also there are three inputs, the input "Email/Username" will be already filled with a random example, but you can change it.
- ![image](https://github.com/user-attachments/assets/8e8835ca-6c8a-4ccc-8bb6-03865024167d)
1. Add a New Website-Password:
   - To add a new website-password register, you will have to fill up the three inputs.
   - Website input: introduce the name of the website which the information is used.
      - Example: email
    - Email/Username input: introduce the email address or the username you use on the website you already introduced.
      - Example: myemail123@gmail.com
    - Password input: introduce the password you use on the website you alredy introduced. The password will not be covered, in order to avoid any typing errors.
      - Example: mygmailpassword456
    - Once you fill up all the inputs and click on the "Add" button, you will need to make a confirmation of your information.
    - ![image](https://github.com/user-attachments/assets/f8e5d859-5764-42cc-8ca9-c58e053831d0)
    - If the information is good, click on the "Accept" button. The information will be saved and the inputs will go blank. 
    - If you don't fill up all the inputs, you will get a warning and the adding process will not be executed.
    - ![image](https://github.com/user-attachments/assets/a808e1c2-84a9-41ef-9ef4-1002e6ba4112)
2. Search a Website-Password:
    - To get the information you already added, use the name of the website you added.
    - If the website name you introduced is found, you will get the information saved.
    - ![image](https://github.com/user-attachments/assets/527e74c6-c788-4321-b45f-f8671fbb2ea5)
    - If the website name you introduced is not found, you will get a warning.
    - ![image](https://github.com/user-attachments/assets/60ae6f69-e0fa-435f-8648-693aac441ece)
3. Generate a Password:
    - To generate a random safe password, click on the "Generate Password" button.
    - And a password will be displayed in the Password input.
    - ![image](https://github.com/user-attachments/assets/eb5b188c-9a9a-45bd-8e4d-665496d4605d)
    - All passwords generated will be random and will contain 8 letters, 4 numbers and 4 special characters
  
- Saving the information
    - All the the information you Add will be saved in a json file named "passwords.json".
    - This file will be created in the same directory you have the program.
    - You can freely open the file and modify any information you want.
    - This is what the file would look like:
    - ![image](https://github.com/user-attachments/assets/29064ac5-e157-4534-acc4-41b26a11af85)

 

