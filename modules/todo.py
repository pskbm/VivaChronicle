import pandas as pd


data = {
    'username': ['alan']*5 + ['boyet']*5,
    'desc': ['Todo1', 'Todo2', 'Todo3', 'Todo4', 'Todo5', 'Todo6', 'Todo7', 'Todo8', 'Todo9', 'Todo10'],
    'due': ['2024-01-10', '2024-01-15', '2024-01-20', '2024-01-25', '2024-02-01', 
            '2024-02-05', '2024-02-10', '2024-02-15', '2024-02-20', '2024-02-25'],
    'category': ['personal', 'work', 'others', 'personal', 'work', 
                 'others', 'personal', 'work', 'others', 'personal']
}

class ToDo:
    def __init__(self, username):
        self.username = username

    def get_todo(self):
        df = pd.DataFrame(data)
        df['due'] = pd.to_datetime(df['due'])
        return df[df['username'] == self.username]
