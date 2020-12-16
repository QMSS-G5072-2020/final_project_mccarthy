bs = BeautifulSoup(open('data/senators_cfm.xml'), 'xml')

from xml.etree.ElementTree import parse
document = parse('data/senators_cfm.xml')

first_name = []
last_name = []
state = []

for item in document.iterfind('member'):
    first_name.append(item.findtext('first_name'))
    last_name.append(item.findtext('last_name'))
    state.append(item.findtext('state'))
    
senator_list = pd.DataFrame({'first_name': first_name, 'last_name': last_name, 'state':state})
senator_list["full_name"] = senator_list["first_name"] + " " + senator_list["last_name"]

def get_senator(state):    
    assert isinstance(state, str), "This function only works with state names as strings."
    senator = senator_list[senator_list["state"] == state]
    senators = senator["full_name"]
    if senators.empty == True:
        print("This input is not supported. Try an abbreviation of one of the 50 states.")
    else:
        return senators
    

def get_senator_id(senator):
    key = os.getenv("FEC_API_KEY")
    assert isinstance(senator, str), "This function only works with senator names as strings."
    try:
        candidate_call = "https://api.open.fec.gov/v1/names/candidates/?api_key=" + key + "&q=" + senator
        candidate_id_call = requests.get(candidate_call)
        json_candidate_id = candidate_id_call.json()
        df_id = pd.DataFrame(json_candidate_id['results'])
        df_id = df_id[df_id["office_sought"] == "S"]
        df_id_return = str(df_id["id"].iloc[0])
        return df_id_return
    except (KeyError):
        print("This senator could not be found. Please try the name of a current U.S. senator.")
        
        
def get_state_ids(state):
    assert isinstance(state, str), "This function only works with state names as strings."
    try:
        for senator in get_senator(state):
            get_senator_id(senator)
    except TypeError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
def get_fec_totals_senator(senator):
    key = os.getenv("FEC_API_KEY")
    assert isinstance(senator, str), "This function only works with senator names as strings."
    try:
        senator_id = get_senator_id(senator)
        schedule_e_call = "https://api.open.fec.gov/v1/candidate/" + senator_id + "/totals/?api_key=" + key  
        call_expenditures = requests.get(schedule_e_call)
    
        json_sched_e = call_expenditures.json()
        df_sched_e = pd.DataFrame(json_sched_e['results'])
        df_sched_e = df_sched_e.sort_values(by=['last_report_year'])
        df_sched_e = df_sched_e.drop_duplicates(subset = 'last_report_year')
        df_sched_e.to_csv(f"{senator} FEC Data", index= True)
    except (TypeError, KeyError):
        print(f"{senator} could not be found. Please try the full name of a current U.S. senator.")
        

def get_fec_totals_state(state):
    assert isinstance(state, str), "This function only works with state names as strings."
    try:
        for senator in get_senator(state):
            get_fec_totals_senator(senator)
    except TypeError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
def lifetime_contributions_senator(senator):
    key = os.getenv("FEC_API_KEY")
    assert isinstance(senator, str), "This function only works with senator names as strings."
    try:
        senate_candidate_id = get_senator_id(senator)
        schedule_e_call = "https://api.open.fec.gov/v1/candidate/" + senate_candidate_id + "/totals/?api_key=" + key  
        call_expenditures = requests.get(schedule_e_call)
    
        json_sched_e = call_expenditures.json()
        df_sched_e = pd.DataFrame(json_sched_e['results'])
        df_sched_e = df_sched_e.sort_values(by=['last_report_year'])
        df_sched_e = df_sched_e.drop_duplicates(subset = 'last_report_year')
        lifetime_contributions = df_sched_e["individual_unitemized_contributions"].sum()
        print(f'{senator} has raised a total of ${lifetime_contributions} in unitemized contributions in his or her life.')
    except NameError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
def lifetime_contributions_state(state):
    assert isinstance(state, str), "This function only works with state names as strings."
    try:
        for senator in get_senator(state):
            lifetime_contributions_senator(senator)
    except TypeError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
        
def lifetime_expenditures_senator(senator):
    key = os.getenv("FEC_API_KEY")
    assert isinstance(senator, str), "This function only works with senator names as strings."
    try:
        senate_candidate_id = get_senator_id(senator)
    
        schedule_e_call = "https://api.open.fec.gov/v1/candidate/" + senate_candidate_id + "/totals/?api_key=" + key  
        call_expenditures = requests.get(schedule_e_call)
    
        json_sched_e = call_expenditures.json()
        df_sched_e = pd.DataFrame(json_sched_e['results'])
        df_sched_e = df_sched_e.sort_values(by=['last_report_year'])
        df_sched_e = df_sched_e.drop_duplicates(subset = 'last_report_year')
        lifetime_contributions = df_sched_e["operating_expenditures"].sum()
        print(f'{senator} has spent a total of ${lifetime_contributions} through his or her campaigns for office.')
    except NameError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
def lifetime_expenditures_state(state):
    assert isinstance(state, str), "This function only works with state names as strings."
    try:
        for senator in get_senator(state):
            lifetime_expenditures_senator(senator)
    except TypeError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
def get_fec_expenditures_senator(senator):
    key = os.getenv("FEC_API_KEY")
    assert isinstance(senator, str), "This function only works with senator names as strings."
    try:
        senate_candidate_id = get_senator_id(senator)
        schedule_e_call = "https://api.open.fec.gov/v1/candidate/" + senate_candidate_id + "/totals/?api_key=" + key  
        call_expenditures = requests.get(schedule_e_call)
    
        json_sched_e = call_expenditures.json()
        df_sched_e = pd.DataFrame(json_sched_e['results'])
        df_sched_e = df_sched_e.sort_values(by=['last_report_year'])
        df_sched_e = df_sched_e.drop_duplicates(subset = 'last_report_year')
        df_sched_e.plot.bar(x = 'last_report_year', y = ['receipts'], rot = 40, legend = None)
        plt.xlabel("Report Year")
        plt.ylabel("Dollars in Millions")
        plt.title(f"Over Time Campaign Expenditures for {senator}")
        print(plt.show)
    except NameError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
def get_fec_expenditures_state(state):
    assert isinstance(state, str), "This function only works with state names as strings."
    try:
        for senator in get_senator(state):
            get_fec_expenditures_senator(senator)
    except TypeError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
def get_fec_contributions_senator(senator):
    key = os.getenv("FEC_API_KEY")
    assert isinstance(senator, str), "This function only works with senator names as strings."
    try:
        senate_candidate_id = get_senator_id(senator)
        schedule_e_call = "https://api.open.fec.gov/v1/candidate/" + senate_candidate_id + "/totals/?api_key=" + key  
        call_expenditures = requests.get(schedule_e_call)
    
        json_sched_e = call_expenditures.json()
        df_sched_e = pd.DataFrame(json_sched_e['results'])
        df_sched_e = df_sched_e.sort_values(by=['last_report_year'])
        df_sched_e = df_sched_e.drop_duplicates(subset = 'last_report_year')
        df_sched_e.plot.bar(x = 'last_report_year', y = ['individual_unitemized_contributions'], rot = 40, legend = None)
        plt.xlabel("Report Year")
        plt.ylabel("Dollars in Millions")
        plt.title(f"Over Time Individual Unitemized Contributions for {senator}")
        print(plt.show)
    except NameError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
        
def get_fec_contributions_state(state):
    assert isinstance(state, str), "This function only works with state names as strings."
    try:
        for senator in get_senator(state):
            get_fec_contributions_senator(senator)
    except TypeError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")
        
def full_report_senator(senator):
    assert isinstance(senator, str), "This function only works with senator names as strings."
    try:
        print(f"Report on {senator}:")
        print("---------------------------")
        lifetime_contributions_senator(senator)
        lifetime_expenditures_senator(senator)
    
        get_fec_expenditures_senator(senator)
        get_fec_contributions_senator(senator)
    except IndexError as e:
        print(f"An error has occurred: {e}. Please check your inputs.")