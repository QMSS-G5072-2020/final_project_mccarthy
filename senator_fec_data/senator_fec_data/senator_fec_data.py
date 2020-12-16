def get_senator_list():
    """
    Returns a pandas DataFrame of current U.S. Senators.
    
    Parameters:
    ------------
    
    Output:
    ------------
    A pandas DataFrame object with three columns: first_name, last_name, and state.
    
    Example:
    ------------
    >> senator_list = get_senator_list()
    >> type(senator_list)
    pandas.core.frame.DataFrame
    """
    bs = BeautifulSoup(open('data/senators_cfm.xml'), 'xml')
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
    
    return senator_list