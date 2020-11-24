def email_slicer(email):
    username = email[:email.index("@")]
    domain = email[email.index("@")+1:]

    print(f"You're new username is '{username}' from the domain '{domain}'")

if __name__ == '__main__':
    email = input("Enter your email address: ").strip()
    email_slicer(email)