from projects import FundRaiseCampaign
from authentication import Authentication

def main():
    auth = Authentication()
    logged_in = False
    fundraise_campaign = FundRaiseCampaign()

    while True:
        if not logged_in:
            choice = input("1- Register\n2- Login\n3- Exit\nEnter your choice: ")
            if choice == "1":
                auth.register()
            elif choice == "2":
                logged_in = auth.login()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            choice = input("1- Create Campaign\n2- View Projects\n3- Delete Project\n4- Edit Project\n5- Logout\nEnter your choice: ")
            if choice == "1":
                user_email = auth.get_logged_in_user_email()
                fundraise_campaign.create_campaign(user_email)
            elif choice == "2":
                fundraise_campaign.view_projects()
            elif choice == "3":
                user_email = auth.get_logged_in_user_email()
                fundraise_campaign.delete_project(user_email)
            elif choice == "4":
                user_email = auth.get_logged_in_user_email()
                fundraise_campaign.edit_project(user_email)
            elif choice == "5":
                logged_in = False
                print("Logged out successfully.")
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
