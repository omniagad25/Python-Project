import json

class FundRaiseCampaign:
    def __init__(self, title=None, details=None, total_target=None, start_date=None, end_date=None, user_email=None):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date
        self.logged_in_user_email = user_email

    def read_file(self):
        try:
            with open('campaigns.json', 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_file(self, campaigns_data):
        with open('campaigns.json', 'w') as file:
            json.dump(campaigns_data, file, indent=4)


    def user_own_projects(self, user_email):
        data = self.read_file()
        return [campaign for campaign in data if campaign.get('user_email') == user_email]

    def create_campaign(self, user_email):
        title = input("Enter campaign title: ")
        if not title.strip():
            print("This field is required.")
            return

        details = input("Enter campaign details: ")
        if not details.strip():
            print("This field is required.")
            return

        total_target = input("Enter total target amount in egyptian pounds: ")
        if not total_target.strip():
            print("This field is required.")
            return

        start_date = input("Enter start date (YYYY-MM-DD): ")
        if not start_date.strip():
            print("This field is required.")
            return

        end_date = input("Enter end date (YYYY-MM-DD): ")
        if not end_date.strip():
            print("This field is required.")
            return

        campaign = {
            "title": title,
            "details": details,
            "total_target": total_target,
            "start_date": start_date,
            "end_date": end_date,
            "user_email": user_email
        }

        campaigns_data = self.read_file()
        campaigns_data.append(campaign)
        self.write_file(campaigns_data)

        print("Campaign created successfully.")

    def view_projects(self):
        projects_data = self.read_file()
        if not projects_data:
            print("No projects found.")
            return

        index = 1
        for campaign in projects_data:
            print(f"Project {index}:\n"
                  f"Title: {campaign['title']}\n"
                  f"Details: {campaign['details']}\n"
                  f"Total Target: {campaign['total_target']}\n"
                  f"Start Date: {campaign['start_date']}\n"
                  f"End Date: {campaign['end_date']}\n")
            index += 1
    
    def delete_project(self, user_email):
        user_projects = self.user_own_projects(user_email)
        if not user_projects:
            print("You don't have any projects to delete.")
            return
        print("Your projects:")
        for index, campaign in enumerate(user_projects, start=1):
            print(f"Project {index}:")
            print(f"Title: {campaign['title']}")
            print(f"Details: {campaign['details']}")
            print(f"Total Target: {campaign['total_target']}")
            print(f"Start Date: {campaign['start_date']}")
            print(f"End Date: {campaign['end_date']}")
            print()

        campaign_to_delete = input("Enter the project number to delete: ")
        try:
            campaign_index = int(campaign_to_delete) - 1
            if 0 <= campaign_index < len(user_projects):
                del user_projects[campaign_index]
                all_projects = self.read_file()
                remaining_projects = [project for project in all_projects if project['user_email'] != user_email]
                remaining_projects.extend(user_projects)
                self.write_file(remaining_projects)
                print("Project deleted successfully.")
            else:
                print("Invalid project number.")
        except ValueError:
            print("Invalid input. Please enter a valid project number.")


    def edit_project(self, user_email):
        user_projects = self.user_own_projects(user_email)
        if not user_projects:
            print("You don't have any projects to edit.")
            return
        
        print("Your projects:")
        for index, campaign in enumerate(user_projects, start=1):
            print(f"Project {index}:")
            print(f"Title: {campaign['title']}")
            print(f"Details: {campaign['details']}")
            print(f"Total Target: {campaign['total_target']}")
            print(f"Start Date: {campaign['start_date']}")
            print(f"End Date: {campaign['end_date']}")
            print()
        
        project_to_edit = input("Enter the project number to edit: ")
        try:
            project_index = int(project_to_edit) - 1
            if 0 <= project_index < len(user_projects):
                project = user_projects[project_index]
                title = input("Enter new campaign title (leave blank to keep current): ")
                if title.strip():
                    project['title'] = title
                
                details = input("Enter new campaign details (leave blank to keep current): ")
                if details.strip():
                    project['details'] = details
                
                total_target = input("Enter new total target amount in Egyptian pounds (leave blank to keep current): ")
                if total_target.strip():
                    project['total_target'] = total_target
                
                start_date = input("Enter new start date (YYYY-MM-DD) (leave blank to keep current): ")
                if start_date.strip():
                    project['start_date'] = start_date
                
                end_date = input("Enter new end date (YYYY-MM-DD) (leave blank to keep current): ")
                if end_date.strip():
                    project['end_date'] = end_date
                
                all_projects = self.read_file()
                remaining_projects = [project for project in all_projects if project['user_email'] != user_email]
                remaining_projects.extend(user_projects)
                self.write_file(remaining_projects)
            else:
                print("Invalid project number.")
        except ValueError:
            print("Invalid input. Please enter a valid project number.")
