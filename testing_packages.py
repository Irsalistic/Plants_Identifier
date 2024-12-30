import pkg_resources


def list_installed_packages():
    print("Installed packages and their versions:\n")
    for dist in pkg_resources.working_set:
        print(f"{dist.project_name}=={dist.version}")


# Run the function
if __name__ == "__main__":
    list_installed_packages()
