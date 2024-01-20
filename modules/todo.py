"""Supports the todo section in the main.py file."""


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
    
     

    # st.markdown(f'''username: **{st.session_state.username}**''')
    # st.markdown(
    #     '''Except for username column, others can be edited but table cannot be saved.
    #     This is only a demo to check that the username who logged in is the same as the
    #     username shown in this table.
    #     ''')

    # todo = ToDo(st.session_state.username)
    # st.data_editor(
    #     todo.get_todo(),
    #     column_config={
    #         'due': st.column_config.DateColumn(format="YYYY-MM-DD"),
    #         'username': st.column_config.TextColumn(disabled=True),
    #         'category': st.column_config.SelectboxColumn(options=['personal', 'work', 'others']),
    #     },
    #     use_container_width=True,
    #     hide_index=True,
    #     key='data_editor_k'
    # )
