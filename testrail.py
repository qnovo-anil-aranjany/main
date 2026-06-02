from testrail_api import TestRailAPI

client = "https://qnovocorp.testrail.io"
client_user = "aaranjany@qnovocorp.com"
client_password = ""



def get_all_projects(limit=250, offset=0, **kwargs):
    print("Testrail: get_all_projects")
    return testrail.projects.get_projects(limit, offset, is_completed=0)


def get_all_plans_from_project_id(project_id, limit=250, offset=0, **kwargs):
    plans = testrail.plans.get_plans(project_id, **kwargs)
    return(plans)

def get_all_test_suite_from_project_id(project_id):
    print(f"Get suites from project_id : {project_id}")
    # get all suites
    return testrail.suites.get_suites(project_id)

def get_all_sections_from_pid(project_id, limit=250, offset=0, **kwargs):
    print("Get all sections afrom project id {project_id}")
    sections = testrail.sections.get_sections(project_id, **kwargs)
    return sections


def get_all_tests_from_testsuite(project_id, **kwargs):
    print("get_all_tests_from_testsuite")
    return testrail.cases.get_cases(project_id, **kwargs)

if __name__ == '__main__':
    testrail = TestRailAPI(client, client_user, client_password)
    res = get_all_projects() 
    #print(res)
    for p in res["projects"]:
        print(p)
        print()
    res = get_all_plans_from_project_id(2)
    #print(res)

    res = get_all_test_suite_from_project_id(2)
    print(res)

    res = get_all_sections_from_pid(2, suite_id=3)
    print(res)

    print()
    print()
    print()
    print()
    #res = get_all_tests_from_testsuite(2, suite_id=3, section_id=6)
    res = get_all_tests_from_testsuite(2,  suite_id=3)
    print(res)
